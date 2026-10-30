# PufferPanel ARM64 templates

Experimental community-style [PufferPanel](https://www.pufferpanel.com/) 3 templates for Linux ARM64 / AArch64 servers.

| Game | Runtime | Template |
| --- | --- | --- |
| Minecraft Java | Native ARM64 Java | [Minecraft](templates/minecraft-java-arm64.json) |
| Valheim | Linux x86_64 via Box64 | [Valheim](templates/valheim-arm64-box64.json) |
| Don't Starve Together | Linux x86_64 via Box64; Master and Caves in one PufferPanel instance | [DST](templates/dst-arm64-box64-master-caves.json) |

**Development status:** Tested on one Ubuntu 22.04 ARM64 host with PufferPanel 3.0.9. Minecraft Java, Valheim (Steam networking), and DST Master + Caves have passed basic functional tests. Results are not a guarantee of compatibility on other hosts, with other game versions, or under prolonged load.

## Importing

Download and import an individual JSON file using PufferPanel's template-import feature. Repository-based template discovery may vary by PufferPanel version; this repository uses the `main` branch.

The templates are designed for PufferPanel's **host** environment. The machine must provide compatible native Java or Box64, any required x86_64 libraries, and a working installation method for the Steam dedicated-server binaries. `steamgamedl` does not guarantee x86 SteamCMD compatibility with an ARM64 host.

## Don't Starve Together

The DST template installs two shard configurations, then starts both Master and Caves as child processes of one PufferPanel server. On a Box64 0.4.4 test host, both shards initialized, connected, transferred a player from Master to Caves, serialized their worlds on a controlled PufferPanel stop, and reloaded their saved worlds on a later start. This confirms the observed basic lifecycle, not robustness under all shutdown scenarios. Independent shard controls are **not provided**. See [DST shard details](docs/DST-SHARDS.md) for test scope, remaining limitations, and whitelist behavior.

## Security and license

Only reusable templates and supporting technical documentation belong in this public repository. Never commit server tokens, credentials, private keys, world saves or private host configuration.

Adapted from [PufferPanel community templates](https://github.com/PufferPanel/templates/tree/v3), licensed under Apache-2.0. See [LICENSE](LICENSE), [LICENSE-NOTICE.md](LICENSE-NOTICE.md) and [upstream attribution](docs/UPSTREAM.md).
