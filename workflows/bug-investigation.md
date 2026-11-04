# Bug investigation workflow

1. Capture expected versus actual behavior, impact, environment, and first occurrence.
2. Reproduce with minimal inputs and record safe diagnostics.
3. Separate verified facts from hypotheses.
4. Trace the code path, data state, external dependencies, and recent changes.
5. Test one hypothesis at a time with a discriminating experiment.
6. Identify the root cause and assess blast radius.
7. Implement the narrowest safe fix and a regression test, if authorized.
8. Run relevant tests and inspect the final diff.
9. Report root cause, evidence, fix, verification, limitations, and follow-up actions.

Do not suppress exceptions, disable protections, delete data, or alter production state without approval.
