# Troubleshooting

## Python version

AgentForge requires Python 3.10 or newer.

```bash
python --version
python -m agentforge --version
```

On systems where `python` points to an older runtime, use `python3`.

## Module or command not found

From a source checkout, run commands at the repository root:

```bash
python -m agentforge --help
```

If installed as a package:

```bash
python -m pip show agentforge-toolkit
agentforge --help
```

If the console command is not on PATH, use `python -m agentforge` from an accessible source checkout or fix the active virtual environment.

## Validation reports JSON formatting

Run:

```bash
python scripts/format_json.py
python scripts/format_json.py --check
python -m agentforge validate --strict
```

The formatter preserves Unicode and emits two-space indentation with one trailing newline. It rejects duplicate keys, non-standard constants, and invalid JSON instead of silently rewriting malformed data.

## Package data is out of sync

The root folders are canonical. Do not edit `src/agentforge/data/` manually.

```bash
python scripts/sync_package_data.py
python scripts/sync_package_data.py --check
```

After a successful sync, commit the generated package mirror alongside the canonical changes.

## Existing files are skipped

AgentForge deliberately skips an existing path that is not recorded in its manifest. Inspect the destination and merge content manually. Do not delete user-owned files to make installation proceed.

## A modified installation is kept

If a tracked file's hash no longer matches the installation manifest, AgentForge preserves the local modification, even with `--force`. Compare the local version with the current canonical source and merge manually. Reinstall only after deciding which changes should remain.

## Uninstall keeps a shared path

Some targets share one Agent Skills directory. A shared path remains while another selected target still references it. Uninstall the remaining target(s) if you intend to remove the shared file.

## Uninstall rejects a manifest path

AgentForge only removes paths inside known managed directories under the selected project/global root. Inspect the manifest and any symlinks. It will not delete an arbitrary file named in a manifest.

## A provider does not discover generated files

A successful generation step proves only that AgentForge wrote a file. It does not prove the provider version or surface discovers that path/format. Check:
1. The correct product surface and version.
2. The documented project/global directory.
3. Required frontmatter or schema.
4. Provider-side feature flags, plan, preview status, and settings.
5. Whether the target supports the generated field/tool names.

See [compatibility](compatibility.md). Report provider discovery as unverified unless it was tested in that provider.

## Tests fail on a provider-specific format

Run focused tests first:

```bash
python -m unittest tests.test_agentforge.AdapterTests -v
python -m unittest discover -s tests -v
```

Check that the target adapter and its compatibility registry are both updated. Never weaken a test simply to accept invalid provider output; verify the official schema/format first.

## CI failure

Inspect the failed job and exact command output. Common gates:
- `format_json.py --check`: unformatted or invalid JSON.
- `sync_package_data.py --check`: root assets differ from the embedded package mirror.
- `agentforge validate --strict`: invalid frontmatter, broken references, duplicate catalog entries, or inconsistent adapters.
- Unit tests: renderer, install/uninstall safety, or regression behavior.

Fix the source issue, run the same command locally, then push. Do not claim the pipeline passed until the latest commit has a successful run.
