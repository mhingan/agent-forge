# Publishing AgentForge to PyPI locally

The distribution name is agentforge-toolkit and the installed command is agentforge. Releases are uploaded locally by the maintainer using a project-scoped PyPI API token. GitHub Actions do not publish the package.

## Verify the repository

Start from a clean checkout and run:

    python -m pip install --upgrade build twine
    python scripts/format_json.py --check
    python scripts/sync_package_data.py --check
    python -m agentforge validate --strict
    python -m unittest discover -s tests -v

## Build and check distributions

    rm -rf dist build
    python -m build
    python -m twine check dist/*

Check that pyproject.toml and src/agentforge/__init__.py contain the same version before building.

## Upload locally

Create a PyPI API token for the agentforge-toolkit project, then run:

    python -m twine upload dist/*

When prompted, use __token__ as the username and paste the API token as the password. Twine hides password input. Do not put the token in source files, shell scripts, GitHub files, or committed environment files.

## Versioning

PyPI releases are immutable. Increase the version in both pyproject.toml and src/agentforge/__init__.py for each release, update CHANGELOG.md, rebuild, and upload the new distributions. Never reuse an already-uploaded version.

Install the package with:

    python -m pip install --upgrade agentforge-toolkit
