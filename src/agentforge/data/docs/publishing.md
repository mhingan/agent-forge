# Publishing AgentForge to PyPI

AgentForge is built with the standard Python packaging workflow. The distribution name is
`agentforge-toolkit`; the installed command is `agentforge`.

## One-time PyPI Trusted Publisher setup

Configure this once in the PyPI project settings. If the project has not been created yet,
create it with an initial manual upload first, then configure its publisher.

1. Open the project settings on PyPI: https://pypi.org/manage/project/agentforge-toolkit/settings/publishing/
2. Add a pending publisher with:
   - Owner: `mhingan`
   - Repository: `agent-forge`
   - Workflow filename: `publish-pypi.yml`
   - Environment name: `pypi`
3. Save the publisher configuration.

The workflow uses GitHub's OIDC identity token. No PyPI API token or GitHub secret is needed.

## First publication

If `agentforge-toolkit` does not exist on PyPI yet, Trusted Publishing cannot create the
project on its own. Make the first upload manually from a clean checkout:

```bash
git clone https://github.com/mhingan/agent-forge.git
cd agent-forge
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade build twine
python -m build
python -m twine check dist/*
python -m twine upload dist/*
```

Authenticate with username `__token__` and a PyPI API token as the password. Do not commit
the token or put it in the repository.

If the project already exists on PyPI, skip the manual upload and configure the Trusted
Publisher directly.

## Subsequent releases

1. Update the version in both `pyproject.toml` and `src/agentforge/__init__.py`.
2. Update `CHANGELOG.md`.
3. Commit and push the changes.
4. Create and publish a GitHub Release whose tag matches the package version, for example
   `v1.1.1`.
5. The `Publish AgentForge to PyPI` workflow runs validation, tests, builds the wheel and
   source distribution, checks the distributions, and publishes them to PyPI.

PyPI releases are immutable: never reuse a version that has already been uploaded. Bump the
version for every release.

## Local verification

```bash
python -m pip install --upgrade build twine
python scripts/format_json.py --check
python scripts/sync_package_data.py --check
python -m agentforge validate --strict
python -m unittest discover -s tests -v
python -m build
python -m twine check dist/*
```

Install the published package with:

```bash
python -m pip install agentforge-toolkit
```
