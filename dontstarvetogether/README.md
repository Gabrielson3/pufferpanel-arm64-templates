# Don't Starve Together — ARM64 via Box64 (Master + Caves)

The [DST template](dst-arm64-box64-master-caves.json) uses **one PufferPanel server** to launch **two dedicated-server processes** with separate shard configuration:

```text
DoNotStarveTogether/DontStarveTogetherServer/
  cluster.ini
  cluster_token.txt             # generated locally; never commit credentials
  Master/server.ini
  Caves/server.ini
  Caves/worldgenoverride.lua   # DST_CAVE preset
```

The script starts `-shard Master`, pauses briefly, and then starts `-shard Caves`. Both use the same cluster and storage root. The internal shard connection is localhost-only (`127.0.0.1`); public game ports must differ between the shards.

The token is entered on the private PufferPanel server instance. The cluster synchronization key is generated locally the first time the cluster starts.

## Requirements and first installation

This is a PufferPanel **host** template for Linux ARM64/AArch64. It requires PufferPanel 3, Box64 (tested with **0.4.4**), compatible x86_64 runtime libraries, Python 3, Bash, `od` and `sed`.

The template uses `steamgamedl` to install the Linux x86_64 server (Steam app **343050**); ARM64 hosts may need a compatible Steam download tool configured separately.

Generate a private cluster token through [Klei's server account page](https://accounts.klei.com/account/game/servers?game=DontStarveTogether). Import [the JSON template](dst-arm64-box64-master-caves.json), supply the token in your **private** PufferPanel server instance and choose different game ports for Master (**10999/UDP** by default) and Caves (**11000/UDP** by default). The internal shard synchronization port **10889** is localhost-only: never expose it publicly.

The template embeds the scripts it writes into the game instance on startup. Their maintained sources are [the shard supervisor](scripts/start-dst-master-caves.sh) and [the settings synchronizer](scripts/configure-dst.py); these files do **not** have to be downloaded separately for a fresh installation.

## Functional test status

Validated on one Ubuntu 22.04 ARM64 host with PufferPanel 3.0.9 and Box64 0.4.4:

- Dedicated server installed and both Master and Caves launched.
- Both world maps generated; one cave world-generation attempt failed and the game's automatic retry completed successfully.
- Both shards connected over localhost and a player authenticated, entered the surface, and migrated through a cave entrance.
- During a controlled PufferPanel stop with the player in Caves, logs confirmed `Saving Dedicated server data...`, `Serializing world`, and `Stopping shard mode` for **both** shards.
- A later startup successfully loaded the saved Master and Caves worlds, and the player's cave location was restored.

This is an observed successful lifecycle test, **not** a guarantee of crash safety, unattended operation, or correct behavior on all hosts and future versions. Keep backups of important worlds.

## PufferPanel settings and access control

This template now exposes the following values in PufferPanel's server variables:

- Server name, description, password, player limit and Survival game mode.
- **Reserved whitelist slots** (`whitelistslots`, default `0`): this is a **reserved-seat mechanism**, not a guaranteed allowlist. Reserving all available seats without enough listed users does not automatically block outsiders. Server owners or admins may also be unsuitable accounts for testing access restrictions.
- **Whitelist ID management** (`whitelistmode`, default `file`):
  - **File manager:** maintain `whitelist.txt` beside `cluster.ini`; startup leaves this file untouched.
  - **PufferPanel:** enter a comma-separated list of Klei IDs beginning with `KU_` in the `whitelistids` field. Each startup replaces `whitelist.txt` with those IDs, removes duplicates, and verifies the format. An empty field deliberately clears the list in panel mode. Do not manually edit the list while panel mode is enabled, because the next start overwrites those edits.
- PvP and pause-when-empty toggles.
- **Steam group only:** when enabled, membership in the supplied decimal Steam group ID is required. An empty/zero ID is rejected when group-only access is enabled. This is a separate access mechanism from DST's reserved slots.
- `adminlist.txt` and `blocklist.txt` live beside `cluster.ini` and are managed in the PufferPanel file manager. One Klei `KU_` ID per line.

The new-install template creates empty `whitelist.txt`, `adminlist.txt`, and `blocklist.txt` only when missing. The cluster token is supplied privately in the server variables and must never be committed.

### Applying changes without overwriting worlds

At each start, the PufferPanel `run.pre` step writes the latest helper scripts, then `configure_dst.py` synchronizes **only these keys** in the existing `cluster.ini`:

- `[GAMEPLAY]`: `game_mode`, `max_players`, `pvp`, `pause_when_empty`
- `[NETWORK]`: `cluster_name`, `cluster_description`, `cluster_password`, `whitelist_slots`
- `[STEAM]`: `steam_group_only`, `steam_group_id`

Other INI keys, other files, the cluster synchronization key, and both shard worlds are not modified. The helper keeps a one-time `cluster.ini.before-panel-management` backup before its first actual change; `whitelist.txt.before-panel-management` is likewise saved once if panel mode first overwrites an existing list. Settings owned by PufferPanel take precedence over manual edits to those specific managed INI keys on the next startup.

The obsolete `-console` flag has been removed from the launcher: `[MISC] console_enabled = true` remains active.

### Existing instances

Updating the GitHub template **does not** automatically change already-created server definitions. To migrate an existing instance without deleting worlds, download the updated template JSON and the [upgrade helper](scripts/upgrade-dst-instance.py), stop the game and PufferPanel service, preview the upgrade, then apply it. The helper preserves existing variable values, imports newly-managed `whitelist_slots`, PvP, pause and Steam group values from the instance's current `cluster.ini`, and backs up the instance JSON before replacing its `data` and `run` sections. Its default whitelist mode is `file`, preserving existing lists. Review the new variables before restarting. The upgrade helper does not alter world saves, cluster token or cluster configuration directly.

The upgrade helper syntax is:

```sh
python3 upgrade-dst-instance.py SERVER_ID latest-template.json
sudo python3 upgrade-dst-instance.py SERVER_ID latest-template.json --apply
```

The game and PufferPanel service must already be stopped when running `--apply`. Do not put private instance files in a public repository.

## Known limitations

- A compatible x86_64 game-download setup, Box64 and matching runtime libraries must already be available on the ARM64 host. The `steamgamedl` operation can require host-specific compatibility setup.
- The supervisor uses process signals for controlled shutdown. Graceful saves were observed for both shards in the test, but forced termination or process crashes remain untested.
- A shared console and shared start/stop control replace independent shard controls.
- A future parameterized single-shard template could be instantiated twice for independent management, but the two instances would need explicitly shared game and cluster storage.
- Do not expose the internal shard synchronization port to the public Internet.

Run new installations with test credentials, disposable worlds and non-conflicting ports. Check startup logs, shard connectivity, world generation, reload behavior and save/shutdown behavior before production use.

This is not an official PufferPanel template. For details on ChatGPT's contribution, see [authorship and AI assistance](../README.md#authorship-and-ai-assistance).
