# Edit a passage after the three-hour mark and keep its source timestamps

Extract the section you need into its own file before editing. In the review notes, save the original filename, the source start time, and the corresponding time in the excerpt. That gives an editor a short file to work with and gives a reviewer a direct route back to the original statement.

Valmera’s [long-video workflow](https://valmera.io/long-video-ai-editing) documents indexing the first three hours of an upload and using a separate file to edit later material. Separate the exact part you need and keep your original recording as the reference.

## Try a cut that starts at 03:00:01.250

The [synthetic source](examples/long-take-timecode/sparse-long-recording.mp4) has a reported duration of 03:00:07.96. It holds an opening slate for about three hours and then displays a visible source clock and frame counter. This small file tests a late seek. It has no audio and represents a timing fixture rather than a load test for a continuous three-hour camera recording.

Play the [five-second excerpt](examples/long-take-timecode/late-section.mp4). Its player starts at zero while the picture shows the original source time. The first picture was source frame 30. The output contains all 120 consecutive frames through source frame 149 at 24 fps.

| Check | Original source clock | Excerpt clock |
| --- | --- | --- |
| First frame | 03:00:01.250 | 00:00:00.000 |
| Review point | 03:00:03.000 | 00:00:01.750 |
| Last frame | 03:00:06.208 | 00:00:04.958 |

The last frame starts one frame interval before the end of the five-second excerpt. Use the [source-to-excerpt CSV](examples/long-take-timecode/source-to-clip-time.csv) when exchanging timestamped review notes.

## Repeat the extraction with your own recording

```sh
ffmpeg -ss 03:00:01.250 -i sparse-long-recording.mp4 -t 5 \
  -map 0:v:0 -map '0:a:0?' -c:v libx264 -crf 20 -pix_fmt yuv420p \
  -c:a aac -movflags +faststart late-section.mp4
```

Change the source filename, the start after `-ss`, and the requested duration after `-t`. This example maps the first video track and the first audio track if present. Choose the correct track explicitly for a recording with separate mixes or languages. Keep some lead-in and follow-through around the material you plan to use. FFmpeg decodes and discards frames before the requested start when accurate seeking is active during transcoding. When you use stream copy, the preceding seek point can affect what reaches your output, so inspect the delivered opening. [FFmpeg input seek reference](https://www.ffmpeg.org/ffmpeg-all.html)

## Keep the source and edit clocks in your review notes

1. **Record where the excerpt begins.** A note at excerpt 00:00:01.750 maps to source 03:00:03.000 in this example. Use elapsed time from the file start for the command. If the footage carries camera timecode, log that in its own field and identify the clip.
2. **Put the reference in your editing brief.** For an interview or public meeting, quote the complete sentence and give its excerpt time. Ask the editor to preserve the question or qualifier when its removal would change the meaning. Include a note that the original file starts earlier.
3. **After a revision, map each retained passage separately.** A single offset works for one uninterrupted excerpt. If a later edit removes 12 seconds or reorders two quotes, log the source range and the output range for each cut. For a review copy in a desktop editor, [DaVinci Resolve documents a visible source-timecode burn-in](https://documents.blackmagicdesign.com/SupportNotes/DaVinci_Resolve_19_1_New_Features_Guide.pdf).
4. **Review the downloaded MP4.** Check the first frame and last frame, listen to the ends of each spoken passage, and match one timestamped note back to the source recording. Keep the source map with the edit so the next reviewer can repeat the check.

[Edit the extracted passage in Valmera](https://valmera.io/long-video-ai-editing?utm_source=github&utm_medium=documentation&utm_campaign=late_recording_timecode). For recurring interviews, public events or long-form recordings, send your monthly volume, deadlines, and one example source range through [Valmera’s Enterprise contact](https://valmera.io/subscribe?utm_source=github&utm_medium=documentation&utm_campaign=late_recording_timecode#enterprise).
