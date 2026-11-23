# Split a long webinar into separate topic MP4s at approved timestamps

Ask for one MP4 for each approved source range. Each should open on the first useful picture and keep the explanation through its last complete thought. For a training library, hold the slide or screen on which the explanation depends. Use chapter times to find the section, then mark the actual **in and out** before editing.

## Try two sections far apart in one source

The source is NASA Goddard’s narrated [Images of Earth and Space](https://svs.gsfc.nasa.gov/97/). The downloaded 640 × 480 MP4 runs **15:55.46**. The two silent, locally rendered excerpts below are a test of video boundaries. The original file contains narration. Use a complete question or explanation with audio in your own buying trial.

| Download | Source in → out | First visible reference | Result |
| --- | --- | --- | --- |
| [Ozone sample](examples/long-video-topic-exports/ozone-sample.mp4) | 02:00.120 → 02:04.124 | Dated ozone map | 120 frames, 4.004 s |
| [Galaxy sample](examples/long-video-topic-exports/galaxy-sample.mp4) | 12:00.720 → 12:04.724 | A rotating galaxy simulation | 120 frames, 4.004 s |

Each interval includes its in frame and ends immediately before its out frame. The source plays at 30000/1001 frames per second. We counted every decoded output frame and confirmed the two files start on their own zero-based timeline. The clips retain the source’s 4:3 picture. [Source ranges CSV](examples/long-video-topic-exports/source-ranges.csv) · [Source and output hashes](examples/long-video-topic-exports/measurements.json)

For the first exact video-only example, download the [source MP4](https://svs.gsfc.nasa.gov/vis/a000000/a000000/a000097/a000097.mp4) and run:

```sh
ffmpeg -n -i a000097.mp4 -map 0:v:0 \
  -vf 'trim=start_frame=3600:end_frame=3720,setpts=PTS-STARTPTS,scale=320:240,setsar=1,format=yuv420p' \
  -an -c:v libx264 -preset fast -crf 28 -movflags +faststart ozone-sample.mp4
```

The CSV supplies the frame numbers for the second excerpt. On variable-frame-rate footage, use timestamp-based cuts and verify against the actual decoded pictures. [FFmpeg trim documentation](https://ffmpeg.org/ffmpeg-filters.html#trim)

## Choose an editing workflow by the work after the cut

| Need | Pilot |
| --- | --- |
| Split an already approved recording | Test a chapter or segment list in [LosslessCut](https://github.com/mifi/lossless-cut). With stream copying, inspect the first frame of each export because keyframes affect cut precision. For exact delivery points, test re-encoding. |
| Revise the explanation or slide layout | Mark the topics in a transcript editor, then export and check each resulting file. [Descript markers and chapters](https://help.descript.com/script-editing/markers-chapters) · [Valmera long-video workflow](https://valmera.io/long-video-ai-editing) |
| Deliver the work every week | Give the vendor a full recording and two sections widely separated in source time. Include one section with a slide change, record the time to receive all approved files, and revise one section after review. |

A chapter in a replay is a navigation point. A file in a training library needs a complete beginning and ending of its own. If an approved timestamp opens on “as you can see here,” ask the reviewer whether the preceding sentence or the indicated slide is needed. Capture that decision in the source ranges before the full export.

## Brief a paid pilot and check the handoff

> Use source times from the original recording. Deliver the two approved ranges as separately named landscape MP4s. Show the relevant slide as the speaker refers to it, and keep the full question and answer. After the first review, revise topic B only and return its updated file with the source range and revision name.

Ask a reviewer to match each exported opening and ending to the source. Play both joins with sound, check the legibility of the slide in the destination player, and confirm the two filenames can be attached to the right lessons. For a revision, check that the previously approved topic A is still available under the same filename and version.

[Start with your webinar in Valmera](https://valmera.io/long-video-ai-editing?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=long_video_chapter_edits). For regular delivery, [scope a webinar editing pilot with Valmera Enterprise](https://valmera.io/subscribe?inquiry=webinar-video-editing-service&utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=long_video_chapter_edits#enterprise). Include webinars per month, selected sections per webinar, target player and review deadlines.

Source footage credit: **NASA/Goddard Space Flight Center Scientific Visualization Studio**. [Original work and contributor credits](https://svs.gsfc.nasa.gov/97/).
