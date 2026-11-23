# Hytale (ARM64)

[Template JSON](hytale-arm64.json) · [Repository overview](../README.md)

Dedicated Hytale server running in native ARM64 **Java 25** on PufferPanel 3. The official Linux x86-64 Hytale downloader runs through Box64; Box64 is not used to execute the game server.

## Requirements

Linux ARM64, PufferPanel 3, Box64, Bash and Python 3. Java 25 is installed through PufferPanel. At least 4 GB of memory is recommended for the server, with additional RAM available outside the Java heap. Open UDP port **5520** (or the configured port) in the VM and cloud network.

## Installation

Import [the template](hytale-arm64.json) or select it from this GitHub repository. Configure the server name, MOTD, optional password, player limit, view radius, Java memory and port. Run **Install**.

The installer fetches the [official Hytale Downloader](https://support.hytale.com/hc/en-us/articles/45326769420827-Hytale-Server-Manual) and the game files. **Follow the device-code sign-in URL in the PufferPanel installation console** when prompted. An authorized Hytale account is required.

Start the server, then enter `/auth login device` in the PufferPanel console and complete the separate **server** authorization. The official `start.sh` is retained to handle Hytale's staged updates and regular backups. Panel-managed fields are applied to `Server/config.json` on startup; other settings, worlds and account data are preserved.

The JSON includes the install and launch helpers, so additional script downloads are not necessary.

## Compatibility

Hytale's [server manual](https://support.hytale.com/hc/en-us/articles/45326769420827-Hytale-Server-Manual) lists ARM64 as supported, but bundled native libraries can differ between game releases. Verify the version you deploy before relying on important world saves.

Hytale is a game by Hypixel Studios. This is an unofficial template, not affiliated with Hypixel Studios or PufferPanel. See the [project credits](../README.md).
