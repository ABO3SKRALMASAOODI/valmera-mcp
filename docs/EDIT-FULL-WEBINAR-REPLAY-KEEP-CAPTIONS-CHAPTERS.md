# Edit a full webinar replay and keep captions and chapters in sync

Approve the revised MP4 before you hand off the SRT and chapter list. If you cut a seven-minute break from a 90-minute webinar, the replay runs 83 minutes before any new material. A Q&A that began at 1:10:30 now starts at 1:03:30. Verify those times in the downloaded file. A subtitle that crosses the cut may also need new wording.

This guide is for webinar producers who need one complete replay for their event page, learning platform or archive. The handoff is the MP4, a separate SRT for toggleable captions and a plain-text list of chapter times for the destination player. If the destination requires embedded chapters, check its import behavior using the [MP4 chapter example](examples/replay-chapters/README.md).

## Run the cut and check what actually changed

[Download the offline test kit](https://raw.githubusercontent.com/ABO3SKRALMASAOODI/valmera-mcp/main/docs/examples/replay-chapters/replay-handoff-kit.zip). It includes the chapter and SRT inputs, a reviewed SRT and the Python 3 scripts. The sample captions label shots in a silent teaching video.

The [first preview](https://valmera.io/examples/agent-revision/first-preview.mp4#t=6) has twelve seconds of program. It shows the middle shot at six seconds. Removing the range from six seconds up to eight seconds makes the closing shot appear at six seconds in the [approved export](https://valmera.io/examples/agent-revision/revised-final.mp4#t=6). The revised program runs ten seconds, followed by a five-second end card. [See the recorded edit and frame checks](examples/video-edit-revision/README.md).

Unzip the kit and run these commands in its directory.

```sh
python3 remap_after_cuts.py recorded-source-chapters.txt recorded-removed-ranges.txt 00:12 > candidate-chapters.txt
python3 retime_srt_after_cuts.py source-cues.srt --remove 6 8 > candidate-cues.srt
python3 check_srt_revision.py candidate-cues.srt reviewed-cues.srt
```

| Item on the first preview | Candidate after the cut | What to check |
| --- | --- | --- |
| Optional chapter at 00:07 | Flagged for review | Its start fell inside the cut. The optional beat is gone, so leave its chapter out. |
| Closing chapter at 00:08 | 00:06 | Seek there in the approved MP4 and check that the closing shot is the first frame of the chapter. |
| Middle-shot cue from 00:04.000 to 00:06.400 | 00:04.000 to 00:06.000 | The cue still refers to the removed beat. The reviewed SRT keeps the timing and fixes the text. |
| Cue from 00:06.400 to 00:08.000 | Dropped | The full cue fell inside the cut. |
| Closing cue from 00:08.000 to 00:11.800 | 00:06.000 to 00:09.800 | It still ends during the program. Check any captions for the end card separately. |

The comparison reports **three cues checked, one text change, zero timing changes** between the candidate SRT and the reviewed SRT. The chapter script and SRT script used the first preview as the source clock. Use the same source clock for your cut list and your timed files, even if an earlier camera recording has a different clock.

These scripts cover straight removals at normal speed. If you add new material, change speed, reorder sections or use transitions that change runtime, take new chapter times and subtitle timing from final playback. If you have no reliable cut list, caption and mark the approved export directly.

## Choose a route for a paid pilot

| Where you deliver the replay | First test |
| --- | --- |
| In your Wistia event room | Edit a copy of the recording, then check the updated transcript and chapter starts in the hosted player. Review how replacing an existing replay affects its media analytics before the pilot. [Wistia replay editing](https://support.wistia.com/en/articles/16135695-editing-your-webinar-recording) · [Wistia chapters](https://support.wistia.com/en/articles/8283768-chapters-in-your-video) |
| To a separate host or a marketing team | Ask Eddie AI for a complete replay with the break removed and the demo and Q&A preserved. Its guide describes a full export and chapter timestamps for a description. Test the separate SRT handoff in your destination. [Eddie AI webinar editing](https://www.heyeddie.ai/how-to/edit-webinar-recordings) |
| To several destinations with a written editing brief | Give Valmera the same recording and keep-and-cut brief. Review the complete MP4 in Studio, then verify the separate SRT and chapter list against the approved export. [Valmera webinar workflow](https://valmera.io/use-cases/webinars) |

Valmera publishes this guide. The table uses the providers’ documentation. The downloadable test and recorded export cover the Valmera example.

## Brief the edit and accept the delivery

> Remove the live break from 28:00 to 35:00. Preserve the complete slide demo and Q&A in their original order, including the first question. Keep slide text readable. Return one full MP4 for review. Take subtitle and chapter times from the approved cut.

In the final player, seek to both sides of the join and listen without captions for clipped speech or repeated audio. Turn captions on and check the cue that crosses the cut, the first retained cue and the first Q&A answer. Click the demo and Q&A chapters and confirm they open at the promised moments. Save the MP4, SRT and chapter list under the same revision name. Time the whole handoff, including revisions and quality checks, to compare the cost per finished replay.

[Run a self-serve pilot with a full recording](https://valmera.io/long-video-ai-editing?utm_source=github.com&utm_medium=referral&utm_campaign=full_webinar_replay). For done-for-you production, include your monthly recording count, typical runtime, required formats and delivery deadline when you [scope recurring webinar editing with Valmera Enterprise](https://valmera.io/subscribe?inquiry=webinar-video-editing-service&utm_source=github.com&utm_medium=referral&utm_campaign=full_webinar_replay#enterprise).
