# How to add chapters to an edited webinar or interview MP4

A viewer choosing “Audience questions” needs the time that the first question begins in the **finished replay**. In the [two-hour interview planner](https://valmera.io/long-video-ai-editing?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=replay_chapters#chapter-planner), the questions start at 1:15:00 in the recording. The first three retained passages last 10, 25 and 8 minutes, so the chapter begins at **43:00** in the 75-minute cut. Click **Copy chapters** after entering the passages you kept.

Save the chapter list as UTF-8 text. Give each line a playback time and a title, beginning at 00:00. After a revision, play the exported file at each chapter start. Include any title card or branded ending in your final duration. The planner assumes straight cuts at normal speed.

## Try it on a finished edit

The [recorded three-shot edit](../video-edit-revision/README.md) has two versions. Shortening the middle shot moved the closing shot from 00:08 to 00:06. The delivered MP4 contains ten seconds of edited footage followed by a five-second end card. Use the following four starts to check the chapter menu on a short file before doing the same for a full interview.

| Playback time | What the chapter should open |
| --- | --- |
| 00:00 | Opening shot |
| 00:04 | Middle shot |
| 00:06 | Closing shot |
| 00:10 | Valmera end card |

Download the [revised MP4](https://valmera.io/examples/agent-revision/revised-final.mp4), [chapter list](https://raw.githubusercontent.com/ABO3SKRALMASAOODI/valmera-mcp/main/docs/examples/replay-chapters/revised-chapters.txt) and [conversion script](https://raw.githubusercontent.com/ABO3SKRALMASAOODI/valmera-mcp/main/docs/examples/replay-chapters/chapters.py) into one folder. With Python 3 and FFmpeg installed, run these commands there.

```sh
python3 chapters.py revised-chapters.txt 00:15 > chapters.ffmeta
ffmpeg -i revised-final.mp4 -f ffmetadata -i chapters.ffmeta -map 0:v -map '0:a?' -map_chapters 1 -c copy chaptered.mp4
```

The second command writes a new MP4 with the original video and audio streams and your chapter names. It selects video and audio tracks. If your delivery also needs embedded subtitles, add `-map '0:s?'` for MP4-compatible subtitle tracks. For your own file, replace the filename, chapter list and duration. The script accepts whole-second chapter starts and end times.

## Verify the delivered chapters

Open the result in a player with a chapter menu and select **Closing shot**. It should land on the closing picture at 00:06. You can also inspect the container directly.

```sh
ffprobe -v error -show_entries chapter=start_time,end_time:chapter_tags=title -of json chaptered.mp4
```

We ran the example on the public MP4 and read back four ranges in seconds: 0–4, 4–6, 6–10 and 10–15. The encoded video and audio streams each had the same SHA-256 before and after chapter insertion. A website that uses its own chapter field may ask for the plain-text list instead. [FFmpeg metadata format](https://ffmpeg.org/ffmpeg-formats.html#Metadata-2)
