# Project continuity and decision record

> **2026-11-18 — packaging and acceptance rule clarification:** Creating an authenticated, source-complete, integrity-verified **development review** artifact is allowed before unavailable runtime/simulator/owner tests run, provided it is labeled **UNVALIDATED** and its skipped checks are listed. A known compilation/test failure is not a normal installable review build. Stable promotion and production deployment remain independent approvals. Direct ChatGPT file delivery, `main`-only commits, no new Releases/branches and no unapproved Actions use are unchanged. Where local source transfer is impossible, report that separate technical limitation rather than attributing it to packaging policy. The full normative wording is in [WORKFLOW.md](WORKFLOW.md).

> **Current policy (2026-11-18):** [WORKFLOW.md](WORKFLOW.md) is authoritative; [STATUS.md](STATUS.md) records the latest verified state. Older instructions about development branches, releases or delivery methods are historical and **superseded**.

**Purpose:** leave a small, durable explanation of important decisions for future ChatGPT sessions and maintainers. Read [README](../README.md), the **specific game template README**, the relevant JSON and [upstream attribution](UPSTREAM.md) before changing anything.

## Separate templates

- [Minecraft Java ARM64](../minecraft/README.md) uses **native ARM64 Java**.
- [Valheim ARM64](../valheim/README.md) uses **Box64** for the x86_64 dedicated server.
- [Don't Starve Together ARM64](../dontstarvetogether/README.md) uses **Box64** and **Master/Caves** shard coordination.

Each template has independent runtime choices, version constraints, variables, installation and test evidence. Do not copy environment variables, network/port assumptions, seed/world handling, backup procedures or launch steps from one game into another unless independently checked. Never confuse this repository's templates with the player's **running** servers on their VM. Do not apply assumptions from Gamer Poker or ESO/WoW addons.

## Record decisions where they belong

For a significant template change, update the **specific game README**, plus issue or this repository's documents as appropriate:

> **Date / game / template revision / status** (idea, decided, implemented, host-tested, superseded).  
> **Decision and rationale:** requirement, attempted alternatives, risk and update compatibility.  
> **Test evidence:** exact host architecture, Ubuntu/PufferPanel/Box64/game versions when known, install/start/network/save/reload checks actually performed.  
> **Safety and rollback:** saved worlds, shard config, ports, user secrets, expected behavior on updates.  
> **Follow-up:** what remains untested, with linked issue.

Do not assert a template is stable across future game updates because it passed a previous test; explicitly distinguish unverified scenarios (for example crossplay or crash recovery). Preserve template identifiers unless a migration has been designed. Never introduce a speculative method that depends on undocumented game internals without explicit review.

## New-chat handoff

Identify the **game** and template file; read README, game README, open issues and current JSON; inspect changed code and real host logs only when supplied. Keep a reversible change history and document any newly accepted behavior before finishing. No automatic modification or restart of an active VM is implied by editing GitHub files. Do not commit world saves, IP-specific private config, tokens, credentials or personal server logs.
