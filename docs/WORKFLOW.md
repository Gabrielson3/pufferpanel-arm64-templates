# Repository workflow — owner decisions (2026-11-18)

**Normative. Read this before making changes.** This file overrides older, conflicting suggestions in historic issues, commit notes, READMEs or prior chats. The code and current GitHub state still determine what is actually implemented. Record exceptions only when the owner explicitly decides them.

## Repository language

Write repository documentation, READMEs, new issues and commit messages **in English**. Preserve exact source identifiers, API names, commands, upstream quotations and game-provided strings when translation would change their meaning. The separate Gamer Poker repository is the owner's **Portuguese-language exception**; do not copy its locale to this project.

## Git model — MAIN ONLY

- **`main` is the only authorized development branch.** Work and commit directly on `main`; use small, reversible, appropriately scoped commits even when the owner wants a large functional development batch.
- **Never create a branch**, including `dev/*`, `feature/*`, `fix/*`, `review/*`, `release/*`, temporary packaging branches or branches proposed as a "safe" workaround. **Do not use a pull request or merge workflow that requires another branch.** This restriction applies to all projects in this repository, even in a fresh conversation without previous chat history.
- Git commits, approved stable tags where appropriate and external backups provide rollback. **Do not use GitHub Release/tag creation as a substitute for the required in-chat file delivery.** Approval of a release candidate is not approval to publish a GitHub Release.
- If an operation truly requires a second branch, stop and explain why instead of creating it by default; seek the owner's explicit, operation-specific permission first. An existing extra branch is not implicit permission to create more.
- Before editing, check the actual `main` HEAD, current version, unmerged references and last **owner-validated** version separately. Do not confuse a test ZIP, a repository commit, a CI green check and in-client acceptance.

## Delivery — ChatGPT artifacts, not GitHub Releases

- GitHub is the **source-code workspace**: implementation, history, issues, testing code and documentation. **Do not create GitHub Releases or upload new build ZIPs/binaries into Git branches** as the default distribution method.
- When the owner asks for an installable build or declares a version ready for review, **generate the actual artifact in ChatGPT's available local file environment** (e.g., `/mnt/data/`), verify the precise file exists and link it **directly in the conversation as an attachment** (`sandbox:/mnt/data/<verified-file>`). A GitHub repository/source link, release asset, `dist/` blob, shell script or a command for the user to assemble the package **does not satisfy that deliverable**.
- **Separate artifact creation from acceptance.** A requested development/review package may be assembled and attached **before** all automated, simulator, host or owner tests have run. It must be labeled **UNVALIDATED DEVELOPMENT REVIEW** whenever relevant checks are unavailable or incomplete; name the missing checks and the last owner-approved fallback. Missing test tools are not, by themselves, a packaging veto. Never imply the package is stable, runtime-tested, deployed or approved.
- **Archive safeguards remain mandatory:** use the complete, current, authenticated project sources; include only the intended installable files with correct paths; check manifest/dependencies/source completeness, archive integrity, file bytes or hashes and extraction layout. Never reconstruct missing modules, substitute historical code or claim an attachment that does not exist. A demonstrated compilation failure or known material defect must be corrected before offering a normal installable review package; a deliberately broken diagnostic artifact must be explicitly identified as non-installable.
- **Runtime and promotion remain separate gates:** execute applicable tests where tools and fixtures are available, report actual results versus skipped checks, and do not skip known failures silently. Production deployment or stable approval still requires the project's own verification/owner decision. **Archive integrity alone does not prove runtime compatibility.**
- If the private GitHub connector cannot place source bytes into the available local file environment, **state the blocker truthfully** and request an accessible source copy or a supported local-workspace workflow. **Do not silently substitute a GitHub-hosted ZIP or claim a ChatGPT attachment was created**.
- Do not publish versions, tags, binaries, releases or deploy services without the owner's explicit instructions. **No repeated micro-deliveries**: implement and self-check substantial planned batches, then provide one consolidated review build and a short relevant checklist, unless explicitly asked otherwise.

## New-conversation handoff and verification

1. Identify the exact repository and project/addon/template in scope; inspect `main`, `AGENTS.md`, this file, `README.md`, `docs/CONTINUITY.md`, relevant project docs and current issues **before planning implementation**.
2. Determine which choices are owner-decided versus only suggested, committed, simulator-tested, runtime-tested, deployed, or superseded. New explicit owner decisions override conflicting historical text; document the supersession.
3. Keep each project's existing code, requirements, dependencies, data, licensing, runtime state and rollback separate. Do not infer one project's acceptance from another.
4. Preserve user accounts, game save data, SavedVariables, production databases, secrets and previously approved behavior. Never commit them or private audio/video recordings.
5. Perform source review, reproducible tests and high-information checks before modifying working behavior. Report missing tests instead of claiming success. Do not run paid/quota-limited CI without explicit approval when the owner has exhausted or restricted it.
6. Update the project's `docs/CONTINUITY.md` or the appropriate scoped decision/issue record with new decisions and evidence, without rewriting historical results.

## Conflict rule

When historic documentation instructs agents to create branches, open PRs, publish GitHub Releases or rely on Github-hosted ZIP downloads as the normal deliverable, **treat that as superseded by this owner-approved workflow**. Keep a note of any existing operational dependency before changing code. Project-specific safety exceptions below do **not** grant blanket permission to publish or branch.

## PufferPanel templates specifics

- The deliverable is normally the **changed JSON template source** under its existing game directory and an explanation; this is not a WoW/ESO installable addon. If the user requests a package, attach a locally created ZIP of the intended JSON files in ChatGPT.
- The single `main` branch is the template source consumed by PufferPanel. Changing JSON files does **not** update or restart the user's active servers; make no such claims.
- Keep Minecraft Java native ARM64, Valheim Box64, and Don't Starve Together Master/Caves assumptions separate. Protect worlds, passwords, tokens, servers and template identifiers; no undocumented game metadata injection.
