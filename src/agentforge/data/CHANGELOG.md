# Changelog

## 1.1.0 - 2026-11-04

### Added
- Expanded the library to 18 production-oriented skills with 26+ task-focused reference templates and checklists.
- Expanded the specialist roster to 15 roles with recommended-skill relationships and clear delegation boundaries.
- Added mobile, accessibility, product specification, data engineering, and observability coverage.
- Added product discovery, incident response, data pipeline, and accessibility workflows.
- Added planning, security review, and release-check command recipes.
- Added JSON Schemas for skills, agents, and target configuration.
- Added strict validation for pretty-printed JSON, duplicate keys, catalog cross-references, adapter target paths, and broken local skill links.

### Changed
- Rebuilt skill, agent, and adapter catalogs with consistent two-space pretty printing and UTF-8 output.
- Made skill guidance more actionable with activation criteria, procedures, decision points, deliverables, quality gates, anti-patterns, and completion standards.
- Added progressive-disclosure reference resources so detailed templates are available when needed without inflating every skill prompt.
- Hardened installation and uninstall behavior: `--force` preserves locally modified content, unmanaged files remain untouched, and manifest-driven removal is restricted to known AgentForge paths.
- Improved Antigravity rule triggers and glob metadata.

### Security
- Validate manifest structure and reject duplicate JSON keys or invalid JSON constants.
- Reject manifest paths that escape the selected project/global root.

## 1.0.0 - 2026-11-04

## 1.0.0 - 2026-11-04

- Initial universal toolkit with 13 portable skills and 10 specialist-agent profiles.
- Added adapters for Claude Code, OpenAI Codex, GitHub Copilot, Gemini CLI, and Google Antigravity.
- Added Python CLI for validation, generation, installation, uninstallation, and environment diagnostics.
- Added engineering rules, repeatable workflows, prompt recipes, tests, and CI.
