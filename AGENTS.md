# Agent instructions — PufferPanel ARM64 templates

> **First action in every new task:** read [docs/WORKFLOW.md](docs/WORKFLOW.md) and obey its owner-approved operating rules **before** planning, coding, versioning or packaging. **Work on `main` only: never create a new branch, PR, temporary release/review branch or GitHub Release without explicit case-specific approval.** For installable deliverables, create a verified local ChatGPT attachment rather than linking a ZIP stored in GitHub. Use substantial internal development batches instead of repeated owner checkups. These requirements override conflicting older workflow guidance.

## Non-negotiable owner workflow

- **Git:** `main` only; individual commits for rollback. Do not create development, review, temporary or release branches.
- **Distribution:** GitHub stores source/issues/docs; installable files are generated and linked **as actual ChatGPT attachments**, not GitHub Releases or ZIPs committed to `dist/`.
- **Verification:** never claim a build was run or accepted if only static checks/archive integrity were verified. If no local source file transfer is possible, disclose the blocker rather than substituting GitHub delivery.
- **Handoff:** re-read `docs/WORKFLOW.md`, `docs/CONTINUITY.md`, project docs and actual `main` state even when coming from a long conversation summary. Honor the project's security, data and deployment constraints.

When operating inside this repository, **first read** [README.md](README.md), [docs/CONTINUITY.md](docs/CONTINUITY.md), and [docs/UPSTREAM.md](docs/UPSTREAM.md). Then inspect the appropriate **game-specific README and JSON template**.

- Treat **Minecraft Java ARM64**, **Valheim Box64**, and **Don't Starve Together Box64 Master/Caves** as **separate templates with separate assumptions**, not interchangeable server configurations.
- Record important decisions and their rationale, version compatibility, known limits, game/host tests, rollback strategy and unresolved questions in the **specific game's README** or issue, per `docs/CONTINUITY.md`.
- Preserve existing template identifiers, options and license notices unless a migration is justified. Avoid risky undocumented game-file manipulation and never imply a future game update is guaranteed compatible.
- Editing this repository **does not update, restart or reconfigure** the owner's running servers. Protect game worlds, secrets and private host settings; do not commit them.
- Do not import practices or context from Gamer Poker, the ESO workshop or WoW workshop without an explicit reason.

This file is only followed by tools/agents that **load this repository**; it cannot ensure that a new conversation searches for it.
