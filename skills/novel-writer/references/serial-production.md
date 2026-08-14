# Long-Form Serial Production

Use this reference for chapter-by-chapter webnovel work, volume pacing, reader pull, foreshadowing, chapter review, accepted settlement, project query, and resuming interrupted work. It supplies a lightweight production contract without requiring a database, dashboard, or external runtime.

## Contents

- [1. Production state](#1-production-state)
- [2. Chapter lifecycle](#2-chapter-lifecycle)
- [3. Chapter contract](#3-chapter-contract)
- [4. Reader pull and payoff](#4-reader-pull-and-payoff)
- [5. Signal, spoiler, and knowledge](#5-signal-spoiler-and-knowledge)
- [6. Event and chapter budget](#6-event-and-chapter-budget)
- [7. Multi-chapter pacing](#7-multi-chapter-pacing)
- [8. Foreshadowing and open obligations](#8-foreshadowing-and-open-obligations)
- [9. Review and quality trend](#9-review-and-quality-trend)
- [10. Settlement and projection](#10-settlement-and-projection)
- [11. Query and recovery](#11-query-and-recovery)

## 1. Production state

Keep these states distinct:

- `planned` — causal proposal, not canon;
- `drafting` — prose may create provisional details;
- `reviewed` — issues identified, still not accepted;
- `revised` — changed draft, still not automatically accepted;
- `accepted` — author-approved or stored under the project's explicit acceptance signal;
- `settled` — accepted consequences have been written into Core III;
- `superseded` — replaced by a later accepted version.

Do not infer acceptance from silence. A file saved by NW remains a draft unless the project defines saving or placement as acceptance.

## 2. Chapter lifecycle

```text
retrieve → contract → conceive → draft → local review → revise
→ author decision → settle → next-task handoff
```

The lifecycle is a gate sequence, not nine mandatory documents. For a short request, keep it internal. For persistent work, record the accepted unit in `unit-ledger.md` and current handoff in `working-state.md`.

Before writing, stop only for a contradiction that would materially change the chapter. Unknown decorative facts can remain unknown. After writing, do not polish continuity into existence; reconcile against authority.

## 3. Chapter contract

A compact contract may contain:

- entry state: time, place, present cast, body, resources, knowledge, and emotional/material residue;
- practical objective and pressure;
- opposition's independent action;
- one decisive choice, failure, discovery, or relationship movement;
- reader-visible signal;
- author-only spoiler or hidden cause, if relevant;
- promised local payoff;
- changed exit state and what carries forward;
- constraints that must not be violated;
- one prose or dialogue risk to watch.

Do not turn this into a fixed beat quota. A quiet chapter may move knowledge, trust, labor, or obligation instead of winning a fight.

## 4. Reader pull and payoff

Reader pull is unfinished desire under credible pressure. It can come from danger, choice, relationship, desire, discovery, consequence, competence, mystery, status, or an approaching collision. A chapter ending is strong when the reader can feel what changed and why the next action matters.

Payoff is not limited to spectacle. Useful forms include:

- an attempted task finally works, partly works, or fails in an informative way;
- a promised answer arrives but changes the question;
- competence becomes visible through consequence;
- a relationship grants or withdraws permission;
- an item, rule, clue, or earlier choice acquires practical value;
- pressure converts into a decision the character can no longer avoid;
- ordinary relief lands after sustained strain.

Track promise and delivery, not a numeric quota. Repeated escalation without local satisfaction creates reader debt; repeated satisfaction without renewed pressure creates drift. Do not force a cliffhanger after every chapter or inflate an ordinary uncertainty into apocalypse.

## 5. Signal, spoiler, and knowledge

Separate three layers:

1. **World truth** — what is actually happening.
2. **Author-only spoiler** — hidden explanation, future reveal, planned betrayal, or intended solution.
3. **Reader-visible signal** — the concrete discrepancy, behavior, absence, object, cost, or question present in the current chapter.

A useful signal is observable without explaining its final meaning. It changes attention or expectation now. Do not write reader reactions such as “the reader should suspect” into the outline; write what the text will make available.

Characters receive only information plausibly available to them. Reader knowledge, narrator knowledge, planner knowledge, and character knowledge remain separate.

## 6. Event and chapter budget

Before assigning chapter numbers, read `plot-and-pacing-engine.md`. Estimate an event by the movements readers must experience—not by importance labels or a fixed three-act percentage. Count necessary preparation, attempt, independent countermove, evidence or reinterpretation, relationship change, location or institutional process, decisive choice, and aftermath. Then apply both tests:

- **Expand** when compression would hide a choice, make opposition passive, turn earned knowledge into explanation, skip a relationship permission change, or erase practical aftermath.
- **Compress** when adjacent chapters repeat the same question, resistance, emotional conclusion, or state change; when a chapter exists only for travel, lore, training, or a hook; or when scenes can share one operative question.

A chapter usually carries one dominant movement and at most one supporting movement. Starting estimates are deliberately broad: a minor turn may occupy part of a chapter; a compact event one chapter; a developed event two to three; a complex sequence four to six; a mini-arc seven to twelve. Above that, name the internal phases and consider whether it is actually an arc. Record estimates and actual spans in `event-ledger.md`; record volume capacity and rolling pressure in `pacing-plan.md`.

Calculate capacity with `scripts/story_scale.py` when useful. For example, 1,000,000 Chinese characters at 3,000 characters per chapter is 334 chapter slots. That number is container capacity, not permission to stretch 180 chapters of causal material into 334.

## 7. Multi-chapter pacing

Pacing is pressure and consequence over time, not a preset percentage. Across a run of chapters, vary:

- mode: action, investigation, negotiation, training, travel, labor, recovery, intimacy, administration, or discovery;
- scale: body, relationship, household, institution, region, or world;
- certainty: attempt, partial answer, reversal, consolidation, or new question;
- emotional temperature and sentence density;
- who initiates and who pays.

Use rolling windows rather than judging one chapter in isolation: three chapters for immediate residue, eight to twelve for a short cycle, roughly twenty to forty for arc movement, then the whole volume and whole story. Look for repeated openings, identical confrontation shapes, uninterrupted escalation, delayed aftermath, unused supporting cast, promises without movement, or exposition disguised as lessons. Fix the causal pattern, not merely the chapter title or hook wording.

A volume should renew the central promise while changing its terms. End a volume with consequential settlement and a larger altered situation, not only a stronger enemy announcement.

## 8. Foreshadowing and open obligations

An open obligation needs:

- source unit and visible evidence;
- current state: `seeded`, `active`, `advanced`, `deferred`, `resolved`, `transformed`, or `abandoned`;
- who knows or misreads it;
- what kind of future answer it promises;
- next plausible pressure point, not a rigid due date;
- cost if ignored.

For planning and review, distinguish `must advance` because its due conditions are present, `eligible to resolve` because sufficient evidence and pressure exist, `sleeping` because no current condition calls it forward, and `stale debt` because the story has repeatedly promised movement while relevant actors unnaturally wait. These are diagnoses, not fixed chapter deadlines. Resolve, transform, defer honestly, or remove stale debt; do not mention the clue again and call that progress.

Mentioning an old clue is not advancement. Advancement changes knowledge, available action, cost, interpretation, or relationship. Do not seed more obligations than the story can keep distinct, and do not resolve a cluster of unrelated threads merely to make a volume look tidy.

## 9. Review and quality trend

Review a chapter in this order:

1. authority and continuity;
2. OOC and causal movement;
3. reader signal, payoff, and carried residue;
4. scene necessity and information delivery;
5. prose and dialogue evidence;
6. regression after repair.

Store only recurring, actionable trends in `quality-ledger.md`. A trend entry needs scope, evidence from accepted text or explicit author feedback, effect, attempted repair, and current state. Do not convert every review comment into a permanent prohibition.

Blocking issues include contradictory canon that changes the scene, impossible time or access, a decisive OOC action with no support, accidental spoiler exposure, and an accepted chapter whose state cannot be reconstructed. Stylistic preferences normally remain non-blocking unless the author marks them otherwise.

## 10. Settlement and projection

After acceptance:

1. append one compact entry to `unit-ledger.md`;
2. settle facts once in their natural domains;
3. update body, resource, location, item, knowledge, relationship, faction, and open-thread states where changed;
4. update `working-state.md` with the immediate unfinished action and relevant residue;
5. pass author feedback through the Core III learning gate;
6. update quality trends only when evidence warrants it;
7. mark superseded pending deltas rather than silently deleting their history.

Projection means updating derived current state from accepted events. A projection is not permission to invent an event that the chapter did not establish.

## 11. Query and recovery

For query, begin with the narrowest authoritative source. Return the answer, source pointer, status, and any material conflict. For relationship, system, faction, foreshadowing, or continuity questions, trace only the causal links needed.

For recovery after interruption:

1. scan the project and compare it with `source-map.md`;
2. identify the authoritative manuscript and last accepted ledger entry;
3. inspect unsettled or partially settled work;
4. rebuild current time, place, cast, body, resources, knowledge, relationships, and open pressure;
5. verify that working state follows the accepted manuscript;
6. resume from the unfinished action, not from a generic recap.

If the memory store is missing or unreliable, reconstruct from accepted manuscript and explicit author corrections. Report uncertainty; never fabricate a clean state.
