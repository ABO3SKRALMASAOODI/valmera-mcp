# AI interview editing: build a paper edit you can trace and revise

An interview can become shorter while its meaning becomes less accurate. A useful AI editing workflow keeps the question, the answer's scope and the source footage connected—even when the final video rearranges the conversation.

**Use Valmera to turn recorded interviews into a main story and separately reviewed clips.** Start with the [interview workflow](https://valmera.io/use-cases/interviews?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=interview_paper_edit), or connect a compatible assistant through the [setup guide](https://valmera.io/mcp/setup?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=interview_paper_edit). This companion gives you a worked paper edit, a correction example and a [copyable worksheet](INTERVIEW-REVIEW-WORKSHEET.md). It is an editorial planning method, not an executable edit file or a guarantee of the agent's output.

Published by Valmera · November 7, 2026. The recording, speakers and timings below are **fictional teaching data**, not a customer testimonial or a measured product run.

## Choose the deliverable before selecting quotes

| Deliverable | What the selection must do | What you review |
| --- | --- | --- |
| A shortened conversation | Keep enough questions and responses to follow the exchange | Whether a removed question changes what an answer appears to address |
| A story assembled from an interview | Connect a clear claim, its scope, evidence and next step | Whether rearrangement changes chronology or implies a new causal connection |
| A standalone social clip | Explain its subject without requiring the full interview | Whether the opening, caption and title preserve the answer's qualifications |
| An editable handoff | Preserve the structure the receiving editor needs | Whether the receiving application opens the required tracks, cuts and media |

An MP4 is not an editable timeline. Settle the required handoff before choosing a product or export route. A transcript can help locate a quote, but the recording settles words, tone, interruptions and who said them.

## Build a source ledger, then a paper edit

A **source ledger** records what is in the original files. A **paper edit** selects those moments and places them in a proposed story order. Keep both: the proposed order cannot replace the evidence of where a quote came from.

For each selection, record the source file, source in/out, verified speaker, exact words or a short locator phrase, and the context that must travel with it. Use source time until you have a preview; after rendering, add a separate preview-time column. Do not silently replace one clock with the other.

### Worked source ledger

Every interval here is start-inclusive and end-exclusive. The example uses one recording, `workshop-interview.mp4`, and straight cuts at normal speed. Real boundaries need listening and frame review; these invented times do not establish natural cut points.

| ID | Original source | Speaker | What the fictional passage says or establishes |
| --- | --- | --- | --- |
| Q | 00:00–00:08 | Host | Asks what the team learned from its small pilot |
| A | 00:10–00:26 | Guest | Says the new checklist reduced setup time for their three-person workshop team |
| B | 00:26–00:38 | Guest | Says they have not tested larger teams or measured long-term reliability |
| C | 00:40–00:52 | Guest | Describes the checklist; its first four seconds repeat an earlier explanation |
| D | 00:56–01:04 | Guest | Suggests a small trial with a recorded baseline before broader adoption |

The guest's claim is bounded by the pilot. A punchy title such as “This fixes setup for every team” would exceed the fictional interview, even if the selected words themselves were transcribed correctly.

### Main story, version 1

| Order | Selection | Duration | Planned program time | Editorial purpose |
| --- | --- | --- | --- | --- |
| 1 | Q: source 00:00–00:08 | 8 s | 00:00–00:08 | Establish the pilot question |
| 2 | A: source 00:10–00:26 | 16 s | 00:08–00:24 | State the observed benefit and team size |
| 3 | B: source 00:26–00:38 | 12 s | 00:24–00:36 | Preserve what the pilot did not establish |
| 4 | C: source 00:40–00:52 | 12 s | 00:36–00:48 | Explain the practical change |
| 5 | D: source 00:56–01:04 | 8 s | 00:48–00:56 | End with a bounded next step |

The planned program lasts **56 seconds**. This sum excludes titles, pauses, transitions or an appended end card. Record those separately if the actual export adds them.

### Standalone clip: the tempting cut and the better brief

Taking A alone produces a 16-second selection. It retains the small-team reference but loses the explicit limits about scale and reliability. For a clip presenting the pilot's conclusion, keep A and B together: **28 seconds**, with A at clip 00:00–00:16 and B at 00:16–00:28.

That is a proposed selection, not automatic approval. A and B are adjacent in the source, so listen through the A–B transition and the clip's opening and ending. Check whether the opening identifies the checklist. If it does not, include additional source context or add an accurate editorial label clearly distinguished from the speaker's words. Do not manufacture a new spoken sentence.

## Give the assistant a bounded editing brief

Use your own recording, actual speaker identities and verified source times. Do not paste the fictional filenames and ranges as though they describe your footage.

> Open [project and source file]. Make a [target length and format] interview story for [audience]. Use the attached source ledger as a proposal and verify its words, speakers and boundaries against the recording. Keep the question needed to understand the answer, the claim's scope and the stated limitations. Remove repetition where it does not change meaning. Do not invent speech or use a reaction from another moment to imply a response. Render a preview and identify the source selections used. Report anything you could not verify.

For a separate clip:

> Create a separate [format] clip from [verified source ranges]. Keep [qualification] with [claim]. Use the title “[accurate title]” only if the recording supports it. Check that the opening makes sense without the main interview. Preview this clip separately; approval of the main story does not approve the clip.

Valmera editing requires an eligible paid plan. An external assistant needs a supported, authorized connection and may have separate billing. Consult [current plans](https://valmera.io/subscribe) and the [client reference](CLIENTS.md) before starting. The worksheet itself requires no account.

## Carry one correction through the exports

Suppose the reviewer shortens C from source **00:40–00:52** to **00:44–00:52**, after confirming that the removed four seconds are redundant and the new opening still sounds natural.

| Item | Planned version 1 | Planned version 2 | Consequence |
| --- | --- | --- | --- |
| Q, A and B in main story | Program 00:00–00:36 | Program 00:00–00:36 | No timing change |
| C in main story | Program 00:36–00:48 | Program 00:36–00:44 | Four seconds removed from the start of C |
| D in main story | Program 00:48–00:56 | Program 00:44–00:52 | Starts four seconds earlier |
| A+B standalone clip | 00:00–00:28 | 00:00–00:28 | Selection and timing unchanged |

The main story becomes **52 seconds**. Captions inside C need remapping to its retained words; moving every caption by four seconds would damage the earlier sections. Later captions associated with D move earlier. The separate A+B clip does not inherit this timing change. See the [caption revision walkthrough](CAPTION-REVISIONS.md) for the underlying source-to-program mapping.

> In main-story preview [version], shorten only the explanation corresponding to original source [range]. Keep [retained words/action] and preserve all other approved story decisions. Re-render the main story, update its captions and identify the new version. The separate clip uses different source selections; do not replace it with the main-story export. Tell me which deliverables changed and which checks remain outstanding.

Keep the superseded export identifiable. A changed main-story filename is not proof that the separate clip, captions or thumbnail were updated correctly.

## Review picture, sound and meaning together

Watch each proposed join with sound. Preserve the speaker's intended emphasis and enough pause for the answer to land. Verify speaker labels against the actual voice and shot; overlapping speech can make transcript attribution uncertain. Check names, negations, numbers and conditional phrases in captions.

With two camera files, record their synchronization reference separately from the paper edit. Equal timecodes on two files do not by themselves establish synchronization. Inspect a shared visible-and-audible event, then another later event to check for drift. Review angle changes after cutting; a reaction shot should not falsely suggest a response to a different statement. The [interview workflow](https://valmera.io/use-cases/interviews#two-camera) includes a two-camera timing example.

For each delivery, record the project and preview version, export filename, program duration, total file duration, dimensions, branding and review outcome. A transcript review cannot confirm readable framing, intact audio or the actual ending of a rendered file.

## Take this into your next interview

Copy the [blank interview review worksheet](INTERVIEW-REVIEW-WORKSHEET.md), fill it with your source evidence, and bring the brief to [Valmera Studio](https://valmera.io/studio?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=interview_paper_edit) or your connected assistant. Keep the first preview's problems in the record even after a revision fixes them. That makes the next editing decision easier to assess.

For choosing an editor, use the broader [AI video editing agents guide](VIDEO-EDITING-AGENTS.md). For comparing basic cut, crop and revision behavior on the same sample, use the [evaluation kit](EDITOR-EVALUATION.md). Neither substitutes for testing your actual interview's speech, context and delivery requirements.
