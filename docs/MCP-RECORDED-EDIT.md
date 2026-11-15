# A recorded MCP video edit: source, revision and downloadable result

On November 7, 2026, we ran Valmera's public edit-and-revise exercise through its MCP connector in a fresh project. It produced a 12-second square preview, accepted a request to shorten only the middle section, and exported the revised 10-second program. The downloaded MP4 lasts 15 seconds because this run includes a five-second branded end card.

**Published by Valmera.** This is one recorded run on our silent motion-graphic sample, not an independent comparison or a test of speech editing. The animation and wording already exist in the source. The connector performed the cuts, framing, revision, preview rendering and final export; we did not recreate the delivered video with a local editor.

[Source MP4](evaluation/recorded-run-20261107/original-source.mp4) · [First preview, 12 seconds](evaluation/recorded-run-20261107/first-preview.mp4) · [Revised final MP4, 15 seconds including branding](evaluation/recorded-run-20261107/revised-final.mp4) · [Evidence JSON](evaluation/recorded-run-20261107/evidence.json) · [Repeat the evaluation](EDITOR-EVALUATION.md)

Open both files at the edit point. [First preview at six seconds](https://valmera.io/examples/agent-revision/first-preview.mp4#t=6) · [Delivered MP4 at six seconds](https://valmera.io/examples/agent-revision/revised-final.mp4#t=6). For a single control that seeks both videos together, [open the synchronized comparison](https://valmera.io/ai-agent-that-edits-video#recorded-revision).

## Watch what changed at six seconds

Play the first preview and the revised export side by side below. Both start five seconds into the edit. Watch the heading on the right at **6.0 seconds**. It changes to “Share the finished cut” while the first preview still reads “Keep what serves the story.” The first preview reaches that same heading at **8.0 seconds**. Removing two seconds from the middle brings the last shot forward by exactly that amount.

![Synchronized excerpt. Both pictures show the middle shot at five seconds. The revised export cuts to the last shot at six seconds, and the first preview follows at eight.](evaluation/recorded-run-20261107/revision-playback.gif)

The excerpt samples every third frame of each 30 fps file from output seconds 5 through 9. The clock below the pictures shows output time. The small clock inside each picture identifies the source frame. For a still view, [inspect the frames on either side of the revised cut](evaluation/recorded-run-20261107/export-boundaries.png).

## What the run establishes

| Stage | Observed result | Evidence |
| --- | --- | --- |
| Upload | Original 25-second, 1280 × 720, 30 fps silent sample analyzed successfully | Source file, hash and analysis result |
| First edit | Source 3–7, 12–16 and 19–23 seconds retained; centered square crop | EDL v3, preview frames and downloaded 12-second / 360-frame preview |
| Revision | Source 14–16 seconds removed from the existing edit | EDL v4 retains 3–7, 12–14 and 19–23; 10-second revised preview |
| Delivery | Final EDL v4 MP4 downloaded successfully | Export receipt and matching SHA-256 |
| Final dimensions | 1080 × 1080 at 30 fps; 450 video frames over 15 seconds | `ffprobe` on the downloaded file |
| Sound | AAC track containing decoded digital silence | FFmpeg `astats`: minimum and maximum sample level both zero |
| Branding | Corner mark, branded ending over the final program frame, five-second end card | Frames extracted from the exact final MP4 |

The final file's 1080-pixel dimensions exceed the 720-pixel source height. That is output scaling, not evidence of additional source detail. The preview was 720 × 720.

## Reopen the cut decisions with the source media

[Download the rough-cut comparison ZIP](https://valmera.io/downloads/valmera-rough-cut-comparison.zip) and extract the whole folder. It contains the source, the actual revised delivery, the public edit record, and two versions of both a Shotcut project and a CMX 3600 list. We prepared the timelines from the retained source ranges in this recorded run. This package documents a handoff for this example.

To identify the original frame behind a review note, [open the source-timecode lookup](https://valmera.io/glossary/edit-decision-list#frame-lookup). Switch between **First cut** and **Revised cut** with record timecode `00:00:06:00`. For the reverse check, select **Source timecode** and enter `00:00:19:00`. That frame appears at record `00:00:08:00` in the first cut and `00:00:06:00` in the revision. Include the version, reel and both clocks in a handoff note.

Open `first-cut.mlt` and `revised-cut.mlt` in Shotcut. Keep `original-source.mp4` beside both files. In an editor importing a CMX list, select 30 fps non-drop-frame and relink the SOURCE reel to that same file. The three pieces should appear on a single video track.

| Timeline frame | First cut, source clock | Revised cut, source clock |
| ---: | --- | --- |
| 119 | 00:00:06:29 | 00:00:06:29 |
| 120 | 00:00:12:00 | 00:00:12:00 |
| 179 | 00:00:13:29 | 00:00:13:29 |
| 180 | 00:00:14:00 | 00:00:19:00 |

The last number in each clock is a frame count. In the revised project, advance from frame 179 to 180. The final scene now opens two seconds earlier. Both editable timelines preserve the landscape source. The packaged Valmera MP4 shows the separate square framing and branded delivery.

**How we checked the package.** We extracted the published package layout into a different folder, read both CMX files with OpenTimelineIO’s CMX adapter at 30 fps, and rendered both MLT projects with the renderer bundled with Shotcut (MLT 7.41.0). We compared the decoded luma plane of every rendered frame with the source frame selected by the recorded decisions. All 360 frames of the first cut and all 300 frames of the revision matched. This checks source selection and order. The automated check did not exercise an interactive GUI, audio, captions or project exchange in a commercial editor.

To compare another AI editor, ask it to keep 3–7, 12–16 and 19–23 seconds, then shorten only the middle range to end at 14 seconds. Ask the finishing editor to reopen what they receive, relink the source and move a cut. Play the separate reference render to check the intended framing and ending. [Compare both pictures at six seconds](https://valmera.io/ai-video-editor#timeline-handoff).

## Inspect the same cuts as Premiere XML

The [Premiere comparison and download](https://valmera.io/compare/valmera-vs-premiere-pro#timeline-handoff) includes a pair of Final Cut Pro 7 XML sequences, the 25-second original and the revised Valmera MP4. The XML is also available here as plain text. [First sequence](evaluation/recorded-run-20261107/premiere/first-cut.xml) · [Revised sequence](evaluation/recorded-run-20261107/premiere/revised-cut.xml).

In Premiere, use **File → Import** for each XML and locate `original-source.mp4` if asked. Both sequences use one video track at 30 fps. Source frames 570–689 make up the last shot in both cuts. That shot starts at frame 240 in the first assembly and at frame 180 after the revision. Leave the source linked and step across the join to check the picture counter. [Adobe media relinking](https://helpx.adobe.com/premiere/desktop/organize-media/ingest-proxy-workflow/relink-offline-clips.html).

These example sequences reconstruct the recorded cut decisions. The final square framing, branding and end card are visible in the delivered MP4. We checked XML source and sequence ranges with OpenTimelineIO. Desktop Premiere import remains untested.

### Check an XML returned by another editor

Use the two requests in this guide with the supplied `original-source.mp4`. If the editor returns a Final Cut Pro 7 XML, save our [picture-cut checker](https://raw.githubusercontent.com/ABO3SKRALMASAOODI/valmera-mcp/main/docs/evaluation/check_rough_cut_xml.py) beside the file. With Python 3 installed, run:

```sh
python3 check_rough_cut_xml.py your-revision.xml
```

The checker reads the XML locally. It compares which source frame plays at **every output frame**. A correct revision matches all 300. As a negative control, run it against the supplied `first-cut.xml` with the default settings. It reports that output frame 180 uses source frame 420 where the revision needs frame 570. To check the original request instead, add `--cut first`. Splitting a clip into two adjacent pieces is fine if the output still uses the same frames.

This exercise uses one enabled picture track, straight cuts, the original source filename and 30 fps. A filter, nested sequence or transition needs review in the destination editor. A passing result establishes the cut decisions written in the XML. Relink the media and review captions, sound, framing and the rendered MP4 separately. The checker reads file references and does not authenticate the media bytes.

## Verify the downloaded export

The mcp.film curator independently downloaded this run’s MP4, matched the file hash to the receipt, inspected the video stream and sampled frames for branding. The curator also checked the public endpoint’s authentication challenge and OAuth metadata. The authenticated editing steps above were run by Valmera. [Read the curator’s notes](https://mcp.film/mcps/valmera/).

To repeat the file check on macOS or Linux, download the recorded revision and run:

```sh
curl --fail --location --output revised-final.mp4 \
  https://raw.githubusercontent.com/ABO3SKRALMASAOODI/valmera-mcp/798e873006467bb0bab6f5332e83f9b99e69aba9/docs/evaluation/recorded-run-20261107/revised-final.mp4
shasum -a 256 revised-final.mp4
ffprobe -v error -select_streams v:0 -show_entries stream=width,height,avg_frame_rate,nb_frames:format=duration -of json revised-final.mp4
```

The expected SHA-256 is `9b7f97b8e75c80b49c8e2c61f2bace1c279cc26599d65b28b5d4d394bcdc592e`. The video stream should report 1080 × 1080, 30 frames per second and 450 frames. Play the ending to see how the ten-second program becomes a 15-second delivery. [Compare the saved measurements](evaluation/recorded-run-20261107/final-metadata.json).

## 1. Use a source other people can inspect

The [public example](https://valmera.io/examples/trim-and-reframe) supplies this clip. We downloaded it, checked its SHA-256, created a new project and uploaded it using `upload_start` and `upload_finish`. Editing began after `index_status` returned `done`.

The source has three centered headings, animated bars and a source timecode, with no speech or audio track. Its timecode distinguishes a correct selection from a video that merely has the expected length.

![Source frames before editing](evaluation/recorded-run-20261107/source-frames.jpg)

This is a basic editing check. Use a representative interview, tutorial or moving subject to evaluate speech recognition, captions, meaning preservation and tracking.

## 2. Make the first cut and inspect its preview

We used the [evaluation kit's first brief](EDITOR-EVALUATION.md#2-submit-the-same-first-edit): keep source seconds 3–7, 12–16 and 19–23 in order, use a centered square crop, preserve normal speed and add no creative material.

After reading the initial EDL and source frames, the assistant called:

```json
{"tool":"keep_segments","arguments":{"project_id":5532,"segments":[[3,7],[12,16],[19,23]],"snap_to_words":false}}
{"tool":"set_frame","arguments":{"project_id":5532,"ratio":"1:1","mode":"crop","focus_x":0.5,"focus_y":0.5}}
{"tool":"render_preview","arguments":{"project_id":5532,"complete":true,"quality":"approval","report":true}}
```

These are recorded arguments, **not a project ID to reuse**. Create your own project and copy its returned ID into every call. These ranges belong to this sample; do not transfer them to another recording. Each line represents a separate call.

The result was EDL v3 and a 12-second preview. We inspected its source-timecoded frames, including both joins, and retained the original preview file for comparison.

## 3. Revise one section without replacing the edit

The follow-up was specific: keep source 12–14 instead of 12–16 in the middle section, leaving source 3–7 and 19–23, framing and speed unchanged. We used a local source-time cut:

```json
{"tool":"cut_range","arguments":{"project_id":5532,"start":14,"end":16,"snap_to_words":false}}
```

The EDL changed from v3 to v4. Reading it back showed these ranges and the same centered square framing:

| Retained source in revised edit | First preview location | Revised program location |
| --- | --- | --- |
| 3–7 seconds | 0–4 seconds | 0–4 seconds |
| 12–14 seconds | 4–6 seconds, followed by source 14–16 | 4–6 seconds |
| 19–23 seconds | 8–12 seconds | 6–10 seconds |

The second complete preview was 10 seconds. Its sampled frames still showed the headings in the required order. The last section moved two seconds earlier in program time; its source selection did not change.

![Revised preview at sampled program times](evaluation/recorded-run-20261107/revised-preview-frames.jpg)

## 4. Check the downloaded export

We called `export_final` with project 5532 and EDL version 4. It returned job 137424, not a finished file. After `wait_for_job` reported `done`, `download_url` returned the final MP4. Its locally calculated SHA-256 matched the export receipt.

The output contains 300 frames of program and 150 frames of appended branding at 30 fps. Branding also blends over the last program frame; the delivery is not ten seconds of completely unobstructed footage. These are observations of this account and run, not promises about every plan's branding rules.

The image below comes from the **downloaded final MP4**, not the preview. Read each row left to right:

| Row | Left frame | Right frame | Check |
| --- | --- | --- | --- |
| 1 | Program frame 119, source `00:06:29` | Program frame 120, source `00:12:00` | First join at output 4 seconds |
| 2 | Program frame 179, source `00:13:29` | Program frame 180, source `00:19:00` | Revised join at output 6 seconds |
| 3 | Program frame 299, source `00:22:29` under branding | Frame 300, branded card | Program ends at 10 seconds; delivery continues |

Source labels use seconds and frames at 30 fps: `00:13:29` is the last source frame before 14 seconds, not 13.29 decimal seconds. Frame numbers above are zero-based.

![Exact frames either side of export joins and the branding boundary](evaluation/recorded-run-20261107/export-boundaries.png)

Inspect the downloaded file yourself:

```sh
ffprobe -v error -count_frames \
  -show_entries stream=codec_name,codec_type,width,height,r_frame_rate,nb_read_frames,duration \
  -show_entries format=duration,size -of json revised-final.mp4

ffmpeg -i revised-final.mp4 -map 0:a \
  -af astats=metadata=0:reset=0 -vn -f null -

shasum -a 256 original-source.mp4 first-preview.mp4 revised-final.mp4
```

Audio statistics establish silence in this output. They do not test speech, music or audio preservation on other inputs.

## What remains untested

Codex called the connected tools in this run. Claude, ChatGPT, Gemini or Grok may make different decisions with the same tools. We did not test competitors, score creative quality, measure per-edit charges, benchmark latency or establish reliability across repeated runs. The existing account's subscription tier and per-call charges were not independently established; no plan purchase or upgrade was made for this run.

Visual review covered sampled frames and the exact final-file boundaries above. We did not complete a continuous, human-equivalent playback review of every frame in an independent player. The evaluation kit's full-playback criterion remains untested; the files are provided for that review.

The preview emitted generic advisories about a speaker jump and shot-specific crop evidence. This synthetic source has no speaker. We did not treat those messages as proof of a visual defect or convert them into a quality pass. The centered crop and hard joins were intentional; the rendered headings remained visible in the inspected frames.

## Repeat it with your footage

[Connect Valmera to your assistant](https://valmera.io/mcp/setup?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=recorded_mcp_edit), create your own project and use the [same evaluation brief](EDITOR-EVALUATION.md). Then repeat with the recording you need to deliver. Check [current editing and account requirements](https://valmera.io/subscribe) before committing to a workflow.

Keep the first preview, request one precise revision, export the reviewed version and inspect the downloaded file. A useful comparison preserves failed attempts, unexpected branding and manual work alongside successful results.
