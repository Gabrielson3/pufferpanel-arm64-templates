#!/usr/bin/env python3
"""Synchronize selected PufferPanel DST variables without replacing custom config.

Only keys explicitly owned by this template are updated in cluster.ini.
The three Klei user-list files are preserved unless whitelist management is
explicitly set to 'panel'. Never commit generated configuration or credentials.
"""
import os
import re
import stat
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CLUSTER = ROOT / "DoNotStarveTogether" / "DontStarveTogetherServer"
INI = CLUSTER / "cluster.ini"


def env(name, optional=False):
    value = os.environ.get(name)
    if value is None and optional:
        return ""
    if value is None:
        raise ValueError(f"Missing PufferPanel environment variable: {name}")
    return value


def one_line(value, name):
    if "\n" in value or "\r" in value or "\x00" in value:
        raise ValueError(f"{name} must be a single line")
    return value


def switch(name):
    value = env(name).lower()
    if value not in ("true", "false"):
        raise ValueError(f"{name} must be true or false")
    return value


def number(name, low, high):
    value = env(name)
    if not re.fullmatch(r"[0-9]+", value):
        raise ValueError(f"{name} must be an integer")
    result = int(value)
    if not low <= result <= high:
        raise ValueError(f"{name} must be between {low} and {high}")
    return result


def replace_ini_keys(original, changes):
    """Preserve unknown sections, comments and keys; update only managed values."""
    result = []
    section = None
    sections_seen = set()
    keys_seen = set()

    def append(text):
        if result and not result[-1].endswith("\n"):
            result.append("\n")
        result.append(text)

    def finish_section():
        if section not in changes:
            return
        for key, value in changes[section].items():
            if key not in keys_seen:
                append(f"{key} = {value}\n")

    for line in original.splitlines(keepends=True):
        header = re.match(r"^\s*\[([A-Za-z0-9_]+)\]\s*(?:[;#].*)?$", line.strip())
        if header:
            finish_section()
            section = header.group(1).upper()
            sections_seen.add(section)
            keys_seen = set()
            append(line)
            continue
        key_match = re.match(r"^\s*([A-Za-z0-9_]+)\s*=", line)
        if key_match and section in changes and key_match.group(1).lower() in changes[section]:
            key = key_match.group(1).lower()
            if key not in keys_seen:
                append(f"{key} = {changes[section][key]}\n")
                keys_seen.add(key)
        else:
            append(line)
    finish_section()
    for missing, settings in changes.items():
        if missing not in sections_seen:
            append(f"\n[{missing}]\n")
            for key, value in settings.items():
                append(f"{key} = {value}\n")
    return "".join(result)


def write_if_changed(path, content):
    original = path.read_text(encoding="utf-8") if path.exists() else None
    if original == content:
        return False
    backup = path.with_suffix(path.suffix + ".before-panel-management")
    if original is not None and not backup.exists():
        import shutil
        shutil.copy2(path, backup)
    fd, temp = tempfile.mkstemp(prefix=".dst-config-", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(content)
        if path.exists():
            os.chmod(temp, stat.S_IMODE(path.stat().st_mode))
        else:
            os.chmod(temp, 0o600)
        os.replace(temp, path)
    finally:
        if os.path.exists(temp):
            os.unlink(temp)
    return True


def parse_ids(raw):
    unique = []
    seen = set()
    for candidate in re.split(r"[,;\s]+", raw.strip()):
        if not candidate:
            continue
        if not re.fullmatch(r"KU_[A-Za-z0-9_]+", candidate):
            raise ValueError("Invalid whitelist Klei User ID; expected KU_... entries")
        if candidate not in seen:
            seen.add(candidate)
            unique.append(candidate)
    return unique


def main():
    if not INI.is_file():
        raise ValueError("Missing cluster.ini; complete the DST installation first")

    name = one_line(env("DST_SERVER_NAME"), "server name").strip()
    if not name:
        raise ValueError("Server name cannot be empty")
    description = one_line(env("DST_DESCRIPTION", optional=True), "description")
    password = one_line(env("DST_PASSWORD", optional=True), "server password")
    max_players = number("DST_MAX_PLAYERS", 1, 64)
    reserved = number("DST_RESERVED_SLOTS", 0, max_players)
    game_mode = env("DST_GAME_MODE")
    if game_mode != "survival":
        raise ValueError("Unsupported game mode; use survival")
    pvp = switch("DST_PVP")
    pause = switch("DST_PAUSE_WHEN_EMPTY")
    group_only = switch("DST_STEAM_GROUP_ONLY")
    group_id = env("DST_STEAM_GROUP_ID")
    if not re.fullmatch(r"[0-9]+", group_id):
        raise ValueError("Steam group ID must contain decimal digits only")
    if group_only == "true" and int(group_id) == 0:
        raise ValueError("A Steam group ID is required when Steam-group-only is enabled")
    list_mode = env("DST_WHITELIST_MODE")
    if list_mode not in ("file", "panel"):
        raise ValueError("Whitelist management must be 'file' or 'panel'")
    listed_ids = parse_ids(env("DST_WHITELIST_IDS", optional=True)) if list_mode == "panel" else []

    changes = {
        "GAMEPLAY": {
            "game_mode": game_mode,
            "max_players": str(max_players),
            "pvp": pvp,
            "pause_when_empty": pause,
        },
        "NETWORK": {
            "cluster_name": name,
            "cluster_description": description,
            "cluster_password": password,
            "whitelist_slots": str(reserved),
        },
        "STEAM": {
            "steam_group_only": group_only,
            "steam_group_id": str(int(group_id)),
        },
    }
    ini_updated = write_if_changed(INI, replace_ini_keys(INI.read_text(encoding="utf-8"), changes))
    if list_mode == "panel":
        write_if_changed(CLUSTER / "whitelist.txt", "".join(x + "\n" for x in listed_ids))
    if list_mode == "panel":
        id_count = len(listed_ids)
    elif (CLUSTER / "whitelist.txt").exists():
        with (CLUSTER / "whitelist.txt").open(encoding="utf-8", errors="replace") as handle:
            id_count = len(set(
                line.strip() for line in handle
                if re.fullmatch(r"KU_[A-Za-z0-9_]+", line.strip())
            ))
    else:
        id_count = 0
    if reserved > id_count:
        print("DST note: reserved slots exceed the listed Klei IDs; this is not an exclusive whitelist.")
    print("DST panel settings checked" + (" and updated" if ini_updated else " (unchanged)"))


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, UnicodeError) as exc:
        raise SystemExit(f"DST configuration error: {exc}")
