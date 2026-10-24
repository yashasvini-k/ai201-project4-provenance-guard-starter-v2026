# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->

1. A writer submits text and a creator ID to POST /submit.

2. The route validates that the request contains non-empty text and a creator ID, and rejects text longer than 20,000 characters.

3. The model signal in detector.py::model_signal measures how predictable the text is to the GPT-2 language model.

4. The style signal in stylometry.py::style_signal measures sentence-length variation, vocabulary diversity, and punctuation density.

5. scoring.py::combine_signals combines the two signals using a weighted average.

6. scoring.py::score_to_label maps the combined score to human, unsure, or ai.

7. The decision and both signal scores are appended to the audit log. If the writer appeals, POST /appeal records the appeal as a separate entry and marks it under_review.

---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:** 
The model signal measures text predictability using GPT-2. The detector calculates perplexity and converts it to a score between 0 and 1, where a higher score indicates text that the model considers more predictable.

**Why that might differ between human and AI writing:**
AI-generated writing may resemble patterns that a language model predicts easily. However, human writing can also be conventional and predictable.

**What it can't see:**
It cannot establish who actually wrote the text or understand the writer's intentions. Plain, formal, or second-language writing may also be predictable and receive a misleading score.

### Signal two — the style signal

**What it measures:**
The style signal combines three text features: normalized sentence-length variation, type-token ratio (unique words divided by total words), and normalized punctuation density. Each feature is converted into an AI-like direction, and the three values receive equal weight.

**Why that might differ between human and AI writing:**
Generated text may have relatively consistent sentence lengths, repeated vocabulary, and conventional punctuation. More varied writing may produce a different feature profile.

**What it can't see:**
It cannot understand meaning or establish authorship. Text length, quotations, editing, typos, and deliberate changes to sentence structure can affect the measurements. These simple features have not been calibrated to establish reliable authorship probabilities.

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule:**
Take a weighted average of the model signal and style signal. Both signals use the same direction: higher means more AI-like. If they disagree, the weighted average falls between their scores instead of automatically trusting either signal.

**The numbers:**
* Model signal weight: 0.50
* Style signal weight: 0.50
* Formula: combined score = (0.50 × model score) + (0.50 × style score)
* Human threshold: 0.35
* AI threshold: 0.65

The combined score is a heuristic, not a calibrated probability that a person used AI.

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my two signals split, and what my rule does with it:**
In my sample run, the model score was 0.4395 while the style score was approximately 0.1882. The model signal was higher than the style signal. The equal-weight average was approximately 0.3138, which fell below the human threshold of 0.35. This demonstrates how the combining rule handles disagreement, but the resulting label is not proof of authorship.


---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|-------|-------------|------------------------------|
| high-confidence human | 0.00–0.35, inclusive | This text has features more consistent with human writing, although the result cannot establish authorship. |
| unsure | Above 0.35 and below 0.65 | We can't confidently distinguish AI-like from human-like writing in this text. This result is inconclusive. |
| high-confidence AI | 0.65–1.00, inclusive | This text has features associated with AI-generated writing, but this result is not proof of who wrote it. |

**Why I worded the "unsure" one this way:**
<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->
The unsure label communicates that the system cannot confidently distinguish between the two patterns. It avoids accusing the writer and acknowledges that the score is inconclusive.

---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

```bash
curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text":"I disagree. This approach seemed promising, but the results were inconsistent. I tested it again and found another problem!","creator_id":"unit7-test-user"}'
```

```json
{
  "content_id": "e6e733ea-2c64-4d49-a3de-6b3887704ac4",
  "guess": "human",
  "confidence": 0.3138410658289851,
  "label": "This text has features more consistent with human writing, although the result cannot establish authorship.",
  "model_score": 0.4395,
  "style_score": 0.18818213165797013,
  "combined_score": 0.3138410658289851
}


```

**An appeal**

```bash
curl -s -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id":"e6e733ea-2c64-4d49-a3de-6b3887704ac4","reasoning":"I wrote this text myself and would like the decision reviewed."}'
```

```json
{
  "content_id": "e6e733ea-2c64-4d49-a3de-6b3887704ac4",
  "message": "Your appeal has been recorded for review.",
  "status": "under_review"
}


```

**What the log shows afterwards**

```bash
curl -s "http://127.0.0.1:5000/log?limit=5"
```

The log contains two entries for this content ID: the original decision, followed by the appeal. The decision retains both signal scores, the combined score, the label, and its original decided status. The appeal is appended separately with status: "under_review" and the writer's reasoning.

```json

```

---

## How I Used AI

**Moment 1**

- *What I asked for:* Help implementing the three stylometry measurements and a combined style score.
- *What came back:* Python implementations using sentence-length variation, vocabulary diversity, punctuation density, and a normalized combined score.
- *What I changed:* I integrated the functions into my project and ran terminal tests to check their output.


**Moment 2**

- *What I asked for:* Help connecting the scoring functions to the Flask submission and appeal routes.
- *What came back:* A submission workflow that validates inputs, computes scores, assigns labels, and logs decisions, plus an appeal workflow.
- *What I changed:* I integrated the route implementations and tested a submission, an appeal, and the audit log.

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
