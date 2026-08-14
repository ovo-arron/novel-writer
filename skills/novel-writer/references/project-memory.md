# Project Memory and Adaptive Learning

Use this reference whenever NW works on a specific fiction project across more than one task, reads an existing manuscript, continues a project, records accepted changes, or learns project-specific prose and author preferences. Core III is the only per-project storage and learning layer. Core I and Core II remain universal, read-only frameworks.

## Contents

- [1. Core boundary and role](#1-core-boundary-and-role)
- [2. Memory layers](#2-memory-layers)
- [2A. Memory profiles](#2a-memory-profiles)
- [3. Default project structure](#3-default-project-structure)
- [4. Automatic discovery and source map](#4-automatic-discovery-and-source-map)
- [5. Import and evidence-backed filling](#5-import-and-evidence-backed-filling)
- [6. Task-scoped retrieval](#6-task-scoped-retrieval)
- [7. Settlement after work](#7-settlement-after-work)
- [8. Adaptive author and craft learning](#8-adaptive-author-and-craft-learning)
- [9. Learning record and promotion gate](#9-learning-record-and-promotion-gate)
- [10. Query, health, and recovery](#10-query-health-and-recovery)
- [11. Maintenance and compression](#11-maintenance-and-compression)
- [12. Isolation, privacy, and failure modes](#12-isolation-privacy-and-failure-modes)
- [12A. Installed skill, local instance, and public clone](#12a-installed-skill-local-instance-and-public-clone)
- [13. Million-character projects](#13-million-character-projects)

## 1. Core boundary and role

Core I supplies reusable reasoning. Core II supplies reusable expression and revision. Neither stores a title, character, setting fact, manuscript passage, author habit, project voice, or accepted method. Core III discovers and owns those project-specific answers.

Core III may build a temporary task packet for Core I and Core II. After the task, only the evidence-backed delta returns to Core III. The universal skill never absorbs live project content automatically.

When a project already has Core III, its use is automatic for NW work on that novel: discover changed sources, retrieve the smallest relevant packet, and stage a delta without waiting for the author to request each memory operation. If the current or prior work has an explicit acceptance signal, settle routine memory updates as part of the task. Do not write during analysis-only work, and never interpret silence as acceptance.

Core III owns:

- confirmed project truth and current story state;
- the project's adaptation profile: form, release mode, narrative form, genre hierarchy, language/register, research boundary, and active domains;
- the project's compass and eight story domains;
- source authority, file order, accepted units, and conflicts;
- explicit author ideas, decisions, likes, dislikes, corrections, and boundaries;
- observed prose tendencies, dialogue ownership, and OOC evidence;
- methods that worked under stated conditions;
- current focus, open obligations, candidate plans, pending deltas, and quality trends.

It learns by changing future retrieval priority and instructions. It does not train weights, infer the author's personality, or declare its own generated habits correct.

## 2. Memory layers

Keep these layers separate even if an existing project uses different files.

| Layer | Contains | Authority |
|---|---|---|
| Source map | manuscript, outline, bible, correction, research, and memory file pointers; order and freshness | file inspection plus author statement |
| Story truth | compass, eight domains, accepted events, current states | latest author correction, then accepted manuscript |
| Working state | focus, pending deltas, candidate branches, next-task handoff | temporary and partly non-canonical |
| Author profile | explicit intentions, boundaries, collaboration habits, decision preferences, terminology | explicit author evidence only |
| Craft profile | project voice, narration, dialogue, detail, rhythm, formatting | confirmed preference or repeated accepted prose |
| Learning log | scoped feedback-derived and process-derived rules | evidence-gated |
| Unit ledger | accepted-unit causal delta and settlement state | accepted manuscript |
| Quality ledger | recurring problems, successful repairs, unresolved risks | repeated evidence or explicit feedback |
| Summary ladder | unit capsules, sequence/arc summaries, and part/volume settlements with source ranges | compressed orientation, never higher than source |
| Local locator | derived SQLite chunks and search metadata | disposable index; never canon |
| Structure and threads | causal architecture, thread lifecycle, obligations, and elastic ranges | confirmed plan plus accepted-event correction |
| Retrieval cues | aliases, paraphrased questions, consequences, and source ranges | evidence bridge, never canon itself |

Statuses: `confirmed`, `observed`, `trial`, `rejected`, and `stale`. A status without a source and scope is not durable learning.

## 2A. Memory profiles

Choose the smallest profile that preserves continuity:

| Profile | Suitable work | Active memory |
|---|---|---|
| **Ephemeral** | one-off conception, isolated passage, analysis without continuing project | no persistent files; state assumptions and uncertainty in the answer |
| **Minimal** | short story, compact novella, early exploration, or occasional collaboration | source map, adaptation profile, compass, working state, author/craft evidence, core characters/events, unit ledger |
| **Standard** | sustained novella, standalone novel, series, or regular serial | relevant domains, structure and thread ledgers, summaries and quality tracking as needed |
| **Large** | fragmented, multi-volume, research-heavy, or million-character corpus | standard profile plus sharding, summary ladder, retrieval cues, source-change scans, and optional SQLite locator |

Profiles are retrieval and maintenance policies, not different artistic frameworks. The blank seed contains the superset so a project can grow without migration; inactive files may remain empty. Do not upgrade a profile because a template file exists.

## 3. Default project structure

Respect an existing structure. When persistent memory is requested and none exists, copy `assets/project-memory/` or run `scripts/init_project_memory.py`.

```text
.novel-writer/
  INDEX.md
  source-map.md
  adaptation-profile.md
  story-compass.md
  working-state.md
  author-profile.md
  craft-profile.md
  learning-log.md
  unit-ledger.md
  event-ledger.md
  pacing-plan.md
  structure-map.md
  thread-ledger.md
  retrieval-cues.md
  quality-ledger.md
  summaries/
    chapters/
    arcs/
    volumes/
  domains/
    worldbuilding.md
    systems.md
    factions.md
    locations.md
    characters.md
    events-and-plot.md
    items.md
    bestiary.md
```

This is a portable Markdown store, not database theater. Empty sections are valid. Never invent encyclopedia entries or style claims to make the structure look complete. If a project already has its own folders and documents, map them in `source-map.md`; do not move, rename, normalize, or replace them merely to match this template.

## 4. Automatic discovery and source map

When project layout is unknown, inspect it before asking the author to repeat information already present. Use `scripts/scan_project_sources.py <project-root>` for a read-only candidate inventory when helpful.

Discovery order:

1. resolve the exact project root and exclude `.git`, `.novel-writer`, caches, temporary output, exports, backups, and installed skills;
2. identify likely manuscripts, chapter folders, outlines, story bibles, character sheets, world notes, author corrections, and prior memory;
3. infer nothing from a filename alone—open candidate files and verify their role;
4. ask only when two sources could both be authoritative and the choice changes the work;
5. record paths, roles, order, authority, last scan time, and known conflicts in `source-map.md`;
6. on later tasks, compare changed files and read the affected units before stale summaries.

The scanner reports candidates and file metadata; it does not read meaning, choose canon, edit files, or upload content.

## 5. Import and evidence-backed filling

For a new novel, record only explicit seeds, boundaries, unresolved choices, and source pointers. For an existing novel, perform incremental import:

1. read the latest explicit corrections;
2. establish manuscript order and last accepted unit;
3. read accepted text in usable ranges;
4. extract events, states, open obligations, and recurring craft evidence with source pointers;
5. separate objective event, narrator assertion, character belief, rumor, plan, and alternate branch;
6. stage contradictions rather than selecting the cleaner version;
7. fill only affected domains and ledgers;
8. leave unknowns unknown.

Automatic filling means evidence-backed extraction after reading, never bulk completion from headings or names. An extracted fact is stored once in its natural domain and linked where its consequence matters. A compressed note must retain enough source information to return to the manuscript.

## 6. Task-scoped retrieval

Read `INDEX.md`, `source-map.md`, `adaptation-profile.md`, and `working-state.md` first when they exist. For a large project, preserve protected context, orient through the current part/volume/arc summary and recent unit capsules, then use retrieval cues and the local locator to find older exact passages. Then retrieve the smallest packet that can constrain the task:

- relevant accepted manuscript passage or reliable causal summary;
- current time, location, cast, body, resources, knowledge, and relationships;
- facts from only the currently active world, system, faction, location, item, or living-world domains;
- open obligations due now and those that must remain unresolved;
- applicable author-profile, craft-profile, learning-log, and quality entries;
- pending delta whose status changes the requested work.

If the requested unit directly continues an unfinished scene, retrieve the `Immediate scene handoff` from `working-state.md` and verify it against the exact predecessor passage. If the slot is absent, stale, or missing any materially active character, weapon, wound, position, knowledge boundary, or private intent, rebuild it before conception or drafting; a chapter capsule is not a substitute.

For Chinese long-form work, a starting packet of roughly 8,000–24,000 characters is one soft operational range, not a limit on the novel or a universal language rule. For other languages and forms, use the smallest packet that preserves the same evidence. Increase it only when the task genuinely crosses arcs, parts, volumes, formal sources, or several character histories. The full source corpus can contain millions of characters while each task sees only the relevant evidence.

More memory should improve precision, not increase exposition. Retrieved facts constrain choices; they do not earn automatic page space.

## 7. Settlement after work

At task end, stage a delta:

```text
change → natural owner → source → status → affected links
→ chapter/unit ledger → next-task consequence
```

Use two mental passes when a chapter changes many things. **Observe** broadly into a pending candidate delta: facts, body, resources, knowledge, relationships, hooks, and possible craft evidence. Then **reflect** against source authority, character knowledge, and acceptance status before applying anything. Broad observation may over-collect; reflection must reject inference, duplicate facts, and unaccepted plans. Neither pass changes canon by itself.

Drafts, forecasts, alternate branches, and interpretations remain pending. After explicit author acceptance or the project's established acceptance signal:

1. append one unit entry to `unit-ledger.md`;
2. write facts once in their natural domains;
3. update body, resources, relationships, location, item custody, knowledge, factions, and open obligations where changed;
4. update `working-state.md` and the next-task handoff;
5. pass author feedback through the learning gate;
6. update quality trends only with sufficient evidence;
7. mark settled, superseded, rejected, or unresolved pending deltas.

Analysis-only work is read-only. Return a proposed delta without claiming it was stored.

At the start of a later task, settle a previously pending unit first if the author has since accepted it or the authoritative manuscript now establishes it. This prevents memory from remaining one chapter behind while still preserving the acceptance gate.

## 8. Adaptive author and craft learning

Use `author-profile.md` only for explicit author evidence:

- desired experience, priorities, protected ideas, boundaries, and unresolved choices;
- terminology, naming decisions, format and delivery preferences;
- how the author signals acceptance, rejection, uncertainty, or a request for options;
- collaboration habits that materially improve the work;
- preferences scoped to this novel versus deliberately cross-project preferences.

Do not infer personality, biography, mood, or permanent taste from conversational style.

Use `craft-profile.md` for this novel's accepted expression:

- viewpoint distance, narrative register, formatting, and chapter scale;
- detail sources, sentence and paragraph movement, humor and seriousness;
- relationship-specific speech permissions and explanation thresholds;
- recurring imagery grounded in world or viewpoint;
- protected wording mechanisms and rejected mechanical patterns;
- proven drafting or revision methods with conditions and limits.

Character-specific speech evidence belongs primarily in `domains/characters.md`. Long copyrighted samples and named-author imitation prompts never enter project memory.

## 9. Learning record and promotion gate

For each distinct author feedback event, prefer one high-impact learning item over many tiny rules. Use this record:

```text
ID and date:
Status and scope:
Trigger or task:
Surface evidence and source pointers:
Rejected or liked layer: wording/collocation | spoken turn | action causality | scene activity | continuity/story
Observable reason:
Rule for next use:
Next-use test:
Counterexample or limit:
Duplicate or contradiction check:
Last confirmed:
```

The surface phrase is a locator, not necessarily the lesson. A correction may reject an entire activity even when it names one prop; a liked line may confirm relationship permission without endorsing its sentence shell everywhere. Record the deepest supported cause. If a synonym swap would preserve the same unwanted turn, action, or scene function, the stored rule is too shallow.

Choose the memory form before adding an NG entry. An exact **hard ban** requires an explicit author ban and stated scope; preserve it verbatim in that project's Core III. Other rejections become **conditional symptoms** with a failed layer, observable cause, next-use test, and counterexample. Liked wording becomes protected evidence plus its transferable mechanism. Merge same-cause feedback instead of growing a phrase blacklist. Use `anti-ai-execution.md` for the compact decision and stop rule.

Promotion gate:

| Evidence | Action |
|---|---|
| Explicit preference, boundary, or correction | `confirmed` within the stated scope |
| Accepted choice plus author's reason | store the mechanism, not a sentence shell |
| Pattern across at least two accepted units | `observed` with both source pointers |
| Proposed method or inferred preference | `trial` |
| Rejected draft, revision, branch, or outline | exclude from positive learning; record rejection only if useful |
| Typo, accident, continuity error, or model habit | never learn as voice |

Before adding, search the learning log, author profile, craft profile, and relevant character entry. Merge only truly equivalent items; preserve differences in scope, listener, scene type, or time. A later explicit correction can mark an older rule `stale` or `rejected`.

Every confirmed craft learning must be callable. Its `Next-use test` should name an observable question or comparison for the next relevant draft, such as whether an omitted object has one recoverable referent, whether a character would still perform the activity if no information needed delivery, or whether an interruption has a concrete cause. A warning without a next-use test becomes an inert catalog.

Core III never promotes a rule into Core I or Core II automatically. Cross-project promotion requires deliberate human review, abstraction, privacy removal, source/licence review, and a separate skill update.

## 10. Query, health, and recovery

For query, answer from the narrowest authoritative source and return status, source pointer, and material conflict. Use manuscript text when exact wording or scene logic matters; use compressed memory for orientation.

Health check:

- source map missing or stale;
- accepted unit absent from the unit ledger;
- pending delta older than its accepted source;
- duplicate or contradictory facts without statuses;
- current state inconsistent with the last accepted event;
- learned rule supported only by generated text;
- character voice rule lacking listener or context;
- quality ledger full of one-off stylistic complaints;
- working state that no longer follows the manuscript.

Recovery order:

1. protect existing files and identify authority;
2. scan changed sources;
3. reconstruct the last accepted unit and current state from manuscript;
4. repair the lowest-authority summary, plan, or memory entry;
5. leave unresolved conflicts visible;
6. rebuild the smallest next-task packet.

Never rewrite chapters automatically to hide a memory conflict.

## 11. Maintenance and compression

As the novel grows:

- keep `INDEX.md` and `working-state.md` short;
- append compact ledger entries and periodically archive resolved temporary detail if the author wants;
- preserve source pointers and authority when compressing;
- mark superseded observations `stale` instead of erasing history;
- merge duplicates only after checking scope and status;
- retain identity, promises, rules, injuries, resources, knowledge boundaries, author corrections, and unresolved conflicts;
- remove resolved plans from active retrieval while preserving accepted consequences;
- keep profiles selective enough to guide rather than imitate.

For long projects, do not let one unit ledger or one domain file grow forever. Shard by stable boundaries such as volume, part, arc, era, region, faction, or character cluster, and keep a short manifest pointing to those shards. Compression adds a navigational layer; it never deletes the authoritative manuscript or silently removes uncertainty. If an existing project uses `chapter-ledger.md`, keep using it as the accepted-unit ledger instead of creating duplicate authority.

When a batch import, reverse outline, or multi-volume plan fails, preserve completed ranges and restart from the last verified unit. Do not overwrite earlier accepted memory merely to obtain one clean rerun. Record incomplete ranges in working state so recovery is observable.

## 12. Isolation, privacy, and failure modes

Each novel has its own Core III. Never write live memory into the installed NW folder or retrieve another novel's names, facts, prose, preferences, or private material without explicit direction. Exclude credentials, unrelated personal data, pirated text, long copyrighted excerpts, and detector-evasion claims.

Common failures:

- **Lore quota** — retrieved facts appear because they were found.
- **Draft promotion** — generated work becomes canon before acceptance.
- **Self-confirming learning** — NW learns from its own repetition.
- **Style overfit** — one liked sentence becomes a global rule.
- **Author profiling** — conversational behavior becomes unsupported personality claims.
- **Cross-project leakage** — another novel contaminates this one.
- **Database theater** — empty fields and duplicate summaries create maintenance without better choices.
- **Lossy compression** — uncertainty, knowledge boundaries, or source distinctions disappear.
- **Stale automation** — an old summary outranks a changed manuscript.

When memory and accepted manuscript conflict, the later explicit author correction or accepted manuscript wins.

## 12A. Installed skill, local instance, and public clone

Keep three authorities physically and conceptually separate:

| Authority | May contain | Must not contain |
|---|---|---|
| Installed NW Skill | universal Core I/II methods, Core III mechanism, scripts, evaluations, blank memory seed | live novel facts, populated author profile, manuscript, local project path |
| Local Core III instance | one project's manuscript pointers, canon, plans, corrections, voice, accepted learning, derived index | another project's data or automatic cross-project promotion |
| Public release clone | installed universal files, blank seed, license, provenance, generic tests and repository documentation | any populated Core III instance, private novel name, character, setting, prose, preference, attachment path, account data, or local absolute path |

Publishing is a copy operation from an allowlisted universal source, not a cleanup operation on a local project. Never delete, rewrite, anonymize in place, or migrate a private project to make a public clone safe. Build the clone in a new destination, deny known private tokens, validate it independently, and compare the protected local instance before and after.

Use `scripts/build_public_clone.py` to create a new skill-only clone without caches or derived indexes. Then run `scripts/validate_nw.py <clone> --public-release --deny-token <private-token>` once for each known project marker. A successful scan reduces accidental leakage risk; it does not authorize publication or prove that every private fact has been identified.

## 13. Million-character projects

Read `long-form-memory.md` when the manuscript approaches several hundred thousand characters, spans multiple volumes, or retrieval begins missing old material. Use its five-tier model:

1. hot current state;
2. warm current arc and volume;
3. compressed chapter, arc, and volume summaries;
4. cold authoritative source;
5. a disposable local locator.

Build or refresh the locator with `scripts/project_archive.py build <project-root>`, inspect coverage with `status`, and search with `search`. It records both source bytes and decoded character counts, uses incremental hashes, supports Chinese short-query fallback, and stays inside `.novel-writer/index/`. Search results are pointers, not answers: open the cited source range before resolving exact wording, canon conflict, or delicate character evidence.

Use `pacing-plan.md` and `event-ledger.md` beside the summary ladder so story scale and memory scale grow together. Full policies for sharding, retrieval order, maintenance, and honest limitations live in `long-form-memory.md`; do not duplicate them into every project file.
