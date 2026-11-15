# Free AI video editors without watermarks: check the actual export

A free editor is useful only if it delivers the file your project needs. Check the required AI operation, output resolution, branding, audio, duration and usage allowance together. A watermark-free preview does not prove a watermark-free download, and a free timeline does not necessarily include free AI processing.

This guide is published by Valmera. It complements the [free-editor comparison](https://valmera.io/free-ai-video-editor) with a short export trial and a record you can reuse. Vendor terms below were checked November 7, 2026; they are published claims, not hands-on competitor test results.

## Reproduce one cut and inspect the downloaded files

On November 15, 2026, we opened a four-second dialogue recording in Valmera’s free browser cutter and Ezgif’s free video cutter. In each tool we selected the same range, from 0.200 to 1.450 seconds, removed it and downloaded the default MP4. This tests a manual cut. The target end time was 2.750 seconds.

| File | Picture | Last video timestamp, including final frame duration | Last audio timestamp, including final packet duration | Audio | File size |
| --- | --- | ---: | ---: | --- | ---: |
| [Valmera export](https://valmera.io/examples/filler-word-cut/first-sentence-removed.mp4) | 800 × 400 H.264 | 2.750 s | 2.750 s | 48 kHz stereo PCM | 587,214 bytes |
| [Ezgif export](https://valmera.io/examples/export-check/ezgif-sentence-removed.mp4) | 800 × 400 H.264 | 2.840 s | 2.888 s | 16 kHz AAC | 59,073 bytes |

The larger file contains 528,000 bytes of uncompressed audio. Its higher sample rate cannot restore detail missing from the 16 kHz source. For a strict duration limit, check where both tracks end. In the Ezgif export, the picture starts at 0.080 s and the audio at zero. A rounded player display can show three seconds for either file.

To repeat the test, download the [source recording](https://valmera.io/examples/filler-word-cut/original.mp4). Listen through the join. You should hear “Um, use the green one for print.” For a subtitle handoff, open the [retimed SRT](https://valmera.io/examples/filler-word-cut/first-sentence-removed.srt) alongside the Valmera file and check the surviving line at 0.310 s. The [browser inspector and full comparison](https://valmera.io/blog/check-video-editor-export#inspect) let you compare your own two files on your device.

To check the container and stream metadata independently, run this command on each download. For streams with nonzero starts, add the reported stream duration to its start time to interpret the end on the presentation timeline. Some demuxers handle audio priming and padding differently.

```sh
ffprobe -v error -show_entries format=duration,size:stream=codec_type,codec_name,codec_tag_string,width,height,start_time,duration,sample_rate,channels -of json downloaded.mp4
```

## Locate the surviving speech after a cut

We used the same source excerpt, from 2.560 to 3.280 seconds, in three downloaded edits. The first two editors performed a manually selected removal from 0.200 to 1.450. For the third edit Valmera’s MCP connector placed a product shot over the original narration. All times below are relative to the beginning of the decoded audio track.

| Download | Expected start | Located start | Difference |
| --- | ---: | ---: | ---: |
| [Valmera removal](https://valmera.io/examples/filler-word-cut/first-sentence-removed.mp4) | 1.310 s | 1.310 s | 0 ms |
| [Ezgif removal](https://valmera.io/examples/export-check/ezgif-sentence-removed.mp4) | 1.310 s | 1.430 s | 120 ms later |
| [Valmera MCP cutaway](https://valmera.io/examples/b-roll-cutaway/final.mp4) | 2.560 s | 2.560 s | 0 ms |

[Try the waveform finder](https://valmera.io/blog/check-video-editor-export#compare-speech) to locate the excerpt automatically, compare your own files locally or check the removed portion at 0.440–1.200 s. A repeated excerpt can produce multiple plausible positions. If the narration has been replaced, sped up or mixed with music, listen to the result when the match is uncertain.

For an independent numeric check, download the [original MP4](https://valmera.io/examples/filler-word-cut/original.mp4), the Ezgif removal and the [Python checker](evaluation/check_speech_cut.py). With FFmpeg on your path, compare the expected position with the measured one in the same file:

```sh
python3 check_speech_cut.py original.mp4 ezgif-sentence-removed.mp4 --window 2560 1310 720 --window 2560 1430 720
```

At the expected 1.310 s position we measured −0.017. At 1.430 s the value rounded to 1.000. The checker decodes directly from the MP4s to mono at 16 kHz and computes a normalized correlation for each specified window. A value near one indicates similar waveforms at the supplied positions. This check locates the same speech within an edit. Confirm picture-to-sound sync by watching a visible event on the target player.

## Separate the promises before choosing a tool

| Wording | What you still need to establish |
| --- | --- |
| Free to start | Whether the completed project can be downloaded without paying. |
| No watermark | Whether premium assets block export, or branding appears in an ending clip instead. |
| Free AI | Which operation is included, how much you can process, and whether the allowance renews. |
| Unlimited exports | Resolution, duration, asset rights and whether AI processing has a separate limit. |
| Runs locally | Which operations stay on the device and whether an optional cloud model has separate charges. |

Write your actual requirement first: “A 60-second 1080p MP4 with reviewed captions, audible original speech and no added branding.” That is more useful than comparing the word *free* across homepages. If your destination accepts WebM, state that; do not assume a file extension is interchangeable with an export requirement.

## Four different export situations

| Route and official source | Published terms or observed scope | Your decision |
| --- | --- | --- |
| [Clipchamp](https://support.microsoft.com/en-us/clipchamp/does-clipchamp-add-a-watermark-to-videos) | Microsoft says the editor adds no watermark. On personal accounts, premium assets or features outside the plan can prevent exporting until the required plan is available. | Check the actual project for premium items before relying on its free export. |
| [Adobe Premiere on mobile](https://www.adobe.com/products/premiere/app.html) | Adobe describes free core editing and unlimited watermark-free 4K exports. Firefly generation uses credits, and its page distinguishes platform availability. | Separate ordinary mobile editing from the generative operation you need. Do not transfer mobile-plan claims to desktop Premiere. |
| [Renderforest](https://www.renderforest.com/ai-video-editor) | Its page describes free timeline editing, with free exports limited to 720p, a watermark and three minutes. AI panels use credits. | Decide whether that delivered file meets the job; access to editing controls alone is insufficient. |
| [Valmera browser utilities](https://valmera.io/free-ai-video-editor) | Free manual utilities are separate from paid Studio/MCP AI editing. The freeze-frame example below produced WebM. The single-range trimmer produces an MP4 in a supported browser. | Choose the operation you need and examine the downloaded file. Studio AI editing requires an eligible subscription. |

For Valmera AI, use the [current plans](https://valmera.io/subscribe). Account creation and uploads are free; eligible paid access is needed for AI editing. The [recorded Studio/MCP examples](MCP-RECORDED-EDIT.md) include export branding, so a paid subscription should not be assumed to mean an unbranded file.

## Run one representative export before the full edit

Use a short passage from footage you own or are authorized to upload. Include speech if your final video needs sound, motion if you need to inspect frame continuity, and a small label if readability matters. Use the same passage across candidates.

1. Record the app, device, account plan and date. Choose the actual AI feature or manual operation you need.
2. Make the edit and one small revision. Include any stock item, template or caption style you intend to use in the full project.
3. Inspect export settings and any payment gate. Record a blocked export as blocked; do not score its preview as a delivered file.
4. Download the file, then open it outside the editor. Check the beginning, corners and ending for added branding and listen to the audio.
5. Verify dimensions, duration and format. Watch the complete short sample, including the joins and final frames.
6. Record the allowance consumed and what the next export would cost. A one-time free trial does not establish an ongoing free workflow.

Do not use a silent source to conclude that speech or music is preserved. Do not remove a source creator's branding to manufacture a clean comparison. Distinguish marks already present in the source from marks added by the editor.

## Download a single cut without an account

Open the [free video trimmer](https://valmera.io/tools/cut-video-online#free-trim). For a first run, keep seconds **3 through 7** of the [25-second sample](https://valmera.io/examples/trim-and-reframe/original-source.mp4), choose **Create trimmed MP4**, then download the file. Open it in a separate player. You should see four seconds from the original 1280 × 720 motion graphic. The original has no audio track.

For a second run, download the four-second [speech test clip](https://valmera.io/examples/filler-word-cut/original.mp4) and choose it in the trimmer. Set the start to **0.5** and the end to **2.5**. Listen to the export. Those numbers deliberately cut into the spoken passage, so the words at the boundaries give you a way to catch a file that starts at the wrong point. This is a timestamp test. To remove a hesitation cleanly, listen for its actual boundaries and revise the selection.

| Output from the recorded browser check | Requested interval | Decoded file |
| --- | --- | --- |
| [Silent motion graphic](evaluation/first-cut-mp4/motion-trim.mp4) | Source 3.0–7.0 s | 1280 × 720, 4.00 seconds, one video track |
| [Speech excerpt](evaluation/first-cut-mp4/speech-trim.mp4) | Source 0.5–2.5 s | 800 × 400, 2.02 seconds, video and audio |

We tested both downloads on the live site on November 14, 2026. The speech file reported a duration of 2.02 seconds. Matching its waveform to the source placed the cut at 0.496 seconds for the requested 0.5-second start. We also compared three decoded frames of the silent export against source seconds 3, 4 and 6. The [verification record](evaluation/first-cut-mp4/verification.json) includes file hashes and measurements. Browser codec support varies. To request a second pass by chat, use **Use this cut in Studio**, upload the matching original and review the saved brief before sending.

## Keep one spoken sentence as an MP4

Open the [free transcript cutter](https://valmera.io/free-ai-video-editor#free-trim). Select “I like the blue label” or “Um, use the green one for print.” Play the source at the selected cue, adjust the start or end if you hear a clipped syllable, then choose **Create trimmed MP4** and download it. The sample includes its transcript.

For your own recording, choose the video and its matching SRT or WebVTT file. Select a timed passage from the menu. The browser uses the cue’s source timestamps to create the clip locally. A line in a subtitle file can split a sentence, so listen to both boundaries. Set the times manually if you have the video alone. Creating the local MP4 requires no account. Agent editing in Studio requires an eligible plan.

To reproduce the import with public media, download the [spoken source](https://valmera.io/examples/filler-word-cut/original.mp4) and its [matching WebVTT](https://valmera.io/examples/filler-word-cut/original.vtt). Select the second passage, from 1.56 to 3.73 seconds. In our Chrome check the downloaded MP4 ran 2.20 seconds and its audio aligned to 1.556 seconds in the source. Encoder padding and video frame boundaries can affect the reported duration.

## Inspect a freeze-frame export

The [recorded freeze-frame run](FREEZE-FRAME-EXAMPLE.md) provides a 25-second silent source and the unmodified downloaded WebM. A 2.5-second hold produced 825 decoded frames at a reported 30 fps, corresponding to 27.5 seconds. The output was 1280×720 VP9, with no audio stream; the source was silent too.

That record includes sampled frames and file hashes. It demonstrates a particular browser export, not general audio preservation, every-browser compatibility or frame-exact behavior. The source itself contains text and an ending card, which should not be mistaken for a newly added watermark.

Use the download to see what a reviewable record looks like, then test your own required file. A valid video can still fail the brief through the wrong format, missing audio, an unwanted ending or unreadable captions.

## Keep a compact delivery record

| Field | Your observation |
| --- | --- |
| Editor, interface, device, date and plan | |
| Exact source and permission to use it | |
| Required operation and revision | |
| Export completed, blocked or failed | |
| Downloaded filename, format, dimensions and duration | |
| Added branding: corners, opening, ending and audio | |
| Sound and captions checked in the downloaded file | |
| AI allowance used, reset terms and next-export cost | |
| Remaining work before publishing | |

Choose based on the delivered requirement. For a larger edit, use the [AI editor comparison kit](EDITOR-EVALUATION.md); for a known freeze moment, try the [free browser tool](https://valmera.io/tools/freeze-frame). Keep the source and approved output tied to the same review record.
