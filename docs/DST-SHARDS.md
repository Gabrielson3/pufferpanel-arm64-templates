# Don't Starve Together: Master + Caves

The [experimental DST template](../templates/dst-arm64-box64-master-caves.json) uses **one PufferPanel server** to launch **two dedicated-server processes** with separate shard configuration:

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

## Functional test status

Validated on one Ubuntu 22.04 ARM64 host with PufferPanel 3.0.9 and Box64 0.4.4:

- Dedicated server installed and both Master and Caves launched.
- Both world maps generated; one cave world-generation attempt failed and the game's automatic retry completed successfully.
- Both shards connected over localhost and a player authenticated, entered the surface, and migrated through a cave entrance.
- During a controlled PufferPanel stop with the player in Caves, logs confirmed `Saving Dedicated server data...`, `Serializing world`, and `Stopping shard mode` for **both** shards.
- A later startup successfully loaded the saved Master and Caves worlds, and the player's cave location was restored.

This is an observed successful lifecycle test, **not** a guarantee of crash safety, unattended operation, or correct behavior on all hosts and future versions. Keep backups of important worlds.

## Access control

The DST `whitelist.txt` feature **reserves player slots**; it must not be treated as a strict admission-control list. In the test, `whitelist_slots = 6` with six total slots and no matching listed player IDs did **not** prevent a connection. The connection also used the token owner's administrative account, so it is not a conclusive test of how an ordinary unlisted player is treated. Use a server password and, when necessary, additional access restrictions; never assume an empty whitelist blocks everyone.

## Known limitations

- A compatible x86_64 game-download setup, Box64 and matching runtime libraries must already be available on the ARM64 host. The `steamgamedl` operation can require host-specific compatibility setup.
- The supervisor uses process signals for controlled shutdown. Graceful saves were observed for both shards in the test, but forced termination or process crashes remain untested.
- A shared console and shared start/stop control replace independent shard controls.
- A future parameterized single-shard template could be instantiated twice for independent management, but the two instances would need explicitly shared game and cluster storage.
- Do not expose the internal shard synchronization port to the public Internet.

Run new installations with test credentials, disposable worlds and non-conflicting ports. Check startup logs, shard connectivity, world generation, reload behavior and save/shutdown behavior before production use.
