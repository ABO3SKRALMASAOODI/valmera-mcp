# Speech-cleanup trial worksheet

Use this with the [filler-word and silence-removal guide](SPEECH-CLEANUP.md). Duplicate the blank sections for each editor or revision. This is a review aid, not a completed product benchmark. Choose a recording you are authorized to use, and apply the same scope to every candidate.

For a shared starting point, use the [four-second filler-word trial](SPEECH-CLEANUP.md#try-a-four-second-cut-before-you-trust-a-whole-interview). Save the first export before opening the reference. Fill out one row per pass so a successful repair does not hide a missed detection.

| Pass | What did the editor identify? | Did “like” and the onset of “use” survive? | Filename / revision |
| --- | --- | --- | --- |
| Description only | | | |
| Correction with source timestamps | | | |

## Delete one sentence and check the subtitle clock

Open the [free transcript cutter](https://valmera.io/free-ai-video-editor#free-trim). With the built-in four-second recording, select “Remove this passage and join the rest” and the first sentence, “I like the blue label.” Create the MP4 and download both the MP4 and the SRT. To test your own recording, open its video and a matching source SRT or VTT. The browser reads those local files. Hosted editing in Studio is a separate workflow.

| Check | Expected for this sample |
| --- | --- |
| Original range to remove | 0.200–1.450 seconds, a 1.250-second cut |
| Picture and sound that remain | Source 0.000–0.200 followed by 1.450–4.000, for a 2.750-second program |
| Point to audition | At output 0.200 the source clock jumps to 1.450. Listen through the pause into the correction. |
| Captions after the cut | One cue, “Um, use the green one for print.” Source 1.560–3.730 becomes output 0.310–2.480. |
| If a cue straddles the removal | Play the joined audio, revise the words and check both cue boundaries before delivery. Timing alone cannot identify the removed words. |

[Original video](https://valmera.io/examples/filler-word-cut/original.mp4) · [Original WebVTT](https://valmera.io/examples/filler-word-cut/original.vtt) · [Reference MP4](https://valmera.io/examples/filler-word-cut/first-sentence-removed.mp4) · [Reference SRT](https://valmera.io/examples/filler-word-cut/first-sentence-removed.srt)

To repeat the cut through a connected editing assistant, give it the original source range, ask for a preview that preserves the surrounding speech, then check the junction in the exported video. Check separately whether your delivery route can supply a subtitle sidecar. The free browser cutter can produce it from the matching timing file.

## Establish the source and brief

| Field | Your entry |
| --- | --- |
| Original file and duration | |
| Language, speakers and recording conditions | |
| Passage under review, in original-source time | |
| Editor, plan and date | |
| Project and starting version | |
| Exact cleanup request and actual settings | |
| Other changes bundled into the operation | |
| Output version and downloaded filename | |

Identify candidates by listening to the **original**, before seeing the tool's suggestions. Keep undecided cases separate. A transcript may omit the very hesitation you want to remove; missing text does not prove missing sound.

## Mark what should happen

| ID | Original-source interval and surrounding phrase | Intended decision: remove / preserve / undecided | Reason |
| --- | --- | --- | --- |
| A | | | |
| B | | | |
| C | | | |
| D | | | |

Use intervals precise enough to locate the sound, without pretending that rounded transcript timestamps are ideal cut boundaries. Preserve an original copy. If a passage contains an important correction, qualification, reaction or demonstration step, name it explicitly in the brief.

## Inspect the actual output

| ID | Actual action and returned source range | Program time / version reviewed | Sound and picture at the join | Caption result | Decision or repair |
| --- | --- | --- | --- | --- | --- |
| A | | | | | |
| B | | | | | |
| C | | | | | |
| D | | | | | |

Compare each proposed removal with its original context. Listen through both sides of the cut at normal speed. If a cut deletes several marked candidates, account for each candidate but count the resulting join only once. Record extra changes outside your original candidate list too.

## Count outcomes without hiding damage

| Measure | Count and evidence |
| --- | --- |
| Wanted removals identified before the test | |
| Wanted removals actually completed | |
| Wanted removals missed | |
| Protected candidates removed | |
| Other unexpected deletions or changes | |
| Unique joins reviewed / total joins created | |
| Reviewed joins with clipped speech, disruptive sound or lost visual action | |
| Undecided candidates and unreviewed joins | |
| Final runtime and whether the scope matched | |

**Fictional example:** an original passage contains eight unwanted hesitations and four protected candidates. An output removes seven unwanted hesitations and two protected candidates, leaving one unwanted hesitation and two protected candidates. Nine candidates were removed, but two deletions damaged the intended content. If those removals create nine distinct joins and two reviewed joins sound clipped, record that separately. The same deletion can both remove protected material and create a damaged join; do not add those counts into a single supposed error total. This example is arithmetic, not a Valmera result.

## Request and verify a focused repair

> Revise [output version]. Restore [verified source interval and phrase] in its original position. Keep the approved removals [IDs and source ranges]. Preserve speed, framing and the remaining source selection. Align captions to the repaired speech. Render another preview and identify any changes beyond this repair.

Record the version that actually contains the restored material. If a direct restoration is unavailable, return to a version containing that passage and reapply the approved cuts. Do not assume whole-pass undo preserves later edits.

| Delivery question | Evidence or unresolved issue |
| --- | --- |
| Was the protected meaning restored? | |
| Were approved edits retained? | |
| Were repaired joins and later captions reviewed? | |
| Was the entire downloaded file played? | |
| What remains unresolved? | |

A completed render is not approval. Keep the output unapproved if it removes required meaning or still has unresolved damaging cuts. When ready to try the workflow, [open Valmera Studio](https://valmera.io/studio?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=speech_cleanup_worksheet) or [connect an authorized assistant](https://valmera.io/mcp/setup). AI editing requires an eligible subscription; check [current plans](https://valmera.io/subscribe).
