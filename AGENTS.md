# Agent instructions — PufferPanel ARM64 templates

Before changing a template, read [the repository workflow](docs/WORKFLOW.md), [current status](docs/STATUS.md), [README](README.md), [decision history](docs/CONTINUITY.md) and [upstream attribution](docs/UPSTREAM.md). Then inspect the selected game's README, template JSON and scripts.

**Non-negotiable:** develop on `main` only. No new branches, pull requests, GitHub Releases or GitHub-hosted packaging without explicit owner approval. If an artifact is requested, deliver an actual verified local ChatGPT attachment. The detailed policy is in [WORKFLOW.md](docs/WORKFLOW.md).

Keep Minecraft native ARM64, Valheim with Box64, and Don't Starve Together Master/Caves assumptions separate. Preserve JSON template identifiers and existing game saves; source edits do **not** reconfigure or restart deployed servers. Avoid undocumented game internals, private credentials, server logs and world files. Validate host/version assumptions rather than claiming future compatibility. Log significant decisions in the affected game's documentation.

**Repository documentation, issues and new commit messages are in English.** This file applies only after the repository has been opened.
