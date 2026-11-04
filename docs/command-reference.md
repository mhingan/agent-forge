# AgentForge CLI reference

The CLI requires Python 3.10 or newer. From a source checkout, run `python -m agentforge`; after installation, use `agentforge`.

## Global options

```bash
python -m agentforge --version
python -m agentforge --help
```

## `list`

List catalog entries or supported targets.

```bash
agentforge list
agentforge list skills
agentforge list agents
agentforge list targets
```

## `validate`

Validate skill directories, frontmatter, agent profiles, catalogs, JSON formatting, target registry consistency, and required files.

```bash
agentforge validate
agentforge validate --strict
```

Strict mode also checks skill-file length and relative links. Validation never executes scripts included in skills.

## `install`

```bash
agentforge install --agent all --scope project
agentforge install --agent claude,codex --scope global
agentforge install --agent copilot --skill frontend-engineering --skill accessibility-ux
agentforge install --agent all --components skills,agents,rules,workflows --dry-run
agentforge install --agent all --force
```

Options:
- `--agent`: comma-separated IDs or `all`.
- `--scope`: `project` (default) or `global`.
- `--destination`: alternate project root; valid only for project scope in practical use.
- `--skill`: repeatable skill selector; when omitted, all skills are selected if the skills component is enabled.
- `--components`: comma-separated subset of `skills`, `agents`, `rules`, `workflows`.
- `--dry-run`: preview operations without writing files.
- `--force`: refresh unchanged AgentForge-managed artifacts. Local modifications and unmanaged paths are preserved.

If a destination already exists but is not present in the manifest, AgentForge treats it as user-owned and skips it. This applies even when `--force` is used.

## `uninstall`

```bash
agentforge uninstall --agent claude --scope project --dry-run
agentforge uninstall --agent claude --scope project
agentforge uninstall --agent all --scope project --skill code-review
```

Options:
- `--agent`: target IDs or `all`.
- `--scope`: project or global.
- `--destination`: project root.
- `--skill`: remove only the selected skills; other component records are retained.
- `--dry-run`: preview removals.

Uninstall removes only unchanged managed paths in known AgentForge locations. It retains modified paths and paths still referenced by another target.

## `generate`

```bash
agentforge generate --agent all --scope project
agentforge generate --agent codex,gemini --scope global
```

Generates native specialist profiles and rule/context files; it does not install skills or workflows. Project context files are not written globally.

## `doctor`

```bash
agentforge doctor
```

Displays Python support, candidate paths, and whether common agent executables are found on `PATH`. Detection is informational; it does not validate provider authentication or feature availability.

## Repository maintenance scripts

```bash
# Format all JSON files
python scripts/format_json.py

# Check formatting without modifying files
python scripts/format_json.py --check

# Rebuild embedded package data
python scripts/sync_package_data.py

# Verify package data is synchronized
python scripts/sync_package_data.py --check

# Validate repository and tests
python -m agentforge validate --strict
python -m unittest discover -s tests -v
```
