# Turn Twitch stream markers into a highlight reel from an OBS recording

A Twitch marker identifies a time in the stream. Your OBS recording can have an earlier start, different pauses or a separate file for each segment. Before you cut, match the same picture in the VOD and the uploaded file. If the local recording started 12 seconds earlier and both recordings ran continuously, add 12 seconds to the stream’s clip boundaries.

[Make a highlight reel from an uploaded recording in Valmera](https://valmera.io/tools/highlight-reel?utm_source=github.com&utm_medium=referral&utm_campaign=twitch_markers_highlight_reel) · [Try the worked ranges](examples/twitch-marker-highlights/stream-ranges.csv)

## Align the clocks before choosing a cut

During the stream, add a Twitch marker or use the broadcaster’s or editor’s `/marker` command. Name the moment so you can find it again. Twitch’s `position_seconds` is an offset from the beginning of the stream. When you edit the Twitch VOD itself, begin the review at that position. [Twitch creator help](https://help.twitch.tv/s/article/creating-highlights-and-stream-markers?language=en_US) · [Twitch marker reference](https://dev.twitch.tv/docs/api/markers/)

1. Find a distinctive visual frame before the first moment you want to keep. Write down its time in the Twitch VOD and in the exact local file you’ll edit. Use a visible score change or scene switch so you can identify the same frame.
2. Find another shared frame after the last moment. Subtract the stream time from the local time at both checks. In the example, Twitch `01:00` matches local `01:12` and Twitch `03:40` matches local `03:52`. Both offsets are **+12 seconds**.
3. If the offsets differ, use shorter continuous sections with their own anchors. If OBS split the recording, log the filename beside each local range. A range spanning two files needs an end point in the first file and a start point in the next. If a frame is missing from the recording, check the VOD or another recording before choosing the cut.

## Cut actions, not bookmarks

Give the marker enough room on each side for what viewers need to understand. In this illustrative example, the first marker at `01:52` follows the start of the setup. Starting the export at that marker would skip the decision that makes the next move intelligible.

| Moment | Twitch marker | Reviewed stream range | Local source range | Duration |
| --- | --- | --- | --- | ---: |
| Final setup, then the clutch | 01:52 | 01:47–02:00 | 01:59–02:12 | 13 s |
| Quiet strategy call | 02:30 | 02:24–02:39 | 02:36–02:51 | 15 s |
| Result screen and teammate reaction | 03:34 | 03:28–03:40 | 03:40–03:52 | 12 s |

Those three ranges make a 40-second sequence before titles or transitions. Watch the start and end of each selection, then scrub each join. Check that the first action is readable, that the quiet call survives, and that the result screen holds long enough to read.

## Generate an edit brief from your ranges

Download [the local Python helper](examples/twitch-marker-highlights/map_stream_ranges.py) and the [example CSV](examples/twitch-marker-highlights/stream-ranges.csv) from GitHub using **Download raw file**. Put both files in the same folder and run:

```sh
python3 map_stream_ranges.py stream-ranges.csv --anchor 01:00 01:12 --anchor 03:40 03:52 --duration 04:30
```

The helper reads reviewed, non-overlapping source ranges from the example CSV format. Enter your own stream in and out times, local file duration and two matching visual anchors. It runs locally and prints the mapped ranges and a paste-ready brief. For a broadcast with several local files, run the helper separately for each checked continuous section. It works in whole seconds, so use your editor for frame-specific trims.

> Make one 16:9 highlight reel from my uploaded recording, retaining the original audio. Keep 01:59–02:12 for the setup and clutch, 02:36–02:51 for the quiet call, and 03:40–03:52 for the result and reaction. Show the preview so I can check all three moments.

If the setup gets clipped, give a precise revision: “Start the first range two seconds earlier. Keep the other two ranges and their order.” Check the source boundaries again in the new preview before export.

## Choose the workflow for the source you have

| Source and result | Route to test |
| --- | --- |
| One moment from the original broadcast | [Twitch Highlighter](https://help.twitch.tv/s/article/creating-highlights-and-stream-markers?language=en_US) can show markers on the VOD timeline. Use the selected range to create a highlight on Twitch. |
| A Twitch or Kick VOD with no shortlist | [Eklipse AI Highlights](https://eklipse.gg/help/how-to-make-stream-highlights-with-eklipse/) imports the VOD and suggests clips. See whether the least obvious must-keep moment is in the results. |
| A public Twitch VOD and several short vertical clips | [StreamLadder ClipGPT](https://www.streamladder.com/clipgpt/import-from-twitch) imports a VOD, ranks clips and offers vertical cropping. Check the gameplay and facecam placement together. |
| A local OBS recording and a three-moment sequence | Map the stream times to the local file, then [upload and request the sequence in Valmera](https://valmera.io/tools/highlight-reel?utm_source=github.com&utm_medium=referral&utm_campaign=twitch_markers_highlight_reel). Use the same ranges for a focused revision. |

Test with a loud play and a quiet moment you want kept before committing the whole broadcast. A good first result preserves both and gives you enough source context to ask for a clean second cut.
