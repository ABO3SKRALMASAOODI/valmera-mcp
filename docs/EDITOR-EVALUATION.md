# How to compare AI video editors: an edit-and-revise test

Compare the result you can download, the revision you can make, and the work it takes to get there. This kit gives you the same source file, starting brief, follow-up request and evidence sheet for every editor on your shortlist.

**Published by Valmera, a video editor included in the comparison.** This is a repeatable test procedure, not an independent ranking or a set of competitor results. The scorecard starts with every criterion marked **Not tested**.

[Download the test kit](https://github.com/ABO3SKRALMASAOODI/valmera-mcp/releases/tag/editor-evaluation-v1.0.0) · [Blank scorecard](evaluation/scorecard.csv) · [Machine-readable brief](evaluation/brief.json) · [Compare editing workflows](https://valmera.io/alternatives/best-ai-video-editors?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=editor_evaluation)

## What you can test with this footage

For one observed result using this procedure, see the [November 7 MCP run](MCP-RECORDED-EDIT.md). It includes source, first preview, revised final MP4, measured output properties and explicit untested criteria. It is a Valmera-authored example, not an independent comparison.

The supplied source is a 25-second, silent, 1280 × 720 motion-graphic video at 30 frames per second. It already contains its wording and animation. A short, unambiguous edit makes it possible to check source selection, crop, revision preservation and export continuity without arguing about taste.

Use this as a **basic editing check**. It does not test speech recognition, caption quality, noise removal, moving-person tracking, long projects, creative judgment or reliability across many runs. The real-footage extension below covers the next questions to ask.

The downloads include:

| File | Purpose |
| --- | --- |
| `original-source.mp4` | Identical input for every editor. |
| `brief.json` | Source ranges, output requirements and the revision target. |
| `scorecard.csv` | Blank evidence sheet; duplicate it for each editor and run. |
| `historical-valmera-export.mp4` | One recorded Valmera output from September 6, 2026. |
| `historical-evidence.json` | Provenance, file hashes, measurements and limitations of that historical output. |
| `SHA256SUMS.txt` | Integrity checks for the files in this release. |

The historical export is **17 seconds**: 12 seconds of edited program followed by an observed five-second end card. It includes an overlaid mark. This is an observation of that file, not a statement about today's plans or all Valmera exports. The source and export are also available on the [public example page](https://valmera.io/examples/trim-and-reframe).

## 1. Set up a fair comparison

Pick the workflow you would actually use: the editor's built-in chat, its timeline, or an assistant connected through MCP. Record the editor, plan, test date, device and, where relevant, assistant/model. Different assistants can make different decisions with the same editing tools.

Decide the required delivery before testing: square MP4, intact selected ranges, usable resolution, and your branding requirements. Record setup time separately from hands-on editing and waiting. Keep unsuccessful attempts and manual repairs in the record.

Use a fresh project and the same source file for each run. Preserve the original upload. If an editor needs manual timeline work, complete it and record those steps; that is useful evidence about the workflow.

## 2. Submit the same first edit

Upload `original-source.mp4`, then use this brief:

> Use the uploaded 25-second source. Keep source seconds 3–7, 12–16 and 19–23, in that order, at normal speed. Treat the end of each range as exclusive. Remove everything else. Make a 1:1 square video using a centered crop, without stretching the image. Do not add speech, music, captions, transitions or new footage. Show me a preview before final export.

The **edited program should be 12 seconds**, with three four-second sections. A platform-added end card, if any, is separate from the program. Record it separately instead of mistaking it for a failed cut or quietly excluding it from the delivery requirements.

| Original-source time | First-edit program time |
| --- | --- |
| 3–7 seconds | 0–4 seconds |
| 12–16 seconds | 4–8 seconds |
| 19–23 seconds | 8–12 seconds |

At 30 fps, these are source frames 90–209, 360–479 and 570–689: 360 program frames in total. If the editor changes frame rate, compare the selected moments and duration rather than treating a different frame count alone as a failure.

Watch the beginning, both joins and the final program frame. Check that cropping preserves proportions. Record the actual dimensions; a square preview does not prove that the downloaded file is square.

## 3. Make one revision in the existing project

After reviewing the first draft, use this follow-up:

> Revise the existing edit. Shorten only the middle section: keep original-source seconds 12–14 instead of 12–16. Leave the first section (source 3–7), last section (source 19–23), centered square crop, playback speed and audio unchanged. Render a revised preview. These timestamps refer to the original source, not the current preview.

Expected revised program:

| Original-source time | Revised program time |
| --- | --- |
| 3–7 seconds | 0–4 seconds |
| 12–14 seconds | 4–6 seconds |
| 19–23 seconds | 6–10 seconds |

The program is now **10 seconds**, or 300 frames if it remains 30 fps. The last section moves two seconds earlier but should contain the same source content. This distinguishes a correct revision from a new edit that happens to have the right overall length.

Keep both previews. If the editor changes another section, crop or audio, record the exact unintended change and the extra correction needed. Do not overwrite the first attempt's outcome with the eventual repaired result.

## 4. Inspect the downloaded file

Export the revised version and play the complete downloaded MP4 in a separate player. Check:

- The exported edit matches the approved revision, including both joins and the ending.
- The file has square dimensions and no stretched picture.
- No source section is missing, repeated or replaced.
- There is no audible sound; an encoded but silent audio track is different from added music.
- Branding, end cards, resolution and other delivery conditions meet the requirements you chose before testing.

Record the filename, export settings, program duration, total file duration and any branding. If an export fails or a plan blocks it, preserve that outcome in the scorecard. A preview is not a completed delivery.

For a technical check, `ffprobe` can report the actual streams and duration:

```sh
ffprobe -v error -show_entries stream=codec_type,codec_name,width,height,r_frame_rate -show_entries format=duration,size -of json revised-export.mp4
```

These measurements do not determine editorial quality. The full playback and source comparison remain necessary.

## 5. Record evidence instead of inventing a score

Use one copy of [scorecard.csv](evaluation/scorecard.csv) per editor/run. Change a status from `Not tested` to `Pass`, `Changes needed` or `Blocked` only after checking it. Keep names, timestamps and filenames in the evidence column. A blank observation is not a pass.

Example evidence **format**, not a reported product result:

> First preview, program 4.0 s: the next frame corresponds to source 12.0 s. Revised preview, program 6.0 s: final section still begins at source 19.0 s. Both downloaded files played through to the end.

Do not turn the rows into a percentage while some are untested. Treat essential failures—such as unavailable delivery or a meaning-changing cut in real footage—as decision points rather than averaging them away with cosmetic successes.

Record actual usage units and charges when available. If a bundled allowance prevents you from measuring per-edit cost, write that limitation. For a monthly workload, include setup, corrections, export attempts, extra applications and seats. The [editing budget calculator](https://valmera.io/tools/video-editing-cost-calculator) can help organize those assumptions; it does not measure your account for you.

## 6. Repeat with the footage you really edit

### Start with the shared speech trial

The [Sintel speech-trial worksheet](SPEECH-EDITOR-TRIAL.md) supplies one licensed source, three precise briefs and a blank results table for comparing caption presentation and a supplied Spanish subtitle revision while preserving the spoken recording.

It links two recorded Valmera examples with actual previews and exports. It separates the unchanged 9.6-second comparison from a later 9.4-second delivery revision. These are first-party observations on one animated-film excerpt, not competitor scores. The trial supplies the Spanish strings to every editor; it does not test translation generation.

### Then use your representative footage

Passing the short exercise establishes a narrow capability on one source. Before choosing a tool for ongoing work, add a representative recording and one difficult revision:

| Your work | Include in the source | Ask for a revision | Inspect closely |
| --- | --- | --- | --- |
| Interviews or podcasts | A qualification, a pause and a speaker change | Restore a phrase without undoing the rest of the cut | Meaning, word boundaries and speaker framing |
| Tutorials | A loading wait and a required setting | Shorten the wait while preserving the complete procedure | Readable controls, step order and final result |
| Social clips | A subject who moves and a key spoken name | Adjust framing and correct the name | Tracking throughout the shot and caption timing |
| Product demonstrations | A visible feature and a specific claim | Replace one supporting shot without changing the claim | Whether the picture demonstrates the actual claim |
| Team delivery | Your real export and handoff requirements | Reopen and change one approved section | Editable structure, relinking and delivery compatibility |

Use footage you have permission to share with each service. Repeat important cases across more than one run and keep failures, retries and manual work visible. Record what you tested and leave other capabilities unclaimed.

## Try the workflow with Valmera

For conversational editing, [connect your assistant](https://valmera.io/mcp/setup?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=editor_evaluation), upload the source and use the same brief above. Follow the current tool schemas and account requirements. Creating an account and uploading footage are free; editing requires an eligible subscription. Your assistant's access and billing are separate.

For your own recording, use the [editing brief builder](https://valmera.io/prompts?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=editor_evaluation#prompt-builder). Keep the resulting draft, revisions and downloaded delivery together so your decision rests on work you can inspect.
