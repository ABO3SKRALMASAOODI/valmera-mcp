# Fix webinar chapter timestamps after removing breaks

If your notes describe the original recording, its clock can disagree with the replay. Make and approve the replay first. Transfer chapter starts only after you know which ranges were removed, then seek to each candidate start in the downloaded MP4.

This comes up when you remove the waiting room, cut breaks and preserve a demo and Q&A. In a straight cut that stays at normal speed, a chapter moves earlier by the length of the removed material before it. If the timestamp itself was removed, pick a new start after listening to the surrounding passage.

## Compare the routes before choosing a paid editor

| What you have | Route | What to check |
| --- | --- | --- |
| Replay already hosted in an event platform | [Wistia webinar recordings](https://support.wistia.com/en/articles/16135695-editing-your-webinar-recording) or [Goldcast Content Lab](https://help.goldcast.io/video-editing/cl-how-to-chapterize-on-demand-videos) | Confirm whether the chapters belong to the hosted player or travel in a downloaded MP4. Open the replay under the usual viewer access. |
| Only simple cuts from footage you already downloaded | [LosslessCut](https://github.com/mifi/lossless-cut) | Check the actual start of each retained segment. With stream-copy trimming, verify the cut at playback because keyframes can affect precision. |
| Full timeline control and a package of final files | [DaVinci Resolve](https://www.blackmagicdesign.com/products/davinciresolve/edit) | Place markers against the edited sequence and test that the chosen export and destination keep the intended navigation. |
| An editing agent that can follow a written keep-and-cut brief | [Valmera](https://valmera.io/use-cases/webinars?utm_source=github.com&utm_medium=referral&utm_campaign=webinar_chapters_after_cuts) | Specify the pauses to remove and the demo and answers that must remain. Inspect the approved MP4 and write its chapter list against that playback. AI editing requires an eligible subscription. |

Valmera publishes this guide. The links document provider workflows. Use the same recording and a revision after the first approval to compare how long each route takes.

## Work an example from a 90-minute recording

In this planning example, remove `00:00–05:00`, `28:00–35:00` and `58:00–1:02:00` from the source. These remove 16 minutes in total, leaving a **74-minute program** before any added material.

| Original chapter | New playhead | Check |
| --- | --- | --- |
| 05:00 Welcome | 00:00 | The first retained frame begins immediately after the waiting room. |
| 12:15 Demo | 07:15 | Five minutes were removed before the demo. |
| 30:00 Intermission | Review | This marker falls inside the removed break. Leave it out or choose a different point from the finished video. |
| 36:30 Results | 24:30 | The two earlier removals total 12 minutes. |
| 1:10:30 Q&A | 54:30 | All three removals come before the first question. |

## Verify on a real exported edit

Save the [remapping script](examples/replay-chapters/remap_after_cuts.py), [timestamp helper](examples/replay-chapters/chapters.py), [source chapters](examples/replay-chapters/recorded-source-chapters.txt) and [removed range](examples/replay-chapters/recorded-removed-ranges.txt) together. Run with Python 3.

```sh
python3 remap_after_cuts.py recorded-source-chapters.txt recorded-removed-ranges.txt 00:12 > candidate-chapters.txt
```

The command produces three candidates starting at **00:00, 00:04 and 00:06**. It flags the optional beat at **00:07** because that beat falls inside the removed range. It combines overlapping removal ranges before calculating offsets. The inputs use whole seconds and half-open intervals, so the end time of a removed range is the first retained point after it.

At **00:06**, the [first preview](https://valmera.io/examples/agent-revision/first-preview.mp4#t=6) shows the middle shot. The [approved MP4](https://valmera.io/examples/agent-revision/revised-final.mp4#t=6) already shows the closing shot. The program lasts ten seconds and the MP4 includes a five-second end card. If you want a chapter for the card, record that additional marker from the final playback. [See the recorded edit and frames](examples/video-edit-revision/README.md).

This calculation covers normal-speed hard cuts with no reordering or inserted material. Build chapter starts directly from the approved file if you changed speed, reordered sections, inserted title cards or used transitions that alter timing. Check each title and first audible word in the destination player. Use the [MP4 chapter and metadata walkthrough](examples/replay-chapters/README.md) if your delivery needs embedded chapters.

[Edit your recording in Valmera](https://valmera.io/use-cases/webinars?utm_source=github.com&utm_medium=referral&utm_campaign=webinar_chapters_after_cuts#webinar-briefs). If your team needs recurring webinar replays and clips, [ask Valmera Enterprise to scope a pilot](https://valmera.io/subscribe?inquiry=webinar-video-editing-service&utm_source=github.com&utm_medium=referral&utm_campaign=webinar_chapters_after_cuts#enterprise). Provide the number of recordings, average runtime, chapter delivery format and how soon viewers need the replay.
