# Refactor safely

Identify the code smell and desired invariant. Inspect callers and tests. Propose a minimal sequence that preserves behavior, add characterization/regression tests where needed, and refactor in small steps. Avoid unrelated cleanup or API changes. Run targeted tests and compare the diff for accidental behavior changes.
