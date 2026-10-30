#!/usr/bin/env python3
"""Upgrade a stopped DST PufferPanel 3 server JSON to the latest template.

Preserves existing user variable values and infers newly-added options from
cluster.ini. Does not read or modify world data and does not print credentials.
Run while the instance and PufferPanel service are stopped.
"""
import argparse
import copy
import json
import os
import re
import shutil
import stat
import tempfile
from datetime import datetime
from pathlib import Path


def read_ini(path):
    found = {}
    if not path.exists():
        return found
    section = None
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        match = re.match(r"^\s*\[([A-Za-z0-9_]+)\]", line)
        if match:
            section = match.group(1).upper()
            continue
        match = re.match(r"^\s*([A-Za-z0-9_]+)\s*=\s*(.*?)\s*$", line)
        if match and section:
            found[(section, match.group(1).lower())] = match.group(2)
    return found


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("server_id", help="PufferPanel instance ID (not the world name)")
    parser.add_argument("template", type=Path, help="Latest DST template JSON downloaded from the public repository")
    parser.add_argument("--panel-root", type=Path, default=Path("/var/lib/pufferpanel"))
    parser.add_argument("--apply", action="store_true", help="Actually upgrade the instance (otherwise preview only)")
    args = parser.parse_args()
    if not re.fullmatch(r"[A-Za-z0-9_-]+", args.server_id):
        parser.error("Invalid server ID")
    target = args.panel_root / "servers" / (args.server_id + ".json")
    cluster_ini = args.panel_root / "servers" / args.server_id / "DoNotStarveTogether" / "DontStarveTogetherServer" / "cluster.ini"
    template = json.loads(args.template.read_text(encoding="utf-8"))
    server = json.loads(target.read_text(encoding="utf-8"))
    if server.get("type") != "dst-arm64-master-caves" or template.get("type") != server.get("type"):
        parser.error("Not a matching DST Master+Caves server/template")
    if not isinstance(server.get("data"), dict) or not isinstance(template.get("data"), dict):
        parser.error("Invalid server/template data")
    ini = read_ini(cluster_ini)
    from_ini = {
        "whitelistslots": ini.get(("NETWORK", "whitelist_slots"), "0"),
        "pvp": ini.get(("GAMEPLAY", "pvp"), "false"),
        "pausewhenempty": ini.get(("GAMEPLAY", "pause_when_empty"), "true"),
        "steamgrouponly": ini.get(("STEAM", "steam_group_only"), "false"),
        "steamgroupid": ini.get(("STEAM", "steam_group_id"), "0"),
    }
    upgraded_data = copy.deepcopy(template["data"])
    for key, definition in upgraded_data.items():
        if key in server["data"] and isinstance(server["data"][key], dict) and "value" in server["data"][key]:
            definition["value"] = server["data"][key]["value"]
        elif key in from_ini:
            raw = from_ini[key]
            definition["value"] = int(raw) if key == "whitelistslots" else raw
    for key, definition in server["data"].items():
        if key not in upgraded_data:
            upgraded_data[key] = definition  # Preserve custom instance variables.
    server["data"] = upgraded_data
    server["run"] = copy.deepcopy(template["run"])
    print("DST instance JSON located; settings and existing values will be preserved.")
    print("New variables:", ", ".join(k for k in template["data"] if k not in json.loads(target.read_text(encoding="utf-8"))["data"]))
    print("Updated run configuration: yes")
    if not args.apply:
        print("Preview only: no changes written. Pass --apply to save with backup.")
        return
    suffix = datetime.now().strftime("%Y%m%d-%H%M%S")
    backup = target.with_name(target.name + ".before-dst-upgrade-" + suffix)
    shutil.copy2(target, backup)
    original = target.stat()
    fd, temp = tempfile.mkstemp(prefix=".dst-upgrade-", dir=target.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(server, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
        os.chmod(temp, stat.S_IMODE(original.st_mode))
        os.chown(temp, original.st_uid, original.st_gid)
        os.replace(temp, target)
    finally:
        if os.path.exists(temp):
            os.unlink(temp)
    print("DST instance updated. Backup saved beside its JSON file.")
    print("Start PufferPanel and review the new server variables before launching.")


if __name__ == "__main__":
    main()
