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

## Known limitations

- A compatible x86_64 SteamCMD setup, Box64 and matching runtime libraries must already be available on the ARM64 host.
- Installation through PufferPanel's `steamgamedl` operation may fail without host-specific compatibility setup.
- The supervisor uses process signals, which have **not been verified to save and stop both shards gracefully**. Do not deploy it with valuable worlds.
- A shared console and shared start/stop control replace independent shard controls.
- A future parameterized single-shard template could be instantiated twice for independent management, but the two instances would need explicitly shared game and cluster storage.
- Do not expose the internal shard synchronization port to the public Internet.

Run new installations with test credentials, disposable worlds and non-conflicting ports. Check startup logs, shard connectivity, world generation and save/shutdown behavior before production use.
