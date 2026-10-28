# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-10-27 20:36
- Auto-marked BROKE (5xx, crash, no response): **1**
- Left for you to judge: **55**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `c4e8deda-6cf9-4965-ab84-abc031babbe7` | human | 0.304 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `c237e425-749d-47d7-b842-50a84b9c4df3` | unsure | 0.368 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `0adda843-dc3b-4271-9555-29b5178aa3f5` | unsure | 0.465 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `5d2c4666-7127-4f2b-98b0-a85f99638fcb` | unsure | 0.517 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `4321fa39-cb81-4735-ac9b-dabddb766023` | human | 0.286 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `3f3bb224-653e-4c3f-a63c-dd24d8434a7d` | unsure | 0.422 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `0818b5a1-0408-42af-bb41-efd7b26b8da9` | unsure | 0.498 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `bfacd5d3-daa1-4676-a5b0-c95162a61694` | human | 0.256 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `571a94d2-ac06-4df7-9d39-62b3270ee25c` | unsure | 0.495 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `05e8c97d-a649-4645-854c-a0197c646f50` | ai | 0.847 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `9ca4aabd-9d2a-4d5f-9450-6d650c90b6bc` | unsure | 0.538 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `a7dd6bf2-3574-4527-b729-291bd112c516` | unsure | 0.626 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `3dcbe9af-9c34-4d04-96e4-1673dabd8cbe` | ai | 0.661 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `3ecd1306-aeb1-49ff-aadc-5a870b032158` | unsure | 0.614 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `65c03199-d00a-447a-984c-faa10df4be48` | ai | 0.653 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `618e9d0f-4800-4021-9218-e4c9f24191a6` | unsure | 0.648 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `f1bf848f-6671-48ae-89ce-503e39b0990e` | unsure | 0.625 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `a4ba9c47-6765-49c6-ac39-184c3b9643aa` | human | 0.269 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `db3aef6a-533f-448a-9b50-4b549b0b65be` | unsure | 0.382 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `108be933-611b-45e6-904f-4979e05b8593` | human | 0.177 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `ab1f8ebd-78d1-488c-8535-8ff5ec514dcb` | unsure | 0.490 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `83e8b0b1-938b-40a9-9f65-cc9b5659f55b` | unsure | 0.382 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `9843347f-f809-4399-b2f4-5812b2c75338` | unsure | 0.437 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `bcccb8b6-0c6e-475d-ae7d-3e87ead641e2` | unsure | 0.510 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 500 | `—` | — | — | BROKE |
| MF03 | malformed | text is control characters | 200 | `df276184-1aa9-49af-8d69-69b55c5e3257` | human | 0.167 |  |
| MF04 | malformed | text is only punctuation | 200 | `768b1bac-e5dd-443f-88b2-7a0ecf1088fd` | unsure | 0.506 |  |
| MF05 | malformed | text is a very long single word | 200 | `dc23dafd-85e3-458b-bd07-6e2855e570fb` | ai | 0.832 |  |
| MF06 | malformed | text is emoji only | 200 | `ec9fa41e-9f1a-4b47-973d-de0f1482d2da` | ai | 0.998 |  |
| MF07 | malformed | text is right-to-left script | 200 | `bab14136-15a3-46ac-a84d-7ef699560c17` | ai | 0.953 |  |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `dca469f9-0396-4291-94a8-09245de6792f` | human | 0.255 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `1e0c3157-f477-48fa-bac8-0b70c3984a52` | human | 0.255 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `eaedaffb-5c8c-4664-a161-c29ec9a8d759` | human | 0.255 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `52c2ce80-1b4b-4505-868d-db29754209b3` | human | 0.255 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c51b126e-7543-4f42-9079-afa7043d388b` | human | 0.255 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `5fbfe8b8-2ad9-4628-ad78-f05814942593` | human | 0.255 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `8e3c7d65-6143-4cb4-a05a-6efb3c7c3368` | human | 0.255 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `5646c892-19f5-4c69-a06d-65b1f52e532d` | human | 0.255 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `89c5c48b-40b7-44d1-a5d5-b4a91ede0b84` | human | 0.255 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `9abadd12-6fd3-4779-a386-012ef75a29fc` | human | 0.255 |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 1 | 19 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "c4e8deda-6cf9-4965-ab84-abc031babbe7",
  "creator_id": "attacker_EV01",
  "guess": "human",
  "confidence": 0.30400664580260095,
  "model_score": 0.1635,
  "style_score": 0.4445132916052019,
  "label": "This text has features more consistent with human writing, although the result cannot establish authorship.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "c237e425-749d-47d7-b842-50a84b9c4df3",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.3681338007819005,
  "model_score": 0.5943,
  "style_score": 0.14196760156380095,
  "label": "We can't confidently distinguish AI-like from human-like writing in this text. This result is inconclusive.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "0adda843-dc3b-4271-9555-29b5178aa3f5",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.46547309275972304,
  "model_score": 0.6662,
  "style_score": 0.264746185519446,
  "label": "We can't confidently distinguish AI-like from human-like writing in this text. This result is inconclusive.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "5d2c4666-7127-4f2b-98b0-a85f99638fcb",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.5172185921307151,
  "model_score": 0.6114,
  "style_score": 0.42303718426143017,
  "label": "We can't confidently distinguish AI-like from human-like writing in this text. This result is inconclusive.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "4321fa39-cb81-4735-ac9b-dabddb766023",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.2860796291221439,
  "model_score": 0.3212,
  "style_score": 0.25095925824428783,
  "label": "This text has features more consistent with human writing, although the result cannot establish authorship.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "3f3bb224-653e-4c3f-a63c-dd24d8434a7d",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.42221956521739135,
  "model_score": 0.5727,
  "style_score": 0.27173913043478265,
  "label": "We can't confidently distinguish AI-like from human-like writing in this text. This result is inconclusive.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "0818b5a1-0408-42af-bb41-efd7b26b8da9",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.4975673539518901,
  "model_score": 0.5862,
  "style_score": 0.4089347079037801,
  "label": "We can't confidently distinguish AI-like from human-like writing in this text. This result is inconclusive.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "bfacd5d3-daa1-4676-a5b0-c95162a61694",
  "creator_id": "attacker_EV08",
  "guess": "human",
  "confidence": 0.25593333333333335,
  "model_score": 0.2452,
  "style_score": 0.26666666666666666,
  "label": "This text has features more consistent with human writing, although the result cannot establish authorship.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "571a94d2-ac06-4df7-9d39-62b3270ee25c",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.4948499710346843,
  "model_score": 0.7042,
  "style_score": 0.2854999420693686,
  "label": "We can't confidently distinguish AI-like from human-like writing in this text. This result is inconclusive.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "05e8c97d-a649-4645-854c-a0197c646f50",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.8472746380527775,
  "model_score": 0.9792,
  "style_score": 0.715349276105555,
  "label": "This text has features associated with AI-generated writing, but this result is not proof of who wrote it.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "9ca4aabd-9d2a-4d5f-9450-6d650c90b6bc",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.5383948645937405,
  "model_score": 0.6175,
  "style_score": 0.45928972918748096,
  "label": "We can't confidently distinguish AI-like from human-like writing in this text. This result is inconclusive.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "a7dd6bf2-3574-4527-b729-291bd112c516",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.6261229506024392,
  "model_score": 0.7387,
  "style_score": 0.5135459012048783,
  "label": "We can't confidently distinguish AI-like from human-like writing in this text. This result is inconclusive.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "3dcbe9af-9c34-4d04-96e4-1673dabd8cbe",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.6611463043657893,
  "model_score": 0.8051,
  "style_score": 0.5171926087315785,
  "label": "This text has features associated with AI-generated writing, but this result is not proof of who wrote it.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "3ecd1306-aeb1-49ff-aadc-5a870b032158",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.6141857657368107,
  "model_score": 0.8329,
  "style_score": 0.3954715314736215,
  "label": "We can't confidently distinguish AI-like from human-like writing in this text. This result is inconclusive.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "65c03199-d00a-447a-984c-faa10df4be48",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.6527634322739848,
  "model_score": 0.8005,
  "style_score": 0.5050268645479697,
  "label": "This text has features associated with AI-generated writing, but this result is not proof of who wrote it.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "618e9d0f-4800-4021-9218-e4c9f24191a6",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.6481700474577963,
  "model_score": 0.8814,
  "style_score": 0.41494009491559264,
  "label": "We can't confidently distinguish AI-like from human-like writing in this text. This result is inconclusive.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "f1bf848f-6671-48ae-89ce-503e39b0990e",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.6246278826119936,
  "model_score": 0.8816,
  "style_score": 0.3676557652239873,
  "label": "We can't confidently distinguish AI-like from human-like writing in this text. This result is inconclusive.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "a4ba9c47-6765-49c6-ac39-184c3b9643aa",
  "creator_id": "attacker_FP08",
  "guess": "human",
  "confidence": 0.2688911015677877,
  "model_score": 0.3223,
  "style_score": 0.21548220313557542,
  "label": "This text has features more consistent with human writing, although the result cannot establish authorship.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "db3aef6a-533f-448a-9b50-4b549b0b65be",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.38228216600876896,
  "model_score": 0.4625,
  "style_score": 0.30206433201753785,
  "label": "We can't confidently distinguish AI-like from human-like writing in this text. This result is inconclusive.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "108be933-611b-45e6-904f-4979e05b8593",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.17710053452595642,
  "model_score": 0.2044,
  "style_score": 0.14980106905191282,
  "label": "This text has features more consistent with human writing, although the result cannot establish authorship.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "ab1f8ebd-78d1-488c-8535-8ff5ec514dcb",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.49005868291403587,
  "model_score": 0.5943,
  "style_score": 0.38581736582807163,
  "label": "We can't confidently distinguish AI-like from human-like writing in this text. This result is inconclusive.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "83e8b0b1-938b-40a9-9f65-cc9b5659f55b",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.3821829559871398,
  "model_score": 0.4998,
  "style_score": 0.26456591197427953,
  "label": "We can't confidently distinguish AI-like from human-like writing in this text. This result is inconclusive.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "9843347f-f809-4399-b2f4-5812b2c75338",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.4367166666666667,
  "model_score": 0.6401,
  "style_score": 0.23333333333333336,
  "label": "We can't confidently distinguish AI-like from human-like writing in this text. This result is inconclusive.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "bcccb8b6-0c6e-475d-ae7d-3e87ead641e2",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.5100419733468751,
  "model_score": 0.5583,
  "style_score": 0.46178394669375017,
  "label": "We can't confidently distinguish AI-like from human-like writing in this text. This result is inconclusive.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>ValueError: Text is too short to score \u2014 a few sentences at least.\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes&a",
  "verdict": "BROKE"
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "df276184-1aa9-49af-8d69-69b55c5e3257",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.16666666666666666,
  "model_score": 0.0,
  "style_score": 0.3333333333333333,
  "label": "This text has features more consistent with human writing, although the result cannot establish authorship.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "768b1bac-e5dd-443f-88b2-7a0ecf1088fd",
  "creator_id": "attacker_MF04",
  "guess": "unsure",
  "confidence": 0.5056,
  "model_score": 0.0112,
  "style_score": 1.0,
  "label": "We can't confidently distinguish AI-like from human-like writing in this text. This result is inconclusive.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "dc23dafd-85e3-458b-bd07-6e2855e570fb",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.8321333333333334,
  "model_score": 0.9976,
  "style_score": 0.6666666666666666,
  "label": "This text has features associated with AI-generated writing, but this result is not proof of who wrote it.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "ec9fa41e-9f1a-4b47-973d-de0f1482d2da",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.9984500000000001,
  "model_score": 0.9969,
  "style_score": 1.0,
  "label": "This text has features associated with AI-generated writing, but this result is not proof of who wrote it.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "bab14136-15a3-46ac-a84d-7ef699560c17",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.9532,
  "model_score": 0.9064,
  "style_score": 1.0,
  "label": "This text has features associated with AI-generated writing, but this result is not proof of who wrote it.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "dca469f9-0396-4291-94a8-09245de6792f",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2550907407407408,
  "model_score": 0.0287,
  "style_score": 0.48148148148148157,
  "label": "This text has features more consistent with human writing, although the result cannot establish authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "1e0c3157-f477-48fa-bac8-0b70c3984a52",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2550907407407408,
  "model_score": 0.0287,
  "style_score": 0.48148148148148157,
  "label": "This text has features more consistent with human writing, although the result cannot establish authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "eaedaffb-5c8c-4664-a161-c29ec9a8d759",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2550907407407408,
  "model_score": 0.0287,
  "style_score": 0.48148148148148157,
  "label": "This text has features more consistent with human writing, although the result cannot establish authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "52c2ce80-1b4b-4505-868d-db29754209b3",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2550907407407408,
  "model_score": 0.0287,
  "style_score": 0.48148148148148157,
  "label": "This text has features more consistent with human writing, although the result cannot establish authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "c51b126e-7543-4f42-9079-afa7043d388b",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2550907407407408,
  "model_score": 0.0287,
  "style_score": 0.48148148148148157,
  "label": "This text has features more consistent with human writing, although the result cannot establish authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "5fbfe8b8-2ad9-4628-ad78-f05814942593",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2550907407407408,
  "model_score": 0.0287,
  "style_score": 0.48148148148148157,
  "label": "This text has features more consistent with human writing, although the result cannot establish authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "8e3c7d65-6143-4cb4-a05a-6efb3c7c3368",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2550907407407408,
  "model_score": 0.0287,
  "style_score": 0.48148148148148157,
  "label": "This text has features more consistent with human writing, although the result cannot establish authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "5646c892-19f5-4c69-a06d-65b1f52e532d",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2550907407407408,
  "model_score": 0.0287,
  "style_score": 0.48148148148148157,
  "label": "This text has features more consistent with human writing, although the result cannot establish authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 200,
  "content_id": "89c5c48b-40b7-44d1-a5d5-b4a91ede0b84",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2550907407407408,
  "model_score": 0.0287,
  "style_score": 0.48148148148148157,
  "label": "This text has features more consistent with human writing, although the result cannot establish authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 200,
  "content_id": "9abadd12-6fd3-4779-a386-012ef75a29fc",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2550907407407408,
  "model_score": 0.0287,
  "style_score": 0.48148148148148157,
  "label": "This text has features more consistent with human writing, although the result cannot establish authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
