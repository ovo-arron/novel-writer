# Multi-Million-Character Memory

Use this reference when a novel may exceed several hundred chapters, the manuscript approaches or exceeds one million Chinese characters, project files become fragmented, retrieval misses old facts, or Core III files become too large to scan safely.

## Contents

- [1. Capacity principle](#1-capacity-principle)
- [2. Five-tier memory](#2-five-tier-memory)
- [3. Project layout at scale](#3-project-layout-at-scale)
- [4. Accepted-unit compression](#4-accepted-unit-compression)
- [5. Domain sharding](#5-domain-sharding)
- [6. Local archive and incremental indexing](#6-local-archive-and-incremental-indexing)
- [7. Governed context](#7-governed-context)
- [8. Retrieval packet](#8-retrieval-packet)
- [9. Semantic bridge to exact source](#9-semantic-bridge-to-exact-source)
- [10. Query expansion and verification](#10-query-expansion-and-verification)
- [11. Maintenance schedule](#11-maintenance-schedule)
- [12. Capacity limits and failure recovery](#12-capacity-limits-and-failure-recovery)

## 1. Capacity principle

Million-scale support does not mean loading millions of characters into one model context. It means:

```text
full accepted manuscript remains on disk
→ every accepted unit receives a compact locator and state delta
→ chapters roll up into arcs and volumes
→ entities and events are sharded instead of endlessly appended
→ a local index finds exact source passages
→ each task receives a small evidence-backed retrieval packet
```

The source corpus may contain several million or tens of millions of characters. The active context remains bounded. Capacity comes from loss-aware compression, searchable source pointers, and incremental retrieval—not from pretending the model remembers the whole book.

## 2. Five-tier memory

| Tier | Purpose | Typical contents | Load behavior |
|---|---|---|---|
| **L0 hot state** | write the next unit correctly | `working-state.md`, latest accepted scene, present bodies/resources/knowledge/relationships, current chapter contract | always for continuation |
| **L1 warm arc state** | preserve current movement | current arc summary, current volume summary, active event ledger, active entities and obligations | load by current arc/task |
| **L2 compressed history** | orient across hundreds of units | unit capsules, closed arc summaries, older part or volume summaries, unit-ledger shards | search or load selected ranges |
| **L3 cold source** | final authority and exact evidence | accepted manuscript, author corrections, original bible files | open exact passages when wording or causality matters |
| **L4 locator index** | find relevant L2/L3 evidence | local SQLite chunk index, paths, headings, character offsets, hashes | query first; never treat as canon itself |

L0 should remain small enough to read at every continuation. L1 may grow within the current arc but is compressed when the arc closes. L2 and L3 may grow indefinitely because they are not loaded wholesale.

## 3. Project layout at scale

The blank seed starts small. Add or shard only when the novel grows:

```text
.novel-writer/
  INDEX.md
  working-state.md
  pacing-plan.md
  event-ledger.md
  summaries/
    chapters/ch0001.md ...
    arcs/arc-001.md ...
    volumes/volume-001.md ...
  ledgers/
    chapters-0001-0100.md
    chapters-0101-0200.md
  domains/
    characters.md              # small-project form
    characters/index.md        # sharded form
    characters/core/*.md
    characters/support/*.md
    events-and-plot/index.md
    events-and-plot/volume-001.md
  index/project-index.sqlite3  # derived and rebuildable
```

Respect existing manuscript organization. The numbers and folder names are defaults, not canon. Do not reorganize author files merely to match this example.

## 4. Accepted-unit compression

After every accepted chapter or unit, create or update four representations:

1. **Source** — accepted prose remains untouched.
2. **Chapter capsule** — compact causal retrieval record, normally a few hundred Chinese characters plus structured fields.
3. **State delta** — only body, resource, location, knowledge, relationship, item, faction, promise, and open-obligation changes.
4. **Search locator** — path, heading, character range, and source hash in the local index.

A chapter capsule records:

- entry state and immediate unfinished action;
- decisive attempts, counter-moves, choice/failure, and result;
- reader-visible signal and author-only spoiler kept separately;
- changed states and who knows what;
- open obligations advanced or created;
- emotional/material residue;
- exact source pointer and acceptance status.

At arc closure, summarize the transformation rather than concatenating chapter capsules. At volume closure, summarize promise, causal spine, relationship movement, system/faction changes, paid and unpaid obligations, and the changed starting condition for the next volume.

Compression never replaces source authority. If a task turns on exact wording, motive, clue placement, or scene order, reopen the source.

## 5. Domain sharding

Split a domain when scanning it becomes slower or less reliable than opening one targeted shard. Common signals include many unrelated entities, several volumes of mixed event history, frequent merge conflicts, or repeated retrieval of the wrong homonymous entry.

Use a short domain index with stable IDs, aliases, status, shard path, last relevant unit, and one-line retrieval cue. Shard by a natural boundary:

- characters by importance, faction, generation, or region;
- events by volume, arc, or historical period;
- locations by region;
- factions by polity or institution family;
- items by owner, class, or volume of active use;
- bestiary by ecology or region;
- systems by operational subsystem.

Do not shard by arbitrary equal file size if the split destroys retrieval meaning. Keep one fact in one authoritative shard and link consequences elsewhere.

## 6. Local archive and incremental indexing

Use `scripts/project_archive.py` when the source corpus is too large for direct browsing.

```powershell
python scripts/project_archive.py build <project-root> --json
python scripts/project_archive.py status <project-root> --json
python scripts/project_archive.py search <project-root> "灰塔粮仓" --scope source --limit 8 --json
python scripts/project_archive.py search <project-root> "她为什么不信任军方" --scope memory --json
```

The archive:

- indexes UTF-8/GB18030 Markdown and text sources plus readable NW memory locally;
- splits on chapter/headings and bounded text chunks;
- uses SHA-256, file size, and modification time for incremental refresh;
- uses SQLite FTS5 trigram search for Chinese phrases and substring fallback for short queries;
- returns path, heading, character offsets, and excerpts;
- excludes `.novel-writer`, backups, caches, exports, temporary output, and Git internals;
- stores a rebuildable database under `.novel-writer/index/`;
- reports authoritative/project source characters separately from memory characters;
- never uploads manuscript text and never edits source files.

Building the archive is a project mutation and requires file-writing scope. `search` and `status` are read-only. The index is a locator, not story truth; verify important results against accepted source and authority rules.

## 7. Governed context

When the task packet must shrink, separate **protected context** from **compressible context**.

Protected context is material whose omission could silently change the requested work:

- latest explicit author intent, boundary, correction, and acceptance rule;
- identity facts, irreversible deaths or losses, hard system limits, and current body/resource state;
- viewpoint knowledge boundaries and secrets that must not leak;
- active promises or obligations whose due conditions are present;
- current event dependency, exact last-scene tail, and blocking continuity conflict;
- source authority and uncertainty status.

Compressible context includes older resolved events, inactive entities, distant setting detail, superseded plans, and prose observations not relevant to the current scene. Compress it into source-linked summaries before dropping it. Never protect a fact merely because it is dramatic, and never compress a fact merely because it is old.

Record a short retrieval trace in `working-state.md`: task, protected material, summaries and exact passages loaded, search terms used, important omissions, and unresolved conflicts. The trace proves what informed the work; it is not new canon.

## 8. Retrieval packet

For a normal continuation, build a packet in this order:

1. author intent and current working state;
2. exact tail of the last accepted scene;
3. last two to four chapter capsules;
4. current arc and volume summaries;
5. current chapter/event contract;
6. relevant character, location, system, faction, item, and creature shards;
7. active obligations and time/resource constraints;
8. three to eight search results for older dependencies;
9. relevant author/craft/quality learning only.

Use a soft retrieval packet budget rather than a rigid token promise. Start around 8,000–24,000 Chinese characters for ordinary chapter work, then enlarge only when the task demonstrably needs multiple old scenes or a complex consistency audit. Exact source passages displace generic summaries; irrelevant lore never fills unused budget.

For queries, load less. For full-volume review, retrieve more summaries and selected source scenes in batches rather than one enormous packet.

## 9. Semantic bridge to exact source

FTS phrase search is strongest when the remembered wording resembles the manuscript. For concept questions, use `retrieval-cues.md` as an evidence-backed bridge:

```text
remembered question or meaning
→ search memory summaries/cues
→ recover canonical names, aliases, objects, places, consequences, and source ranges
→ search authoritative source with those concrete terms
→ open and verify the exact passage
```

Maintain cues for renamed people and places, euphemisms, relationship turning points, mysteries, repeated objects, institutional incidents, and consequences that an author may remember without the original wording. A cue needs a source range and status. Do not invent a causal interpretation merely to improve search.

Use `--scope memory` for the first pass and `--scope source` for verification. `--scope all` is convenient for orientation. This is a transparent semantic bridge, not an embedding model: it can retrieve paraphrased ideas only when summaries or cues preserve the conceptual connection. If it misses, expand the query from entities, objects, locations, actions, and consequences, then repair the cue only if the connection is real.

## 10. Query expansion and verification

Search with project terms, aliases, relationships, objects, locations, and consequences—not only the abstract question. If “为什么她不信任军方” returns weak results, expand into the character name, relevant officer, prior arrest, missing letter, border hospital, and the volume where trust changed.

Verification chain:

```text
index hit → source passage → chapter capsule/state delta
→ entity or event shard → current authority and status
```

If compressed memory and source disagree, repair memory. If two accepted sources disagree, preserve the conflict and use the later explicit author correction when available.

## 11. Maintenance schedule

- **Every accepted unit:** capsule, delta, ledger settlement, working-state handoff, incremental index build.
- **Whenever names or interpretations change:** update retrieval cues with aliases, consequences, and exact source ranges.
- **Every short event or sequence:** update event ledger and actual chapter span.
- **Every arc closure:** create arc summary, close/defer obligations, compress inactive L1 state into L2.
- **Every major-part closure:** create the relevant part or volume summary, shard the unit ledger, review domain indexes, and rebuild current L0/L1 state.
- **Periodically:** run archive status; detect deleted/changed sources, missing capsules, duplicate IDs, stale summaries, and oversized unsharded domains.

Do not rewrite old summaries merely for stylistic consistency. Revise them when authority, retrieval accuracy, or compression quality is wrong.

## 12. Capacity limits and failure recovery

NW can index and retrieve multi-million-character local corpora, but it still cannot reason over the whole corpus simultaneously. Its quality depends on accepted-unit settlement, usable source organization, governed context, and correct retrieval queries. The cue bridge improves concept recall without claiming vector-level semantic equivalence.

Failure recovery:

- missing index → rebuild from source;
- stale index → incremental build;
- missing capsule → reconstruct from accepted chapter and mark reconstructed;
- bloated hot state → settle durable facts, close inactive obligations, move history to L2;
- lossy summary → reopen source and replace only the incorrect summary;
- missed old dependency → expand query and add a durable alias/link if the connection is real;
- corrupted derived database → remove or replace only the index after confirming its exact path; never delete manuscript or project memory.

The archive database is disposable. The manuscript, explicit author decisions, and accepted memory deltas are not.
