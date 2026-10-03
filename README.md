# TranslationParity

TranslationParity is a GenLayer Intelligent Contract for checking semantic parity between two language versions of a public policy document. An owner registers an original URL, a translated URL, language codes, and an immutable pair ID. Validators independently fetch both documents and return a structured consensus receipt covering parity, missing concepts, material differences, and confidence. Whitespace and formatting are not treated as semantic changes; obligations, exceptions, dates, thresholds, and actors are.

Lifecycle: `OPEN` -> `REVIEWED`. The receipt preserves both SHA-256 source digests, source hosts, findings, and the exact structured decision. Duplicate IDs, same-host pairs, same-language pairs, malformed URLs, unavailable documents, and validator disagreement fail closed.

Studionet contract: `0xB664604Afa282B71eC8036a756DC688aC97fBcA6`
Deployment transaction: `0xa2c7c974aeadb7aaf466b7fc6d7675beacc244cd389b3732ca15630cb2ec0eae`
Source SHA-256: `439423af473f46fe930e16e0879a3a0b33a8f76d418e170ad96e54e568c4ea03`

Tests: `python -m pytest test_translation_parity.py -q`
Lint: `PYTHONUTF8=1 genvm-lint translation_parity.py`
