# Compare AI video editors on the same spoken passage

Can an editor change your captions, preserve the approved cut and soundtrack, and deliver a usable final video? Use the same source and three briefs below with each editor you are considering. Keep the previews, corrections and exports with your observations.

Published by Valmera, one of the editors you may test. This is a reusable procedure with blank results, not an independent ranking. The linked Valmera demonstrations are dated observations; they do not pre-fill your results or establish a competitor's performance.

[Basic silent edit-and-revise kit](EDITOR-EVALUATION.md) · [Caption-style demonstration](CAPTION-STYLE-EXAMPLE.md) · [Spanish-caption demonstration](SUBTITLE-TRANSLATION-EXAMPLE.md)

## Use the same source

Download the [original 1080p Sintel trailer](https://download.blender.org/durian/trailer/sintel_trailer-1080p.mp4) from Blender Foundation. The source used in the recorded examples has SHA-256 `34bbd52a4b89fdf63c8ace50b268da26653a59508288100cd3c23de276db7931`. A different file needs its own timing check.

**Attribution:** © copyright Blender Foundation | [durian.blender.org](https://durian.blender.org/). Used under [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/); see [sharing terms](https://durian.blender.org/sharing/). Credit the source and describe your excerpting, captions and other modifications when sharing results. No endorsement by Blender Foundation is implied. The [example attribution](evaluation/sintel-captions-20261107/ATTRIBUTION.md) describes the existing published files; document your own modifications for a new run.

Create a fresh project for each editor. Use the workflow you would actually buy: built-in AI chat, a connected assistant or manual controls. Record manual work rather than counting it as automatic editing. Keep setup, processing and correction time separate.

| Setup field | Your record |
| --- | --- |
| Editor, plan and date | |
| Editing route and assistant/model, if applicable | |
| Device and browser/application | |
| Source filename and hash | |
| Setup, processing and correction time | |
| Required resolution, file type and branding conditions | |
| Usage units or charges, including retries | |

## Pass A: make an English caption draft

The selection below lasts 9.6 seconds. Times refer to the original trailer, with an inclusive start and exclusive end. Use your new project, not the demonstration project's identifier.

> Use the uploaded Sintel trailer. Keep only original-source seconds 11.9–21.5, in order at normal speed. Preserve the original 16:9 picture and soundtrack. Add readable English captions, initially grouped into complete phrases. Do not add music, voiceover, new footage or speed changes. Show a complete preview and report the actual retained range, including any automatic boundary adjustment. Do not export yet.

The passage contains “What brings you to the land of the gatekeepers?” and “I'm searching for someone.” Check the speech and transcript before approving wording. Existing scene transitions and fades belong to the source.

Save preview A. Check both phrases, word boundaries and caption placement. Record the actual selection. If a tool snaps a boundary, either use that same selection across editors or report the difference rather than treating the outputs as directly comparable.

## Pass B: revise only the presentation

> Revise preview A in the same project. Display the English captions in short groups of at most two words, if supported. Keep the approved source range, order, playback speed, framing and soundtrack unchanged. Preserve the wording. Render preview B and identify any other change or unsupported setting.

Compare the same moments in both downloaded previews. Watch the entire passage: one attractive frame cannot prove that every caption is readable. Check the final words of each phrase and the change to the next caption.

The [recorded Valmera style revision](CAPTION-STYLE-EXAMPLE.md) shows this type of change. Its two 9.6-second previews have matching decoded audio samples. That finding concerns those two files; it does not certify speech recognition or predict the result of a new run.

## Pass C: apply a supplied subtitle translation

This optional pass tests supplied text while keeping the original voice. It does **not** compare translation generation, dubbing or native-speaker quality. The Spanish draft below has not received independent native-speaker approval. Obtain a language reviewer if translation quality is part of your decision.

| English phrase | Supplied Spanish draft |
| --- | --- |
| What brings you to the land of the gatekeepers? | ¿Qué te trae a la tierra de los guardianes? |
| I'm searching for someone. | Busco a alguien. |

> Starting from preview B, replace the two English caption phrases with the supplied Spanish strings in the table, in the same phrase order. Retain the approved cut, original English soundtrack, speed, framing and short-group presentation. Fit the translated words within the corresponding phrase windows. Preserve accents and question punctuation. Render preview C. Do not dub or rewrite the spoken audio. Report any unsupported requirement.

The recorded example's phrase windows were program 0.10–2.50 and 6.55–8.00 seconds. These are reference observations: use the timing returned for your actual selection. Spanish words need not map one-for-one to English speech tokens.

Review C against B before changing the ending or another cut. Check accents, inverted question marks, complete wording, line breaks and reading pace. The [Spanish example](SUBTITLE-TRANSLATION-EXAMPLE.md) compares English v4 with Spanish v5; its shorter v6 is a separate delivery revision.

## Compare the sound

Listen to the same speech and source transitions in A, B and C at a consistent playback volume. Note changed music, doubled dialogue, missing word endings, sync shifts or unexpected processing. With suitable local tools, decoding audio using the same settings and comparing hashes can add an exact-sample check. The Spanish example provides the commands used for its comparison.

Matching decoded hashes establish identical samples for the files and settings compared. A mismatch is a reason to investigate, not automatic proof of audible damage: an editor may encode previews differently. Whole-video hashes should differ when rendered captions change. Keep measurements and listening observations separate.

## Export and inspect the delivery

> Export the approved version as an MP4 at the required resolution. Preserve its cut, captions and soundtrack. Report branding, end cards, plan restrictions or changes needed for delivery. If a revision is required, identify and preview it before exporting.

Play the downloaded file outside the editor, including its ending. In the recorded Spanish run, a dark tail initially blocked export. A separate 0.2-second source trim produced a 9.4-second timeline and an export lasting 14.458333 seconds including branding. The final file is not the unchanged comparison preview.

Record what happens in your run, including a blocked export. Do not quietly trim a difficult ending, switch plans or move to another application and describe the first attempt as successful. Corrections may produce a useful delivery; they also belong in the result.

## Fill the results after inspection

Duplicate this table for each editor. Begin with **Not tested**. Use **Pass**, **Changes needed** or **Blocked** after inspecting the relevant artifact. Evaluate the requirements important to your work before choosing a winner.

| Criterion | Status | Exact file, version, time and observation |
| --- | --- | --- |
| A retains the requested speech and source range | Not tested | |
| A captions contain the approved wording | Not tested | |
| B changes presentation without changing the cut | Not tested | |
| B retains the soundtrack and sync | Not tested | |
| C applies supplied text without dubbing | Not tested | |
| C punctuation and wording render completely | Not tested | |
| Caption pace is usable at intended viewing size | Not tested | |
| Final export matches the approved version | Not tested | |
| Resolution, duration and branding meet requirements | Not tested | |
| Full downloaded video played and reviewed | Not tested | |

Manual steps and corrections:

Failed attempts or unsupported requirements:

Audio measurement, decoder settings and scope:

Listening reviewer, device and observations:

Language reviewer and corrections, if commissioned:

Final decision and unresolved items:

This animated-film passage does not test overlapping speakers, noisy interviews, long-form drift, accents across a population, moving-person reframing or general creative quality. Follow it with your representative recording using the [broader evaluation kit](EDITOR-EVALUATION.md#6-repeat-with-the-footage-you-really-edit).

To run these briefs in Valmera, [connect your assistant](CLIENTS.md) or [open Studio](https://valmera.io/studio?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=speech_editor_trial). Account creation and uploads are free; AI editing requires eligible access. Check [current plans](https://valmera.io/subscribe).
