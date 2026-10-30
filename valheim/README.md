# Valheim — ARM64 via Box64

[Template JSON](valheim-arm64-box64.json) · [Launcher source](scripts/start-valheim.sh) · [Repository overview](../README.md)

Runs the **Linux x86_64 Valheim dedicated server** on a Linux ARM64 machine via [Box64](https://github.com/ptitSeb/box64). This is a PufferPanel **host** template, not a Docker image.

## Requirements

- Linux ARM64 host with PufferPanel 3 and working Box64 (tested with **0.4.4**).
- Compatible libraries for the x86_64 Valheim binary and Box64 runtime.
- A host-side Steam game download method compatible with ARM64. The template uses PufferPanel's `steamgamedl` operation with app **896660**, which may require extra setup on ARM64.
- Reachable UDP game port(s) and matching host/cloud firewall configuration; the default configured game port is **2456**.

## Setup and controls

Import [the template](valheim-arm64-box64.json) and configure the server name, world name, password (**at least five characters**), UDP port, public-listing setting, world preset and resource modifier.

The template uses `run.pre` to write its launcher to the **private game-instance directory** every time it starts; the maintained source is [start-valheim.sh](scripts/start-valheim.sh). The launcher passes values as environment variables rather than splicing passwords or names into a shell command.

Keep world backups and store passwords only in PufferPanel, never in GitHub.

## Tested scope and limitations

Steam networking, player connection, world saving and loading were tested on Ubuntu 22.04 ARM64, PufferPanel 3.0.9 and Box64 0.4.4.

**PlayFab/crossplay was not validated**. Missing PlayFab-related libraries were observed in earlier test logs, so do not assume crossplay functionality. Long-term stability and future game versions also need independent testing.

This is not an official PufferPanel template. See [authorship and AI assistance](../README.md#authorship-and-ai-assistance).
