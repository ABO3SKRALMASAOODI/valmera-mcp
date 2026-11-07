# Translate video subtitles with AI while keeping the original audio

To translate a recorded video without changing the speaker's voice, create a translated subtitle track for the approved edit. Keep the original audio, correct the source transcript, translate complete thoughts, then check meaning, timing and layout in the delivered file. Dubbing, subtitle translation and replacing text already burned into the image are separate jobs.

This guide helps you choose a route and write a precise editing brief. It includes a comparison of ten documented workflows, downloadable English and Spanish teaching files, and a [localization review worksheet](SUBTITLE-TRANSLATION-WORKSHEET.md). It is published by Valmera; the vendor comparison is a documentation review, not a hands-on accuracy ranking. Sources were checked November 7, 2026.

[Start a Valmera editing brief](https://valmera.io/prompts#prompt-builder) · [Connect your assistant](CLIENTS.md) · [Current plans](https://valmera.io/subscribe)

For an actual rendered example, open [Spanish captions with the original English audio](SUBTITLE-TRANSLATION-EXAMPLE.md). It includes downloadable comparison previews, supplied source/target wording, identical decoded audio between the matching previews, and an export revision that removes a black tail. The supplied translation has not received independent native-speaker approval.

## Choose the output before choosing the translator

| Desired result | What changes | What to ask for |
| --- | --- | --- |
| Viewers read another language and hear the original speaker | Subtitle text | A translated SRT or VTT for the final edit, or a video with that translation burned in. |
| Viewers choose a language in a player | Separate selectable subtitle tracks | One clearly labeled file per language and a test in the destination player. |
| Both languages appear together | Caption layout and text density | A bilingual treatment tested at the actual viewing size. |
| Viewers hear translated speech | Spoken audio, possibly timing and lip movement | A dubbing workflow with explicit voice, timing and background-audio instructions. |
| Existing subtitles are part of the picture | Pixels in the subtitle region | Prefer a clean master; otherwise inspect subtitle removal and replacement on difficult frames. |
| Slides and interface labels also need translation | On-screen text beyond subtitles | A separate list of visible labels, titles and demonstrations to localize. |

“Keep the voice” is ambiguous: a cloned voice speaking another language changes the recording. If you want the original performance, say **keep the existing spoken audio, music, timing and mix; translate only the subtitle text**.

## Compare the route, not the language-count headline

These were the first ten results returned by our web search for “AI translate video subtitles keep original audio editor.” Search order is not a measured Google ranking. Each linked source is the provider's own description. Availability, export options and plan restrictions should be checked before starting a paid task.

| Product and primary source | Documented approach | A useful trial question |
| --- | --- | --- |
| [LumoCut](https://lumocut.com/) | Reads and replaces burned-in subtitles, with original audio retained by default. | Does the restored background stay convincing when the subtitle crosses a moving object? |
| [Fotor](https://www.fotor.com/ai-video-generator/ai-video-translator/) | Describes subtitle-only translation separately from translated speech. | Can you select subtitle-only output and correct a name before export? |
| [Clip Utils](https://www.cliputils.com/tools/translate-video) | Transcribes and translates speech into subtitles; describes SRT/VTT and burned-in exports. | Does the downloaded subtitle file match your approved cut and target-language wording? |
| [Vosko](https://www.vosko.ai/) | Combines translation, dubbing, subtitles and timing work. | Which controls keep the original recording when only translated text is needed? |
| [Tella](https://www.tella.com/edit-with-ai/translate-a-video) | Creates translated subtitles through its editor or Tella Agent; its guide distinguishes that from MCP tools that read or remove translations. | Is translation creation available through the interface you actually intend to use? |
| [Smartcat](https://help.smartcat.com/translate-video-audio-and-transcripts/) | Imports video or subtitle files for translation and review beside a video preview, with optional dubbing. | Can a language reviewer correct the subtitles against the corresponding scene? |
| [TitraTools](https://titratools.site/) | Works with SRT, ASS and VTT, including translation and manual timing edits with local video. | Can you preserve the existing timing while consistently handling product names? |
| [OpenDub](https://opendub.app/translate-video-to-english) | Describes translated speech, voice replacement or voice-over, and subtitle outputs. | Does the chosen mode produce the audio treatment you want, rather than a dub you did not request? |
| [Rask](https://www.rask.ai/tools/translate-text-in-video) | Translates text in the picture, including slides and burned-in subtitles, with an option to retain audio. | Are small labels, moving text and longer translations readable in the finished frame? |
| [CapCut](https://www.capcut.com/resource/translate-a-video) | Documents bilingual captions and a separate video-dubbing path. | Are you using the caption translation control or the audio translator, and what does the export contain? |

For Valmera, start with a representative passage and a specific brief through Studio or your connected assistant. Discover the available tools, request the intended text and audio treatment, and inspect the result before expanding to the full recording. The [recorded caption-style example](CAPTION-STYLE-EXAMPLE.md) demonstrates a caption revision with identical decoded audio between previews; it does **not** establish translation accuracy or a multilingual end-to-end test.

## Prepare the approved cut and a small glossary

Translate the cut you plan to publish. A transcript from the original hour-long recording will not share timestamps with a 45-second excerpt. Record the project, edit version and media filename first. If the cut changes later, review all affected language tracks against the new version; see [caption timing after cuts](CAPTION-REVISIONS.md).

Correct the source transcript while listening to the recording. A translation can be fluent and still inherit a wrong number, name or missing “not.” Use a short glossary to resolve choices before producing several languages:

| Item | Instruction | Why it matters |
| --- | --- | --- |
| Brand names | Keep Valmera and other approved names unchanged. | Avoid inconsistent spelling or an invented translation. |
| Interface labels | Retain the exact visible label, with an explanation where helpful. | A viewer must be able to find the control on screen. |
| Numbers and units | Preserve the quantity and units; adapt formatting for the intended locale. | A translated sentence must not change the instruction. |
| Qualifications | Preserve words such as only, unless, may and not. | Removing a condition can reverse the meaning. |
| Audience | Specify language, locale, tone and relevant vocabulary. | “Spanish” alone does not settle every editorial choice. |

For a software tutorial, translating the subtitle “Choose Save” while leaving an English **Save** button visible may be clearer than translating the label as if the interface itself had changed. Decide this explicitly with the reviewer.

## A bilingual example you can inspect

The following is an original, fictional eight-second tutorial script. It has no associated recording and is **not a Valmera-generated output or a translation benchmark**. The Spanish is an illustrative draft for review, not a claim of native-speaker approval.

Download the [English SRT](examples/subtitle-translation/tutorial-v1.en.srt) and [Spanish SRT](examples/subtitle-translation/tutorial-v1.es.srt), or open the [sample notes](examples/subtitle-translation/README.md).

| Cue and program time | English source | Spanish draft | Review focus |
| --- | --- | --- | --- |
| 1 · 0.000–2.000 s | Open the project. | Abre el proyecto. | The action remains an instruction. |
| 2 · 2.200–5.200 s | Keep the original audio. | Conserva el audio original. | The audio-preservation requirement remains explicit. |
| 3 · 5.400–8.000 s | Do not change the speed. | No cambies la velocidad. | The negation must survive translation. |

Both files have three cues with identical time ranges. That proves structural alignment between these sample files, not alignment to speech. A real translation may need different line breaks or cue segmentation to remain readable. Do not preserve cue count at the expense of meaning or force a longer translation into a tiny font.

For cue 2, the English text has 24 characters including spaces and punctuation; the Spanish draft has 27. Over three seconds, those are 8.0 and 9.0 characters per second. This simple measure helps spot dense cues, but it is not a universal readability threshold: language, script, audience, line breaks and the image all affect reading. Review at normal speed and at the smallest intended display size.

## Give the assistant a scoped brief

Replace the bracketed fields with your actual project and reviewed media version:

> In project [ID], use approved version [version]. Prepare [language and locale] subtitles for the passage [program time range]. Keep the existing spoken audio, music, mix, cuts, speed and framing. Correct the source transcript against the recording first. Use this glossary: [terms]. Preserve numbers, negations and qualifications. Show the source and translated text for review, then preview the agreed subtitle treatment. Identify the project version and any remaining uncertainty. Deliver [selectable subtitle file / burned-in video / both] if available through the current tools, and identify any unfinished delivery step.

Test a passage containing a name, a number, a conditional sentence and the densest on-screen layout. This reveals more than translating a greeting. Start in [Valmera Studio](https://valmera.io/dashboard) or use the [assistant connection guide](CLIENTS.md). Account creation and uploads are free; AI editing requires an eligible subscription, and an external assistant's billing is separate.

For a focused revision:

> In the translated caption containing [quoted phrase], restore the condition [intended meaning]. Keep all other approved wording, audio, timing and styling unchanged unless this correction needs a line break or cue adjustment. Explain that adjustment and show the affected passage again.

## Review meaning, layout and the actual delivery

A language reviewer should compare the translation with the spoken source and visual context. Back-translating can expose a suspicious omission, but an apparently similar back-translation is not independent proof of correctness.

Inspect the longest lines, speaker changes, mixed-language phrases and text over faces or controls. For right-to-left scripts, inspect direction, punctuation and mixed Latin names or numbers in the actual rendered player. For bilingual output, judge the two blocks together; two individually readable tracks can still overcrowd one frame.

If subtitles were burned into the original, a new selectable track will not remove them. Prefer the clean master where available. If the workflow removes text from the picture, examine the restored region throughout movement and cuts, not just a favorable still.

Deliver a clear filename and language label for each track, associated with the same approved video version. Open sidecar files in the destination player and confirm that the intended language can be selected. For a burned-in export, check the downloaded video with player captions disabled to catch accidental duplicate text, then listen for any unexpected audio change. Whole-video file hashes will differ when visual subtitles change; that alone says nothing about audio preservation.

Use the [review worksheet](SUBTITLE-TRANSLATION-WORKSHEET.md) to record the reviewer, exact files, corrections and unresolved items. For a real caption-only revision with downloadable evidence and audio-comparison details, inspect the [caption-style example](CAPTION-STYLE-EXAMPLE.md). Then repeat the relevant checks on your own translated recording.
