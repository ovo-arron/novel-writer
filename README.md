# Novel Writer (NW)

Novel Writer is a portable Agent Skill for conceiving, drafting, continuing, revising, and maintaining fiction across genres, languages, lengths, narrative forms, and publication modes.

NW 不是某一种网文模板。它可以用于短篇、中篇、单行本、系列与长篇连载，也可以适配现实、文学、言情、历史、悬疑、犯罪、惊悚、恐怖、科幻、奇幻、修仙、轻小说、书信体、文档体、非线性与实验性小说。

Public release candidate: `0.3.0`.

## Three cores

1. **Core I — Conceive**：选择作品真正的叙事引擎并构思。除了情节与冲突，也支持人物策略、关系、调查、声音/意识、氛围/地方、观念/制度及形式驱动。
2. **Core II — Draft**：把构思转成由视角或叙述者拥有的文本。按需使用场景、概述、省略、反思、说明、对白、书信、报告、档案、复现与其他形式。
3. **Core III — Remember & Evolve**：为每部作品隔离事实、人物状态、作者修订、项目文风与长期召回。支持 ephemeral、minimal、standard 与 large 四种记忆深度。

三个核心按任务使用不同深度，不会为了“完整”强制输出三份报告或建立整套数据库。

## Capabilities

- story premise, narrative engine, character and relationship design;
- causal, perceptual, relational, atmospheric, institutional, and formal structure;
- scenes, chapters, documents, nonlinear revelation, arcs, parts, volumes, and series;
- character-owned dialogue, private-state-to-spoken-turn conversion, natural prose, detail, rhythm, and targeted anti-mechanical revision;
- source authority, continuity, OOC control, accepted-state settlement, and project-specific learning;
- optional local retrieval for fragmented or million-character manuscripts;
- lawful comparative craft research without bundling copyrighted novel text or asking for imitation of a living author's distinctive style.

NW improves observable fiction problems; it does not guarantee AI-detector evasion or authorship classification.

## Language scope

NW's conception, continuity, character, dialogue, and memory workflows are language-portable, but portability is not a claim of native-level mastery in every language. Chinese is the most extensively calibrated target in this release. English and Japanese projects can use the same three-core workflow; publication-ready idiom, regional usage, honorifics, and period or professional registers should still be checked by a qualified native reader when they matter.

## Repository layout

```text
skills/novel-writer/   # installable skill only
README.md              # repository documentation
NOTICE.md              # provenance summary
CONTRIBUTING.md        # contribution and privacy boundary
.github/workflows/     # cross-platform validation
```

The installable skill contains universal methods, scripts, evaluations, and blank project-memory templates. It contains no populated novel memory.

## Installation

Copy `skills/novel-writer` into the personal skills directory supported by your Agent Skills client, preserving the folder name `novel-writer`.

Common Codex locations:

- Windows: `%USERPROFILE%\.codex\skills\novel-writer`
- macOS/Linux: `~/.codex/skills/novel-writer`

Example requests:

```text
Use $novel-writer to design a quiet place-driven novella without forcing a villain.
Use $novel-writer to decide which six months should be scene, summary, or ellipsis.
Use $novel-writer to continue this mystery from the accepted manuscript and preserve knowledge boundaries.
Use $novel-writer to diagnose mechanical dialogue without rewriting the rest of the chapter.
```

## Project memory

Persistent Core III memory belongs inside each fiction project, never inside the installed skill. Initialize a blank superset when persistence is wanted:

```bash
python skills/novel-writer/scripts/init_project_memory.py /path/to/fiction-project
```

Use only the memory depth the work needs. A one-off task may remain ephemeral; a short work can use minimal memory; a sustained novel can use standard memory; a multi-volume corpus can use the large retrieval model and optional local SQLite locator.

## Validation

```bash
python skills/novel-writer/scripts/validate_nw.py skills/novel-writer --public-release
python -m compileall -q skills/novel-writer/scripts
```

Repository text is UTF-8. If a third-party Python validator on Windows uses a legacy locale encoding, invoke it with `python -X utf8 ...`.

To build another clean skill-only clone from an installed copy, use a new destination and pass every known private project marker as a deny token:

```bash
python scripts/build_public_clone.py /new/destination/novel-writer \
  --deny-token "private-title" \
  --deny-token "private-character"
```

The builder refuses to overwrite an existing destination and never cleans a local project in place.

## License and provenance

NW is distributed under [GNU AGPL v3](LICENSE). It incorporates adapted ideas from Webnovel Writer (GPL-3.0), Humanizer-zh (MIT), and InkOS (AGPL-3.0). It is not represented as clean-room or MIT-only. See [NOTICE.md](NOTICE.md) and [`sources-and-lineage.md`](skills/novel-writer/references/sources-and-lineage.md).
