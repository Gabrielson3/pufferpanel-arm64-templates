# PufferPanel ARM64 templates

Experimental community-style [PufferPanel](https://www.pufferpanel.com/) 3 templates for Linux ARM64 / AArch64 servers.

| Game | Runtime | Template |
| --- | --- | --- |
| Minecraft Java | Native ARM64 Java | [Minecraft](templates/minecraft-java-arm64.json) |
| Valheim | Linux x86_64 via Box64 | [Valheim](templates/valheim-arm64-box64.json) |
| Don't Starve Together | Linux x86_64 via Box64; Master and Caves in one PufferPanel instance | [DST](templates/dst-arm64-box64-master-caves.json) |

**Development status:** These templates are experimental and have not passed fresh-install and lifecycle tests on every supported host. Use only disposable test worlds until installation, connectivity, saves, and shutdown have been verified.

## Importing

Download and import an individual JSON file using PufferPanel's template-import feature. Repository-based template discovery may vary by PufferPanel version; this repository uses the `main` branch.

The templates are designed for PufferPanel's **host** environment. The machine must provide compatible native Java or Box64, any required x86_64 libraries, and a working installation method for the Steam dedicated-server binaries. `steamgamedl` does not guarantee x86 SteamCMD compatibility with an ARM64 host.

## Don't Starve Together

The experimental DST template installs two shard configurations, then starts both Master and Caves as child processes of one PufferPanel server. Review [DST shard details](docs/DST-SHARDS.md) before testing. Independent shard controls and reliable graceful shutdown are **not yet provided**.

## Security and license

Only reusable templates and supporting technical documentation belong in this public repository. Never commit server tokens, credentials, private keys, world saves or private host configuration.

Adapted from [PufferPanel community templates](https://github.com/PufferPanel/templates/tree/v3), licensed under Apache-2.0. See [LICENSE](LICENSE), [LICENSE-NOTICE.md](LICENSE-NOTICE.md) and [upstream attribution](docs/UPSTREAM.md).
