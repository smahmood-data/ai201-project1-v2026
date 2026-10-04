# The Unofficial Guide

<!-- Replace this line with your name and which corpus you picked. -->

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Unit 1

## What This Does

This system answers questions about campus life using the `campus_life` corpus.
It retrieves relevant chunks from documents about deadlines, courses, housing,
jobs, dining, library services, and transportation. It then answers only when
the best retrieved chunk is close enough, names the source file, and refuses
questions that the corpus does not cover.

## Chunking Strategy

**Chunk size:** Up to 500 characters, split at blank-line paragraph boundaries.
**Overlap:** 0 characters.

The `campus_life` corpus contains 88 short posts, and the starter's 800-character
windows produced one chunk per document. I kept related paragraphs together when
they fit under 500 characters, but used paragraph boundaries so separate thoughts
are not cut in half. I chose no overlap because these short posts usually contain
complete thoughts within a paragraph; repeating text would add noise without
preserving necessary context.

<!-- What about YOUR documents made you pick these numbers? Short posts and
     long sectioned guides don't want the same chunking, and "800 seemed
     reasonable" earns nothing. Point at something you noticed when you read
     the documents in Milestone 1.

     If you changed your mind partway through, say so and say why. That's worth
     more than pretending you got it right first time.

     Milestone 3. -->

## Sample Chunks

<!-- Five chunks, pasted as text. Label each one and name the file it came from
     AND the function that produced it — the grader checks your code against
     what you claim here.

     `python app.py chunks -n 5` prints all three for you. Copy them straight
     across.

     Milestone 3. -->

**Chunk 1** — source: `admin_add_drop_deadline.txt` — produced by: `chunker.py::split_documents`

```
On the add/drop deadline

You can add a course through the end of the second week. Dropping is a longer window — through the end of week six — but a drop after week two shows as a W on your transcript. Nothing anywhere on the registrar's site says this plainly, and students find out from each other.
```

**Chunk 2** — source: `course_biol_160_exams.txt` — produced by: `chunker.py::split_documents`

```
BIOL 160 Cell Biology — assessment

Four unit tests and a cumulative final. Not curved.

The unit tests come fast, roughly every three weeks; falling behind once is very hard to recover from.
```

**Chunk 3** — source: `course_math_220_exams.txt` — produced by: `chunker.py::split_documents`

```
MATH 220 Linear Algebra — assessment

Two midterms and a cumulative final. Curved to a b- median.

The problem sets are the course; the lectures make sense afterwards rather than during.
```

**Chunk 4** — source: `dining_the_ridgeway_cafe.txt` — produced by: `chunker.py::split_documents`

```
The Ridgeway Café

Second-year here. Wait times: 10 to 15 minutes at 12:30, none after 2:00. The thing worth going for is the only place on campus with real espresso. The thing to know is that seating is tight; about 40 seats for a building of 900.

Hours are 7:00am to 4:00pm weekdays only. Costs declining balance only, no meal swipes.
```

**Chunk 5** — source: `housing_morrow_house.txt` — produced by: `chunker.py::split_documents`

```
Morrow House — what it's actually like

Just finished a year in this building. Built 1954, partially renovated 2008. Rooms are singles and doubles, hall bathrooms.

The good: cheapest housing tier by about $900 a year, and the singles are real singles.

The bad: known damp problem on the ground floor; two rooms were taken offline in 2024.

Laundry costs $1.50 wash, $1.25 dry, coin or card. On noise: loud until about 1am on weekends, no enforced quiet hours.
```

## Sample Answer

<!-- One complete question and answer, pasted as text, with the source line
     visible. Milestone 4. -->

**Question:** When is the deadline to drop classes?

**Answer:** You can drop a class through the end of week six. If you drop after week two, it shows as a W on your transcript.

**Source:** `admin_add_drop_deadline.txt`

The grounding prompt requires every factual claim to be supported directly by
the retrieved excerpts and requires the answer to name the specific source file.

```
```

**My relevance cutoff:**

<!-- The number you set in config.py, and how you got there.

     You ran five questions your corpus covers and the five in OUT_OF_SCOPE
     that it clearly doesn't, and wrote down the best distance for each. What
     did those two groups look like? Where was the gap? Put the actual numbers
     here — the table below wants all ten rows.

     Milestone 4. -->

| Question | In corpus? | Best distance |
|---|---|---|
| When is the deadline to drop classes? | Yes | 0.2973 |
| What are the library hours? | Yes | 0.3848 |
| Where is the best place to study at 9pm? | Yes | 0.6016 |
| How often does the campus shuttle run? | Yes | 0.4132 |
| How many hours can I work in the library or dining? | Yes | 0.2292 |
| What is the capital of Mongolia? | No | 0.8246 |
| How do I change the oil in a diesel engine? | No | 0.9340 |
| Who won the 1994 World Cup? | No | 0.8859 |
| What is the recommended dosage of ibuprofen for a headache? | No | 0.8442 |
| How do I write a for loop in Rust? | No | 0.8960 |

The in-corpus distances ranged from 0.2292 to 0.6016. The out-of-corpus
distances ranged from 0.8246 to 0.9340, leaving a gap between 0.6016 and
0.8246. I set the cutoff to 0.70, which lets all five in-corpus questions
through and refuses all five out-of-corpus questions in this test.

## How I Used AI

**1.** I wrote notes about the assignment requirements, my `campus_life`
documents, and what I wanted the chunks to do. I asked AI to check the project
and help implement the chunker. It suggested a paragraph-based strategy, but I
made the important choices: a 500-character limit, zero overlap, and keeping
related short paragraphs together. I ran the chunk preview and checked the
output myself, then made sure the README listed the real source files and
chunks.

**2.** I ran retrieval tests for the five questions I wrote and five questions
outside the corpus. AI helped collect and compare the distances, but I decided
the cutoff from the results: the in-corpus scores ended at 0.6016 and the
out-of-corpus scores started at 0.8246, so I chose 0.70. I also checked the
assembled grounding prompt and tightened it so answers must use direct support
from the excerpts and name the specific source file. The model answer call had
a network error, so I did not treat that as a successful answer test.

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 2 (revised). Answer contains the expected fact | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Sampled chunks are complete thoughts | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 5. Answer cites the document holding the fact | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |

Source: `results/run_2026-09-30_1725_before.md`, produced by `run_eval.py::main`
(retrieval by `store.py::search`, answers by `generate.py::answer_from_chunks`,
pass/fail by `scorer.py::judge`). Criteria 1, 3 and 4 are deterministic —
retrieval, the gate, and the chunker give the same result every run — so one
number goes in all three columns. Criterion 4 uses the five sample chunks
above from `chunker.py::split_documents`, which hasn't changed since they were
taken.

**Criteria 1, 2 and 5** — "How many hours can i work in the library or dining?", run 1:

```
Best distance: 0.2292 (passed the gate)
Sources retrieved: housing_aldridge_hall_noise.txt, housing_morrow_house_noise.txt, money_jobs.txt, study_group_rooms.txt, study_library_hours.txt

The maximum work limit is 20 hours a week during the term (money_jobs.txt).
```

The answer is in `money_jobs.txt` ("Maximum is 20 hours a week during term"),
which was retrieved (criterion 1), and the answer names it (criteria 2 and 5).

**Criterion 3** — `run_eval.py::check_out_of_scope`, cutoff 0.7, refused 5 of 5:

```
| What is the capital of Mongolia? | 0.825 | refused |
| How do I change the oil in a diesel engine? | 0.934 | refused |
| Who won the 1994 World Cup? | 0.886 | refused |
| What is the recommended dosage of ibuprofen for a headache? | 0.844 | refused |
| How do I write a for loop in Rust? | 0.896 | refused |
```

**Criterion 4** — sample chunk 1 from `chunker.py::split_documents`, source `admin_add_drop_deadline.txt`:

```
On the add/drop deadline

You can add a course through the end of the second week. Dropping is a longer window — through the end of week six — but a drop after week two shows as a W on your transcript. Nothing anywhere on the registrar's site says this plainly, and students find out from each other.
```

### Retest

I ran the same eval again with nothing changed (`python run_eval.py --label
retest`), mainly to measure the revised criterion 2 over a fresh set of
answers.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 2 (revised). Answer contains the expected fact | 4 of 5 | 5/5 | 4/5 | 4/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Sampled chunks are complete thoughts | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 5. Answer cites the document holding the fact | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |

Source: `results/run_2026-10-03_2248_retest.md`, produced by `run_eval.py::main`.

**Criterion 2 (revised)** — "What are the library hours", run 2, scored **fail** by `scorer.py::judge`:

```
Best distance: 0.3848 (passed the gate)
Sources retrieved: admin_library_holds.txt, housing_calder_annexe_noise.txt, housing_morrow_house_noise.txt, study_group_rooms.txt, study_library_hours.txt

The library is open until 2 am during term and until 10 pm during reading week (study_library_hours.txt, housing_morrow_house_noise.txt, and housing_calder_annexe_noise.txt).
```

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunk contains the answer | MET | For all five questions the document holding the answer was retrieved (`admin_add_drop_deadline.txt`, `study_library_hours.txt` twice, `transit_shuttle.txt`, `money_jobs.txt`). The run log lists sources, not chunk text; these posts are short and the fact sits in the opening paragraph, so the retrieved chunk contains it. |
| 2 | Every answer names a source | MET | All 15 answers name at least one `.txt` file. Not close. |
| 2 (revised) | Answer contains the expected fact | MET | Before: `scorer.py::judge` passed all five questions in all three runs. Retest: 5/5, 4/5, 4/5 — library hours failed runs 2 and 3. That's still 4 of 5 questions passing in every run, so it holds, but with zero margin. And both failures are the scorer's fault, not the system's (see Diagnoses), so I don't count them as evidence the system got worse. Revised in `criteria.md` because the original measured whether a citation existed, not whether the answer was right — see the reason there. |
| 3 | Gate stops out-of-corpus questions | MET | All five refused; the closest was 0.825 against a 0.7 cutoff. The tight spot is on the other side: the in-corpus "study at 9pm" question scored 0.6016, so the cutoff can't drop much below 0.6 without refusing it. |
| 4 | Sampled chunks are complete thoughts | MET | All five sample chunks start at a heading or paragraph start and end on a full sentence; none is cut mid-sentence. Splitting at blank lines is what guarantees this for these short posts. |
| 5 | Answer cites the document holding the fact | MET | Every answer cites the document containing the fact. Some also cite extra documents: drop-deadline answers add `admin_withdrawal_deadline.txt` (which does say "Dropping ends at week six"), and library-hours runs 1–2 add two `housing_*_noise.txt` files that support 2am but not 10pm. I counted "the right document is among those cited" — the closest call, because the criterion doesn't say how to treat extra citations. |

## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

No criterion was missed in either eval. The before eval was 5/5 everywhere.
The retest came within one question of a miss on the revised criterion 2.

**The near-miss: library hours, retest runs 2 and 3. Stage: evaluation (my
scorer), not the pipeline.** Both answers are correct and cite
`study_library_hours.txt`. They wrote "2 am" with a space, and
`scorer.py::judge` checks for the exact substring `2am` (case-insensitive
only), so it scored a right answer as wrong. Run 1 of the same question wrote
"2am" and passed. The model's spacing varies from run to run, and my scorer
can't tell the difference between a wrong answer and a differently formatted
one. The fix belongs in the scorer: normalise times ("2 am", "2 a.m.",
"2:00am" → "2am") before matching. Changing the `expects` wouldn't fix it,
because the next run could format it a third way.

**Apart from that, the targets were set low, and the pattern is the
questions, not the numbers.** Each of my five questions maps to one short document that states
the fact in its opening lines (`admin_add_drop_deadline.txt`,
`study_library_hours.txt`, `transit_shuttle.txt`, `money_jobs.txt`), so
retrieval and generation had almost nothing to get wrong. My out-of-scope
questions are just as easy in the other direction: the closest one scored
0.825 against a 0.7 cutoff, so the gate was never tested near its edge.

**The weak spots are still visible in the output, even though nothing failed:**

- **Generation drops half of two-part facts.** Every drop-deadline answer says
  "the end of week six" and none mention that a drop after week two shows as
  a W. My `expects` of `week six` can't catch that.
- **Generation over-cites.** Library-hours runs 1 and 2 cite two
  `housing_*_noise.txt` files for "2am during term and 10pm during reading
  week"; those files say 2am but never mention 10pm.
- **Retrieval is closer to the gate than it looks.** "Where is the best place
  to study at 9pm?" scored 0.6016, the only in-corpus question within 0.1 of
  the 0.7 cutoff.

**Which I'd tighten:** criterion 3. Keep the 4 of 5 target, but replace the
out-of-scope questions with near-misses that share vocabulary with my corpus —
e.g. "What are the hours of the downtown public library?" or "When is the drop
deadline at a different university?" That would show whether 0.7 really
separates the two groups, which the current questions can't.

## The Improvement

**What I changed:**

**Why I picked it:**

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->
