# Agent instructions — PufferPanel ARM64 templates

When operating inside this repository, **first read** [README.md](README.md), [docs/CONTINUITY.md](docs/CONTINUITY.md), and [docs/UPSTREAM.md](docs/UPSTREAM.md). Then inspect the appropriate **game-specific README and JSON template**.

- Treat **Minecraft Java ARM64**, **Valheim Box64**, and **Don't Starve Together Box64 Master/Caves** as **separate templates with separate assumptions**, not interchangeable server configurations.
- Record important decisions and their rationale, version compatibility, known limits, game/host tests, rollback strategy and unresolved questions in the **specific game's README** or issue, per `docs/CONTINUITY.md`.
- Preserve existing template identifiers, options and license notices unless a migration is justified. Avoid risky undocumented game-file manipulation and never imply a future game update is guaranteed compatible.
- Editing this repository **does not update, restart or reconfigure** the owner's running servers. Protect game worlds, secrets and private host settings; do not commit them.
- Do not import practices or context from Gamer Poker, the ESO workshop or WoW workshop without an explicit reason.

This file is only followed by tools/agents that **load this repository**; it cannot ensure that a new conversation searches for it.
