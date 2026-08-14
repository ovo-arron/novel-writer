# Plot Expansion and Pacing Engine

Use this reference when adding plot, deciding how much narrative space an event deserves, expanding or compressing a work of any length, budgeting a long serial, fixing rushed or padded sequences, planning parts/arcs/volumes, or mapping author-defined units.

## Contents

- [1. Units of plot](#1-units-of-plot)
- [2. Start from scale](#2-start-from-scale)
- [3. Event span estimator](#3-event-span-estimator)
- [4. Narrative-unit carrying capacity](#4-narrative-unit-carrying-capacity)
- [5. Expand or compress](#5-expand-or-compress)
- [6. Event-to-unit mapping](#6-event-to-unit-mapping)
- [7. Sequence, arc, part, and volume pacing](#7-sequence-arc-part-and-volume-pacing)
- [8. Rolling pacing windows](#8-rolling-pacing-windows)
- [9. Planning horizon](#9-planning-horizon)
- [10. Pacing audit](#10-pacing-audit)

## 1. Units of plot

| Unit | Owns | Ends when |
|---|---|---|
| Scene | continuous local attempt under resistance | place/time relation or operative objective changes |
| Event | one material change produced by actions and counter-actions | the central change occurs and creates residue |
| Sequence | several dependent events pursuing one near objective | the objective is achieved, lost, or redefined |
| Arc | recurring pressure transforms capability, relationship, identity, or institution | a choice creates a durable new condition |
| Part/installment/volume | a readable promise, campaign, period, or formal division | its central question or formal movement settles with larger residue |
| Story | the durable human pressure across the work | the central transformation receives its final answer |

Do not call a long campaign “one event” merely because it has one label. Split it into causally distinct events that can each change the next action. In a short story, several units may collapse into one scene; in a documentary novel, one unit may be a letter or record rather than a chapter.

## 2. Start from scale

For chaptered long fiction, use `scripts/story_scale.py` to calculate arithmetic only:

```powershell
python scripts/story_scale.py --total-characters 1000000 --characters-per-chapter 3000 --volumes 8 --json
```

One million Chinese characters at 3,000 per chapter produces about 334 chapters. Eight equal capacity bands produce roughly 41–42 chapters each. Those ranges are a planning canvas, not final volume boundaries. Move boundaries to consequential settlements.

When a target length or release schedule exists, plan two totals:

- **capacity total** — approximate author-defined units available from the length target;
- **committed plot total** — units currently justified by actual causal material.

Leave part of a long work's capacity uncommitted. New relationships, aftermath, discoveries, and necessary compression will change the later map. Filling every future unit on day one usually creates padding or forces characters to obey an obsolete outline. For short fiction, work from concentration and omission rather than capacity arithmetic.

## 3. Event span estimator

Begin with the smallest unit the form permits, then inspect the event's required movements. Add space only when the reader must experience a distinct change rather than receive a report.

Possible unit-bearing movements:

- preparation contains a choice, cost, or relationship negotiation;
- the first attempt tests a plan rather than merely approaching the real scene;
- an opponent makes an independent counter-move that changes available action;
- evidence must be encountered before it can be reinterpreted;
- a relationship grants, withdraws, or renegotiates permission;
- location, viewpoint, or institutional process changes what can happen;
- climax contains an irreversible choice;
- aftermath changes body, resources, public belief, duty, route, law, or future strategy.

For a serial using roughly 3,000-character chapters, these are starting estimates; other forms should translate the same movements into scenes, sections, letters, parts, or longer chapters:

| Shape | Likely span | Evidence required |
|---|---:|---|
| minor turn inside another chapter | part of 1 chapter | no independent setup or aftermath |
| compact event | 1 chapter | one main attempt/change, consequence can land immediately |
| developed event | 2–3 chapters | preparation/collision/aftermath or one meaningful counter-move |
| complex event sequence | 4–6 chapters | multiple altered plans, parties, settings, or reveal stages |
| mini-arc | 7–12 chapters | several distinct events transform a relationship, capability, or local order |
| larger than 12 chapters | arc/volume territory | split into named events and intermediate settlements |

These are starting estimates, not quotas. A 3,000-character chapter with dense dialogue may carry less external action and more relationship movement; a battle chapter may carry many actions but only one strategic change.

## 4. Narrative-unit carrying capacity

A readable scene, chapter, document, or section usually carries one dominant movement and zero or one supporting movement:

- dominant movement: the practical attempt, counter-move, discovery, choice, or aftermath that changes the exit state;
- supporting movement: relationship pressure, resource consequence, signal, or setup that directly alters the dominant movement.

Several scenes can belong in one chapter or part when they share the same operative question and causal direction. Split when a new scene needs a new objective, new information regime, emotional reset, formal source, or independent counter-move. Merge when two units leave the same state and one only repeats information or travel.

For roughly 3,000-character serial chapters, do not budget by equal percentages. In every form, reserve enough room for the decisive movement to be experienced and for at least one consequence to register. If setup consumes a unit and the state does not change, either make setup itself costly or combine it with the collision.

## 5. Expand or compress

### Expand when

- a decisive choice appears before pressure and alternatives are credible;
- a reversal arrives without the reader experiencing the failed plan;
- trust, fear, loyalty, competence, or status changes in one sentence despite needing interaction;
- a reveal needs evidence, wrong interpretation, and later reinterpretation;
- logistics, healing, training, investigation, travel, or institutional procedure creates meaningful choices;
- the climax changes several systems and its aftermath would alter later behavior.

### Compress when

- consecutive scenes preserve the same objective, belief, relationship, and resource state;
- a delay adds time but no new pressure, information, cost, or choice;
- several characters repeat the same explanation;
- preparation only inventories equipment or lore;
- each attempt fails for the same reason;
- an event exists only to reach a predetermined chapter count;
- aftermath repeats the emotional conclusion without changing action.

Compression options: summary bridge, enter later, combine messenger with decision, let preparation occur during conflict, or carry minor aftermath into the next event. Expansion options: restore missing counter-action, evidence stage, relationship negotiation, practical work, or consequential aftermath. Do not expand through decorative obstacles.

## 6. Event-to-unit mapping

For each planned event, write:

```text
Event change:
Why now:
Entry state:
Required movements:
Movements that can share a unit:
Movements that require separate experience:
Estimated span and uncertainty:
Unit-by-unit state change:
Exit residue:
Compression trigger:
Expansion trigger:
```

Example shape for a border evacuation:

1. **Evacuation order** — officers and families contest who leaves first; route and trust change.
2. **Road failure** — opponent or weather closes the easy route; the prior plan becomes unusable.
3. **Alternative crossing** — characters spend supplies or political legitimacy to move people.
4. **Arrival and count** — missing people, damaged medicine, rumors, and blame establish the next event.

This deserves four units only if each line contains a distinct decision and changed state. In a serial they may be chapters; in a standalone they may be scenes within fewer chapters. If the order is uncontested or the road failure has no strategic effect, compress it.

## 7. Sequence, arc, part, and volume pacing

A sequence should alternate attempts and altered conditions, not attempts and louder attempts. Give it at least one intermediate settlement so readers receive progress before the final result.

Track strategy memory between attempts: what method was tried, what value or self-image it protected, what it cost, what the character learned or refused to learn, and how the opposing actor or environment adapted. The next unit may repeat a behavior, but it cannot erase the body, resource, trust, knowledge, or public change already produced.

An arc needs:

- a starting behavior or condition under pressure;
- several tests that do not teach the same lesson;
- consequences that accumulate rather than reset;
- a choice the earlier character or institution could not make;
- residue that changes another arc.

In a long Chinese webnovel, a volume may often contain dozens of chapters, but causal settlement decides the boundary; a numeric range is a planning assumption, never a universal craft rule. A standalone may use untitled parts, a novella may use none, and an episodic series may settle one local promise per installment.

Within any major part, installment, or volume, maintain only what the form supports:

- one visible campaign or practical objective;
- two to four active arcs that collide rather than take turns occupying slots;
- local payoffs before the volume climax;
- an opponent timeline independent of protagonist appearances;
- a midpoint condition change, not merely a surprise;
- enough aftermath to make the settlement real.

## 8. Rolling pacing windows

Review different problems at different windows. For a serial, the examples below may map to chapters; for other forms, map them to recent scenes/documents, current sequence, current part, and whole work:

- **recent local units:** immediate continuity, repeated openings, whether each exit changes the next entry;
- **current sequence:** short promise/payoff movement, mode variety, supporting-cast use, repeated confrontation shape;
- **current part or long range:** arc movement, resource inflation, relationship transformation, opposition progress, unresolved debt;
- **whole part/volume/installment:** promise delivery, midpoint change when relevant, decisive choice, aftermath, inherited condition;
- **whole story:** growth scale, repeated premise, thematic pressure, power and setting inflation.

These windows diagnose patterns; they do not demand one fight, hook, or payoff at fixed intervals.

## 9. Planning horizon

Use rolling detail:

| Horizon | Detail |
|---|---|
| whole story | promise, major transformations, tentative scale, ending constraints |
| all major parts or installments | objectives, settlements, escalation of consequence; later divisions remain provisional |
| current part or sequence | event network, arcs, opposition timeline, time/resource logic |
| next medium-range units | dominant movements and dependency chain |
| next near-range units | concrete contracts, signals, payoffs, transitions |
| current scene or unit | entry state, choice, exit residue, prose risks |

After each accepted event, compare actual span with estimate. Move later ranges rather than padding or cutting an event to protect old numbering.

## 10. Pacing audit

Ask:

1. What state changes in each unit?
2. Which units repeat the same attempt or explanation?
3. Which event is rushed because a necessary movement was omitted?
4. Which event is padded because its outcome has already become inevitable?
5. Where did an opponent, institution, or relationship fail to answer?
6. Has a promise accumulated without a local payoff?
7. Has payoff occurred without renewed pressure?
8. Does aftermath affect later choices or only describe emotion?
9. Is a numeric quota driving events, or are event movements determining space?
10. What can be merged, moved offstage, or expanded through real consequence?
11. Which repeated attempt changed method, tolerated cost, relationship reliance, or definition of success—and which one merely changed scenery?

Return a revised event-to-unit map with reasons. Do not solve pacing by uniformly shortening chapters, adding cliffhangers, or inserting fights.
