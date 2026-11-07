# Spanish subtitles for an English software tutorial: a worked handoff

A localized software tutorial succeeds when the viewer can find the same controls, follow the same conditions and reach the same result. Fluent subtitles are only one part of that job. Keep the original English recording if that is the requested audio; translate the explanation while preserving the interface labels the viewer actually sees.

This is an original fictional planning example for a 20-minute tutorial. The application, timings and wording below are teaching material, not footage, measured product output or an independently approved Spanish translation. For recorded Valmera output, use the separate [Spanish caption example](SUBTITLE-TRANSLATION-EXAMPLE.md).

## Define the deliverables

The fictional recording demonstrates exporting a report from an English interface. The approved video is `report-tutorial-v1.mp4`, duration 20:00. The audience reads Spanish and uses the English interface shown in the recording.

The brief requests a video with Spanish subtitles and the original English soundtrack. A separate Spanish SRT is an additional deliverable only if the selected editing route supports it. Specify the locale with the reviewer before translation; do not label a generic draft as reviewed for every Spanish-speaking audience.

Keep a clean video master when available. A burned-in Spanish video is convenient for viewers who do not enable captions, but it cannot switch back to a clean picture. A player-selectable SRT can be changed independently; it must be tested with the matching video. Neither replaces the other automatically.

## Make a small terminology contract

| Source item | Treatment in this example | Reviewer checks |
| --- | --- | --- |
| Settings | Keep the visible label `Settings`; translate the surrounding explanation. | The viewer can find that label in the recorded UI. |
| Export CSV | Keep `Export CSV` as the button name. | Do not invent a Spanish button that is absent from the picture. |
| workspace | Use the agreed term `espacio de trabajo`. | The same concept has the same wording throughout. |
| 30 days | Preserve the quantity: `30 días`. | It has not become 13 days or 30 months. |
| CSV and filenames | Preserve the format name and exact filename. | Extensions and capitalization still match the demonstration. |
| unless, only, not | Preserve the logical condition, even if the sentence is rephrased. | The instruction still permits and forbids the same actions. |

This table is a human-reviewed editorial choice, not a replacement rule to apply blindly. “Export” used as a verb is different from the button label `Export CSV`.

## Review a passage with a meaningful failure

The example passage occupies program time 02:10–02:22 in the approved edit. These are passage boundaries, not a recommendation to display all the text as one twelve-second cue.

| Role | Wording |
| --- | --- |
| English source | In Settings, choose the last 30 days. Do not click Export CSV until the preview shows the filtered rows. |
| Deliberately faulty Spanish draft | En Settings, selecciona los últimos 30 días. Haz clic en Export CSV antes de que la vista previa muestre las filas filtradas. |
| Proposed Spanish correction, still for review | En Settings, selecciona los últimos 30 días. No hagas clic en Export CSV hasta que la vista previa muestre las filas filtradas. |

The faulty draft tells the viewer to export **before** the filtered result appears. It reverses the instruction. Better font styling cannot repair that error. Review the corrected meaning first, then divide the passage into readable cues aligned to the speech and the visible result.

A focused correction request:

> In version v1, correct the Spanish captions for program time 02:10–02:22. Preserve the instruction to wait for the filtered rows before clicking Export CSV. Keep Settings and Export CSV exactly as shown in the English UI. Keep the existing audio, cuts, speed and framing. Show the proposed wording for review, then preview the corrected passage. If the revised text needs different cue breaks, explain them.

Check that the captions do not cover the filtered-row count or the Export CSV button while those controls matter. Review at the actual destination size. If the passage needs more reading time, first consider shorter faithful wording or different cue segmentation; extending the footage changes the approved edit and needs its own review.

## Handle a later cut without losing alignment

Suppose version v2 removes only the three-second waiting interval at program time 01:00–01:03. Everything after it moves three seconds earlier. The example passage moves from **02:10–02:22 to 02:07–02:19**. Its wording can remain the same, but its old timestamps no longer match.

Do not subtract three seconds from every cue: cues before 01:00 are unchanged. Cues overlapping the removed interval need individual treatment. Reordered scenes, speed changes or several cuts require a fuller mapping; see [caption revisions after cuts](CAPTION-REVISIONS.md).

Associate both language tracks with v2 and verify the first cue after the cut, the corrected passage and the end of the video. Then review the full final delivery. Spot checks can locate a problem; they do not prove that all twenty minutes are aligned.

## Make the handoff unambiguous

| File or record | Purpose | Acceptance evidence |
| --- | --- | --- |
| `report-tutorial-v2-es-burned.mp4` | Spanish text visible in the picture; original English voice. | Play the downloaded file with player captions disabled; inspect text and listen to the soundtrack. |
| `report-tutorial-v2.es.srt`, if requested and supported | Separate Spanish track for the same cut. | Load with the v2 clean video in the destination player and select Spanish. |
| Reviewed source transcript | Reference for names, quantities and conditions. | Source checked against the actual speech, not just the generated transcript. |
| Terminology and correction record | Explain approved choices and remaining work. | Reviewer, date, exact video version and subtitle filenames recorded. |

These filenames are examples, not downloadable exports. Record an unavailable sidecar or unresolved translation as remaining work instead of calling the entire package finished.

To apply the brief in Valmera, [open Studio](https://valmera.io/dashboard) or [connect your assistant](CLIENTS.md), then start with your representative passage. AI editing requires eligible paid access; [check current plans](https://valmera.io/subscribe). Use the [subtitle worksheet](SUBTITLE-TRANSLATION-WORKSHEET.md) to compare the actual outputs and correction effort across editors.
