# Upstream attribution

The original templates are maintained in [PufferPanel/templates](https://github.com/PufferPanel/templates/tree/v3), licensed under the Apache License, Version 2.0.

Reference implementations:

- [Minecraft Java](https://github.com/PufferPanel/templates/blob/v3/minecraft/minecraft.json)
- [Valheim](https://github.com/PufferPanel/templates/blob/v3/valheim/valheim.json)
- [Don't Starve Together](https://github.com/PufferPanel/templates/blob/v3/dontstarvetogether/dontstarvetogether.json)

Modifications:

- Minecraft: ARM64 host-only mode, native Java, reduced Vanilla/Fabric/Paper selection.
- Valheim: Box64 execution, ARM64 host requirements, editable world preset and resource modifiers.
- Don't Starve Together: Box64 execution, Master/Caves shard configuration, a localhost-only synchronization endpoint, an underground world-generation preset, and an experimental two-process supervisor.

The JSON templates now reside in their game-specific folders (`minecraft/`, `valheim/` and `dontstarvetogether/`). They retain their original template type identifiers. These independently maintained community modifications are not official PufferPanel templates. See the root [README](../README.md#authorship-and-ai-assistance) for disclosure of substantial development assistance from ChatGPT (OpenAI).
