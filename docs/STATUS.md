# Current state — PufferPanel ARM64 templates

**Reviewed:** 2026-11-18. **Development branch:** `main` only. **Delivery:** normally the versioned JSON template source, never a GitHub Release or an addon-style ZIP unless a file package is specifically requested.

| Template | Source/runtime | Evidence stated in repository |
| --- | --- | --- |
| Minecraft Java | native ARM64 Java | Host functional testing recorded |
| Valheim | Box64 for x86_64 dedicated server | Steam-network multiplayer, save/reload tested; crossplay not established |
| Don't Starve Together | Box64, Master + Caves | Both shards, transfer, save/shutdown/restart tested |

Real host evidence in the [README](../README.md) references Ubuntu 22.04, PufferPanel 3.0.9 and Box64 0.4.4. No promise of future game version compatibility follows from those tests. The live VM is **not automatically updated** by editing GitHub source.

**Handoff:** read [WORKFLOW](WORKFLOW.md), [continuity](CONTINUITY.md), the specific `<game>/README.md` and JSON, plus [upstream attribution](UPSTREAM.md). Preserve template IDs, server worlds and secrets. Do not introduce undocumented game metadata workarounds. No extra branches remain.
