# PufferPanel ARM64 game server templates

Unofficial, community-maintained [PufferPanel](https://www.pufferpanel.com/) 3 templates for Linux ARM64/AArch64 hosts.

| Game | Runtime | Template | Documentation |
| --- | --- | --- | --- |
| Minecraft Java | Native ARM64 Java | [JSON](minecraft/minecraft-java-arm64.json) | [Minecraft README](minecraft/README.md) |
| Valheim | Linux x86_64 via Box64 | [JSON](valheim/valheim-arm64-box64.json) | [Valheim README](valheim/README.md) |
| Don't Starve Together | Linux x86_64 via Box64, Master + Caves | [JSON](dontstarvetogether/dst-arm64-box64-master-caves.json) | [DST README](dontstarvetogether/README.md) |

## Compatibility and testing

All three templates passed basic functional tests on an Ubuntu 22.04 ARM64 host with **PufferPanel 3.0.9**. Valheim and Don't Starve Together were tested with **Box64 0.4.4**.

- **Minecraft Java:** native ARM64 server operation was tested.
- **Valheim:** Steam-network multiplayer, world saving and reloading were tested; PlayFab/crossplay was not validated.
- **Don't Starve Together:** Master/Caves startup, communication, player transfer, controlled save/shutdown and subsequent world reload were tested. Its expanded server-settings template also passed a fresh-install, multiplayer connection, cave transition and controlled shutdown test.

These are limited real-world tests, not a guarantee of prolonged stability, support on other hosts, crash safety or compatibility with future updates. Read each game's README and back up worlds before making changes.

## Installation

1. Prepare a Linux ARM64 machine with PufferPanel 3. The templates target the **host environment**, not Docker.
2. Read the relevant game's README for Box64, Java, Steam download, network and game-specific requirements.
3. Add `https://github.com/Gabrielson3/pufferpanel-arm64-templates.git` as a PufferPanel template repository on branch `main`, or download and import the desired JSON file.
4. Create a server from the template, set game variables and credentials privately, install, launch and test saves and connectivity.

**Important:** On ARM64, PufferPanel's `steamgamedl` operation may need additional host-side compatibility setup to download Linux x86_64 Steam dedicated-server files.

The files are grouped by game, following the [official PufferPanel template repository's](https://github.com/PufferPanel/templates/tree/v3) directory convention. PufferPanel 3 reads JSON templates from immediate subfolders and displays the `README.md` in each template folder. The former `templates/` JSON paths were relocated; **template identifiers and JSON contents were not changed by this reorganization**. Existing instances are unaffected by these file-location changes.

## Authorship and AI assistance

This repository was developed with **substantial assistance from [ChatGPT](https://chatgpt.com/) (OpenAI)**. ChatGPT produced and revised much of the template code, shell/Python helper scripts and documentation, and helped analyze server logs and troubleshoot compatibility issues.

The repository owner defined the project's goals, supplied and configured the ARM64 test environment, performed the in-game validation, identified issues and directed revisions. The owner maintains the repository and is responsible for its contents. AI-assisted code can contain mistakes and should be independently reviewed, particularly before use with valuable worlds.

**This project is not an OpenAI product and is not affiliated with, endorsed by, or maintained by OpenAI or PufferPanel.**

## License, upstream attribution and security

Distributed under [Apache-2.0](LICENSE). Portions of the JSON templates are adapted from the [PufferPanel community templates](https://github.com/PufferPanel/templates/tree/v3). See [upstream attribution](docs/UPSTREAM.md) and [license notice](LICENSE-NOTICE.md).

Never commit server tokens, passwords, private keys, user identities, raw server logs, private host configurations or game saves. Supply secrets in your private PufferPanel instance.
