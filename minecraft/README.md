# Minecraft Java — native ARM64

[Template JSON](minecraft-java-arm64.json) · [Repository overview](../README.md)

Runs a Minecraft Java dedicated server using a native ARM64 Java runtime on PufferPanel's **host** environment. It does not require Box64.

## Requirements

- Linux ARM64/AArch64 host running PufferPanel 3.
- ARM64 Java compatible with the intended Minecraft version. The template uses PufferPanel's `javadl` operator and defaults to Java `25`; use the version appropriate for your chosen game release.
- Sufficient CPU, RAM and disk space, plus inbound network access on the Minecraft server port (default **25565/TCP**).

## Setup and controls

Import [the template](minecraft-java-arm64.json), create an instance and configure:

- **Minecraft version:** prefer a fixed game version for repeatable installs. `latest` may not work with every server software release.
- **Launcher:** Vanilla, Fabric or Paper. Forge/NeoForge are not supported by this template.
- **Java version and heap memory:** match the game version and allocated resources. The default maximum heap is **2048 MB**.
- **EULA:** the administrator must explicitly accept the [Minecraft EULA](https://www.minecraft.net/en-us/eula). Default: not accepted.
- **Port and MOTD:** configure the public listening port and server-list message.

The template creates `server.properties` only if missing, so custom settings there are preserved on subsequent installations. It also writes `eula.txt` according to the EULA field.

## Tested scope and cautions

Native Java operation was tested on the project's ARM64 host. Not every Minecraft version, launcher build, mod or plugin combination has been tested. Keep backups before upgrading a world or changing its server software.

This is not an official PufferPanel template. For an explanation of the ChatGPT contribution, see [authorship and AI assistance](../README.md#authorship-and-ai-assistance).
