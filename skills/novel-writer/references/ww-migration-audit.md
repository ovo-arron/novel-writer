# WW to NW Capability Migration Audit

This audit records whether the creative and long-form abilities of Webnovel Writer (WW), later custom additions, Humanizer-zh, and InkOS are represented in NW without copying their expression or importing unnecessary runtime weight.

## Contents

- [1. Decision rule](#1-decision-rule)
- [2. Core creative migration](#2-core-creative-migration)
- [3. Later WW additions](#3-later-ww-additions)
- [4. Operational migration](#4-operational-migration)
- [5. Humanizer-zh and InkOS](#5-humanizer-zh-and-inkos)
- [6. Deliberate non-migrations](#6-deliberate-non-migrations)
- [7. Remaining risks](#7-remaining-risks)
- [8. Structural replacement map](#8-structural-replacement-map)
- [9. Replacement verdict](#9-replacement-verdict)

## 1. Decision rule

Migrate a capability when it improves conception, drafting, continuity, author collaboration, or long-form reliability. Re-express it as an original, tool-neutral principle or lightweight project artifact. Do not import copied prose, provider setup, database schemas, dashboards, model-specific agents, or platform assumptions into the universal cores.

Project-specific samples and preferences belong in Core III, not in the installed skill.

## 2. Core creative migration

| WW capability | NW location | Status |
|---|---|---|
| inspiration, premise, selling point, renewable engine | `ideation-engine.md`, `story-compass.md`, `story-design.md` | migrated and generalized |
| world, power, faction, location, item, creature design | eight domain references | migrated and expanded |
| character design, relationship, voice, OOC | `characters.md`, `dialogue.md` | migrated and strengthened |
| character-generated plot, strategy memory, attention-led prose, integrated craft repair | `craft-integration.md`, `characters.md`, `structural-architecture.md`, `detail-and-texture.md` | added as a compact cross-layer bridge; not loaded for narrow fixes |
| outline, scene, chapter, event span, arc, volume design | `story-design.md`, `events-and-plot.md`, `plot-and-pacing-engine.md`, `fiction-workflows.md` | migrated and expanded without rigid percentages |
| conflict and independent opposition | `ideation-engine.md`, `story-design.md` | migrated |
| continuity, knowledge, time, body, resources | `continuity.md` | migrated and expanded |
| query and integrated consistency reasoning | `continuity.md`, `fiction-workflows.md`, `serial-production.md`, `long-form-memory.md` | migrated with layered retrieval and exact-source return |
| review, blocking issue, smallest repair | `revision.md`, `serial-production.md` | migrated with evidence threshold |

## 3. Later WW additions

| Later addition | NW location | Status |
|---|---|---|
| core NG card | `anti-ai-execution.md`, `natural-prose.md`, `dialogue.md`, `revision.md` | mechanisms migrated; one compact router selects the deepest failed layer before detailed references |
| dialogue core card and dialogue lab | `dialogue.md`, `characters.md` | migrated and made relationship-specific |
| human prose training lab | `natural-prose.md`, `detail-and-texture.md` | migrated with positive scene construction |
| author feedback contract | `revision.md`, `project-memory.md` | migrated with rejected-layer diagnosis, mechanism extraction, scope boundary, and next-use test |
| author-confirmed dialogue bank | Core III character/craft memory | structure migrated; project sample content deliberately excluded |
| author error catalog and glossary | `author-profile.md`, `learning-log.md`, character and craft entries | capability migrated; old project data excluded |
| plot signal versus spoiler | `fiction-workflows.md`, `serial-production.md` | migrated explicitly |
| reading-power, hooks, payoff, cool points | `serial-production.md`, genre references | migrated as reader pressure and payoff; numeric quotas removed |
| iconic-line mechanics | `natural-prose.md`, `genres-and-works.md` | abstract mechanisms retained; copied lines excluded |
| prose fingerprint library | `craft-research.md`, `genres-and-works.md`, Core III craft evidence | research method migrated; imitation and stored excerpts excluded |
| Qidian and genre contracts | `story-compass.md`, `genres-and-works.md`, Core III project compass | generic contract migrated; time-sensitive platform rules not hard-coded |

## 4. Operational migration

| WW operation | NW replacement | Status |
|---|---|---|
| init | blank project-memory seed and initializer | migrated |
| preflight/project status | source map, working state, source scanner | migrated lightly |
| chapter contract | `serial-production.md` | migrated |
| write/review/revise gates | Core loop plus chapter lifecycle | migrated |
| accepted chapter commit | chapter ledger plus settlement gate | migrated semantically |
| fact extraction and projection | evidence-backed import and domain settlement | migrated semantically; model reads meaning |
| learn | author profile, craft profile, learning log, promotion gate | migrated and strengthened |
| query | narrow authoritative retrieval and cross-domain trace | migrated |
| doctor/recovery | health checklist and reconstruction order | migrated |
| dashboard | Markdown index, summary ladder, pacing plan, and ledgers | intentionally simplified |
| recent chapter summaries and story skeleton | chapter capsules plus arc and volume summaries | migrated with explicit source ranges |
| compact working memory and selective recall | hot/warm/compressed/source/locator tiers plus retrieval packet | migrated and made capacity-aware |
| BM25/vector retrieval | local SQLite FTS5 trigram locator with Chinese short-query fallback | migrated for exact and lexical retrieval; semantic vector reranking not reproduced |
| incremental corpus index | size, modification time, SHA-256, stale-file deletion, and chunk rebuild | migrated |
| million-character corpus support | sharded Markdown, hierarchical summaries, cold source, local locator | migrated and scale-tested; never represented as one model context |
| event-to-chapter and rolling beat planning | event span estimator, chapter capacity, rolling windows, pacing/event ledgers | migrated and expanded |
| governed context selection | protected versus compressible context plus retrieval trace | migrated from InkOS concept and adapted to portable Markdown |
| concept-level old-memory recall | retrieval cues → memory search → concrete terms → source search | added; transparent semantic bridge without external embeddings |
| Observer/Reflector state update | broad pending observation followed by authority/acceptance reflection | migrated semantically without agent-temperature machinery |
| Git backup | user's normal version control | not bundled |
| multi-agent context/reviewer/data agents | one three-core workflow | consolidated, not reproduced |

## 5. Humanizer-zh and InkOS

Humanizer-zh contributes observable general AI-text symptoms: inflated significance, promotional evaluation, false ranges, formulaic enumeration, vague authority, synonym cycling, and generic conclusions. NW translates only fiction-relevant mechanisms into `natural-prose.md` and routes their use through `anti-ai-execution.md`. It rejects detector claims, universal word bans, random first-person opinion, deliberate mess, sentence-length quotas, and automatic list reshaping; fiction repairs must still pass viewpoint, canon, relationship, and causality.

InkOS contributes separation of intent, canon, current focus, plan, draft, audit, revision, and settlement; task-scoped context; and non-canonical forecasts. Its current application runtime also offers chapter import and state reconstruction, multi-dimensional audits, analytics, model routing, Studio/CLI workflows, interactive narrative, research, and export. NW carries the fiction-reasoning and state-authority ideas through the shared spine, continuity rules, project memory, and chapter lifecycle; it does not claim to reproduce that application surface.

## 6. Deliberate non-migrations

- Long copyrighted passages, famous-line collections, and distinctive living-author imitation prompts.
- Facts, dialogue examples, glossaries, and author corrections from any specific novel; these belong only in that novel's Core III.
- Fixed genre percentages, hook quotas, cool-point quotas, and automatic blocking thresholds.
- WW dashboards, provider adapters, multi-agent orchestration, and Git automation. NW uses its own smaller local index design rather than copying WW's schema.
- InkOS Studio/CLI, chapter import engine, analytics, model routing, image/export pipeline, and interactive-film or open-world runtime.
- Time-sensitive platform policy or market claims embedded as permanent universal truth.

These omissions prevent Core I and Core II from becoming project-specific, legally risky, contradictory, or overly engineered.

## 7. Remaining risks

- NW can now store and locate multi-million-character local corpora, but lexical search is weaker than WW's optional semantic vector retrieval when the query shares no wording with the source.
- NW does not claim that millions of characters fit into one model context. Reliability still depends on maintained chapter/arc/volume compression and task-scoped retrieval.
- NW also has less operational automation than the current InkOS application: it relies on Codex to read and reason over files instead of a dedicated import, analytics, and execution engine.
- Automatic source discovery identifies candidates but cannot decide semantic authority without reading or author evidence.
- Adaptive learning still depends on explicit acceptance and reliable source pointers; vague feedback produces weaker memory.
- One-skill portability trades dashboard visibility and automated metrics for transparency and lower maintenance.

For writing quality, author adaptation, dialogue, anti-mechanical prose, project isolation, transparent long-form continuity, event-span reasoning, and local million-character storage, NW now covers or exceeds the migrated WW design goals. WW remains operationally stronger in semantic vector retrieval, entity-graph automation, dashboards, Git commits, and multi-agent throughput. This is a capability comparison, not a claim that either system can recall an entire novel without retrieval or maintenance.

## 8. Structural replacement map

| WW structural surface | NW replacement | Decision |
|---|---|---|
| master outline: premise, main line, hidden line, volume ranges, growth, milestones, foreshadowing | story compass + `structure-map.md` + `thread-ledger.md` + event domain | fully covered with clearer authority and thread states |
| volume beat table | inherited entry, promise/campaign, opposition clock, condition change, climax choice, settlement, handoff, elastic range | covered without forcing three crises, false victory, or lowest point |
| volume timeline and countdown | event timeline, time/travel/message constraints, pacing plan, chapter entry/exit state | covered; large time jumps require causal evidence rather than a mandatory transition chapter |
| fixed Quest/Fire/Constellation weave | open thread types with own futures, collision targets, advancement evidence, and stale debt | replaced by a more general model; fixed genre ratios deliberately rejected |
| CBN/CPN/CEN structured chapter nodes | inherited entry → dominant movement → changed exit → next dependency | covered with fewer compulsory fields and no fixed internal-node count |
| eight-to-twelve chapter planning batches | rolling planning horizon: next 8–12 mapped, next 3–5 contracted, later ranges provisional | covered |
| reading-power taxonomy, hooks, micro-payoffs | reader pressure, local payoff, signal/spoiler separation, open obligations, must-advance/eligible/stale-debt states | covered without quotas |
| cross-volume recent summaries and open loops | chapter capsules, arc/volume summaries, thread ledger, retrieval cues, exact-source verification | covered at larger scale |
| context agent and data agent | governed task packet plus observe/reflect settlement | covered semantically in one three-core workflow |
| outline validation and recovery | structural stress test, reverse outline, source authority, stale forecast and lowest-authority repair | covered |

## 9. Replacement verdict

For the author's stated scope—original novels and webnovels, conception, structure, drafting, revision, project memory, continuity, pacing, and anti-mechanical prose—NW is the primary and sufficient skill. It no longer needs WW for a missing creative or structural method.

This does not mean every WW application feature was cloned. WW remains a separate heavier runtime for dashboards, automated Git commits, provider-backed vectors, entity-graph projections, and multi-agent execution. NW replaces those features only where they affect the writing decision: local indexing, evidence-linked state, governed retrieval, structural maps, thread ledgers, and conservative settlement. If a future task explicitly requires WW's dashboard or vector service itself, that is a tooling requirement rather than a novel-writing knowledge gap.
