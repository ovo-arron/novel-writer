# Contributing

Contributions should improve a concrete fiction task and add or update an evaluation case.

Good contributions include:

- a narrative engine or form not handled well;
- an observable conception, prose, dialogue, continuity, or memory failure;
- a positive repair recipe with an original control example;
- a compatibility, retrieval, validation, or privacy improvement;
- lawful source provenance and a clear anti-copy boundary.

Do not contribute private manuscripts, populated Core III directories, personal data, credentials, pirated or scraped novels, continuous copyrighted passages, prompts to imitate a living author's distinctive style, or claims of guaranteed AI-detector evasion.

Before opening a pull request, run:

```bash
python skills/novel-writer/scripts/validate_nw.py skills/novel-writer --public-release
python -m compileall -q skills/novel-writer/scripts
```

If a change adapts another project, update `sources-and-lineage.md` with its repository, license, required notice, transferred mechanism, and rewritten boundary.
