# TranslationParity

TranslationParity compares a canonical public document, its translation, and a terminology glossary. GenLayer validators independently fetch all three sources and classify the translation as FAITHFUL, DRIFTED, or INCOMPLETE with issue codes and SHA-256 evidence.

- Network: GenLayer Studionet
- Contract: $(System.Collections.Hashtable.addr)
- Deployment transaction: $(System.Collections.Hashtable.tx)
- Reviewed source SHA-256: $(System.Collections.Hashtable.sha)
- Contract source: contracts/translation_parity.py

Run 
pm install, 
pm run contract:test, 
pm run contract:lint, and 
pm run build.
