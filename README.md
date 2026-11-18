# PufferPanel ARM64 game server templates

Unofficial community-maintained [PufferPanel](https://www.pufferpanel.com/) 3 templates for Linux ARM64/AArch64 hosts. They configure the host environment directly rather than Docker.

## Templates

| Game | Runtime | Template | Guide |
| --- | --- | --- | --- |
| Minecraft Java | Native ARM64 Java | [JSON](minecraft/minecraft-java-arm64.json) | [Minecraft](minecraft/README.md) |
| Valheim | Linux x86_64 server via Box64 | [JSON](valheim/valheim-arm64-box64.json) | [Valheim](valheim/README.md) |
| Don't Starve Together | Linux x86_64 via Box64; Master + Caves | [JSON](dontstarvetogether/dst-arm64-box64-master-caves.json) | [DST](dontstarvetogether/README.md) |

Each game has independent installation requirements, variable definitions and compatibility limits; read its guide before importing a template.

## Compatibility and validation

Basic functional tests were completed on **Ubuntu 22.04 ARM64** with **PufferPanel 3.0.9**. Valheim and DST used **Box64 0.4.4**.

- **Minecraft:** native ARM64 server operation tested.
- **Valheim:** Steam-network multiplayer and world save/reload tested; PlayFab/crossplay was not validated.
- **DST:** Master/Caves startup, shard connections, player transitions, controlled saving/shutdown and world reload tested. An expanded settings template also passed a fresh-install multiplayer lifecycle test.

These observations are not guarantees of crash recovery, unattended operation or compatibility with future game versions. Back up important worlds before changing a running server.

## Installation

1. Prepare a Linux ARM64 host with PufferPanel 3 and the dependencies listed in the game-specific guide.
2. Add `https://github.com/Gabrielson3/pufferpanel-arm64-templates.git` as a PufferPanel template repository using branch **`main`**, or import the desired JSON file.
3. Set all game-specific variables and credentials **in your private server instance**, then install and verify connectivity and save behavior.

On ARM64, the PufferPanel `steamgamedl` operation may require additional host-side compatibility setup for Linux x86_64 Steam server downloads. Editing a JSON file in GitHub does **not** restart or update an existing game server.

The JSON templates follow the official PufferPanel v3 layout: immediate game subdirectories, with a local README for each template. Previous `templates/` paths were relocated without changing template identifiers or JSON content.

## Documentation and maintenance

- [Owner-approved workflow](docs/WORKFLOW.md): `main`-only development; no automatic branches or GitHub Releases.
- [Current status](docs/STATUS.md), [decision history](docs/CONTINUITY.md), [upstream provenance](docs/UPSTREAM.md) and [agent instructions](AGENTS.md).

## License, authorship and security

Licensed under [Apache-2.0](LICENSE), with portions adapted from community templates; see [LICENSE-NOTICE](LICENSE-NOTICE.md) and [upstream attribution](docs/UPSTREAM.md). The project was substantially developed with ChatGPT (OpenAI) assistance under the owner's direction and real-world testing. It is not an OpenAI or PufferPanel product.

Do not commit access tokens, private keys, credentials, personal host configurations, raw private logs or saved worlds. AI-assisted code should be reviewed before use with valuable server data.
