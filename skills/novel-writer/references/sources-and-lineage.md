# Sources, Lineage, and Redistribution

Read this file before publishing, forking, relicensing, or moving substantial text from NW into another project. It records influence, license obligations, and the boundary between learning from a mechanism and copying its expression.

## Contents

- [1. Ownership and originality boundary](#1-ownership-and-originality-boundary)
- [2. Software-skill sources](#2-software-skill-sources)
- [3. Text-overlap review](#3-text-overlap-review)
- [4. License of NW](#4-license-of-nw)
- [5. Literary and research sources](#5-literary-and-research-sources)
- [6. Public-release checklist](#6-public-release-checklist)
- [7. Contribution boundary](#7-contribution-boundary)

## 1. Ownership and originality boundary

NW has its own three-core architecture, story-domain model, project-memory seed, adaptive learning gate, routing, fiction tests, examples, and prose guidance developed through repeated author feedback. It is runtime-independent and does not require any upstream application.

NW is not described as a clean-room implementation. Its development involved reading and adapting ideas from the three projects below. Rewriting wording and removing close textual overlap improves editorial originality, but does not erase the documented GPL/AGPL lineage. Keep the provenance record and the AGPL license when publishing this version.

The intended transfer boundary is:

```text
source observation → abstract mechanism and limitation → new fiction-specific structure
→ original wording and original control example → overlap and behavior review
```

Do not copy source examples, tables, command surfaces, or distinctive paragraph sequences merely because the license permits modification.

## 2. Software-skill sources

### Webnovel Writer

- Local source: `webnovel-writer`, itself derived from `lingfengQAQ/webnovel-writer` v6.2.1.
- Upstream: <https://github.com/lingfengQAQ/webnovel-writer>
- License: GNU GPL v3.
- Conceptual influence: long-form fiction routing, genre analysis, continuity concerns, prose and dialogue practice, evidence-based review, and reference-work boundaries.
- NW omits the upstream runtime, dashboard, database, platform commit pipeline, templates, and project-specific data.

### Humanizer-zh

- Source: <https://github.com/op7418/Humanizer-zh>
- License: MIT.
- Copyright notice: Copyright (c) 2026 歸藏.
- Its core is translated from `blader/humanizer` and references `hardikpandya/stop-slop` and Wikipedia's “Signs of AI writing.”
- Conceptual influence: inflated significance, promotional language, vague authority, formulaic triads, negative antithesis, synonym cycling, false ranges, formatting residue, over-qualification, generic conclusions, and the need for a non-neutral textual voice.
- NW rebuilds these as conditional fiction symptoms, supplies different repairs and original examples, rejects mandatory word blacklists, and prevents “specificity” or “messiness” from licensing fabricated facts and random errors.
- License and notice: <https://github.com/op7418/Humanizer-zh/blob/main/LICENSE>. Preserve the upstream copyright notice if future contributors copy or modify a substantial portion of its expression.

### InkOS

- Source: <https://github.com/Narcooo/inkos>
- Relevant package: <https://github.com/Narcooo/inkos/blob/master/skills/SKILL.md>
- License: GNU AGPL v3.
- Conceptual influence: separation of author intent, current focus, canonical truth, readable summaries, and temporal memory; protected versus compressible governed context; non-canonical forecasts and staleness; broad observation followed by validated reflection; conservative audit and revision; visible unresolved findings; staged planning, drafting, review, revision, and settlement.
- NW does not contain InkOS commands, tools, provider setup, Studio/TUI code, schemas, or application runtime.

## 3. Text-overlap review

Before a public release:

1. compare every NW Markdown file with the relevant upstream skill texts;
2. normalize case, whitespace, Markdown punctuation, and links, then flag long exact lines;
3. run a fuzzy or long-common-block pass to catch lightly edited sentence shells;
4. manually review flags, because titles, licenses, URLs, filenames, and necessary technical terms are not plagiarism evidence;
5. rewrite close instructional prose from the underlying idea, not by synonym substitution;
6. verify that all control examples use original characters, objects, actions, settings, and outcomes.

The release audit should report thresholds and findings rather than claim that a similarity scan proves legal independence. License text and required notices are intentionally verbatim legal material and should be excluded from prose-overlap judgments.

## 4. License of NW

NW is distributed under the GNU Affero General Public License, version 3. This is the conservative whole-work license for a synthesis that includes modified GPLv3 material and adapted AGPLv3 material. GNU documents explicit GPLv3/AGPLv3 combination compatibility, with AGPL requirements applying to the combined work.

- AGPL v3: <https://www.gnu.org/licenses/agpl-3.0.en.html>
- GPL/AGPL compatibility: <https://www.gnu.org/licenses/license-compatibility.en.html>

Redistributors must preserve the license, source form, modification notices where required, and this provenance record. This file is a conservative publication guide, not legal advice.

## 5. Literary and research sources

Named novels in `genres-and-works.md` are comparative references, not bundled source material. NW includes no continuous passages from those works. Official or licensed links are recorded to constrain future research to lawful evidence.

General research lineage:

- Wikipedia, “Signs of AI writing”: <https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing>
- WikiProject AI Cleanup: <https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup>
- Author and editor interviews retained with source-specific boundaries in `craft-research.md`.

## 6. Public-release checklist

- Keep `LICENSE`, `SKILL.md`, referenced files, and `sources-and-lineage.md` together.
- State that NW is modified and give the release date or version in the repository metadata.
- Attribute WW, Humanizer-zh, and InkOS with working repository and license links.
- Do not describe this lineage as public domain, proprietary, MIT-only, or clean-room.
- Remove private manuscripts, project canon, attachment paths, API keys, personal names, and local machine data.
- Build a new allowlisted clone; never clean a populated local Core III in place or copy a novel project directory into the release.
- Run `scripts/validate_nw.py <clone> --public-release` plus one `--deny-token` for every known private title, character, setting, and project marker.
- Run structure validation, trigger tests, behavior cases, link checks, and the text-overlap review.
- Explain that the skill aims for stronger fiction and less mechanical prose; it does not guarantee AI-detector evasion or authorship classification.

## 7. Contribution boundary

Contributions should add:

- observable symptoms with real examples or tests;
- positive writing recipes;
- original control samples;
- lawful source provenance;
- genre mechanisms that remain useful after work and author names are removed.

Do not contribute:

- pirated or scraped novels;
- continuous copyrighted passages;
- prompts to imitate a living author;
- word bans presented as detection science;
- claims that NW guarantees detector evasion;
- project-specific canon, private manuscripts, API keys, or personal data.
