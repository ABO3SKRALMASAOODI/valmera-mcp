# Video background removal: trial and delivery worksheet

Use this alongside the [background-removal guide](VIDEO-BACKGROUND-REMOVAL.md). This is an empty review template, not a benchmark result, software test or universal quality score.

## Identify the intended result

- Project and approved source version:
- Source filename and permission to process it:
- Exact source interval and corresponding program interval:
- Subject and objects that must remain:
- Objects that should remain in front during occlusion:
- Required output: finished composite / transparent foreground / foreground plus matte:
- Intended replacement background, if any:
- Destination editor, browser or playback environment and version:
- Speech, music and other audio that must remain:
- Cuts, speed, captions and framing that must remain:

## Choose representative moments

Use events present in your actual footage. If an event is absent, mark it untested; do not report a pass.

| Event | Source time | Program time | What must survive | Reviewed result |
| --- | --- | --- | --- | --- |
| Relatively still subject |  |  | Hair, shoulder, fine boundary |  |
| Fast turn or gesture |  |  | Fingers, motion blur, stable outline |  |
| Held object |  |  | Microphone, product or prop and its gaps |  |
| Occlusion or exit/re-entry |  |  | Correct foreground order and recovery |  |
| Shot change, if included |  |  | Correct subject after the cut |  |

## Record processing conditions

- Provider, tool and date:
- Exact settings and any chosen model:
- Actual local/cloud route and relevant upload consent:
- Displayed price or credit estimate before processing:
- Job identifier and start/completion time:
- Any length limit, frame sampling or resolution reduction:
- Failed, queued or incomplete operations:
- Manual correction required and time spent:

Do not treat a queued job as a completed result. Record an existing job before retrying an uncertain submission, so the review does not create duplicate processing charges.

## Inspect the downloaded deliverable

| Check | Exact file and environment | Observation / evidence | Unresolved item |
| --- | --- | --- | --- |
| Foreground over a light background |  |  |  |
| Same foreground over a dark background |  |  |  |
| Intended destination background |  |  |  |
| Full passage at normal playback speed |  |  |  |
| Difficult consecutive frames |  |  |  |
| Separate matte alignment, if used |  |  |  |
| Alpha interpretation, if applicable |  |  |  |
| Audio presence and playback |  |  |  |
| Duration, dimensions and frame cadence |  |  |  |
| Branding, end card or export restriction |  |  |  |

Changing the lower background should change the empty area around a transparent subject. A visible checkerboard that stays fixed may be part of the pixels. A dark rectangle can also result from an importer that ignores alpha: distinguish that from missing transparency before blaming the mask.

## Log precise corrections

| File version | Time range | Observed problem | Requested change | New file and replay observation |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

Example wording, not a measured result: “At 4.2–4.5 seconds, the right hand disappears during the gesture. Retain the hand and review the same passage over the destination background.” Avoid replacing the original evidence with the corrected file; retain both identities for comparison.

## Handoff

- Delivered filenames, optional hashes and version:
- Container, codec/preset and alpha interpretation:
- Matching matte filename and timing, if separate:
- Audio included or deliberately omitted:
- Destination import test and reviewer:
- Remaining defects with timecodes:
- Untested cases:
- Decision: usable for this destination / needs correction / incompatible delivery / processing incomplete:

Keep visual quality, format compatibility, cost and elapsed time separate. A fast output with unusable transparency has not met an alpha-delivery brief, and a clean still frame does not establish stable motion.
