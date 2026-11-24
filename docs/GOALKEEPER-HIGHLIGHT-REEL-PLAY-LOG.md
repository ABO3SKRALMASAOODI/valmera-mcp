# Make a goalkeeper highlight reel with distinct plays

Give each play a match, period, game clock, and source time range before you edit. Use one clear angle of the save, then show a different skill, such as playing a pass out under pressure. If you keep two angles of one event, mark the second as a replay so the viewer can follow it.

A game clock identifies the event. The recording time identifies the cut. Keep both when you have multiple cameras, different clips or an embedded replay. Hudl’s [soccer recruiting discussion](https://www.hudl.com/blog/recap-breaking-through-the-clutter-on-the-soccer-recruiting-trail) includes a college coach’s explanation of why a keeper’s ability to play to feet can be useful to show.

## Compare two equal-length decisions

Play the [15-second source sequence](examples/goalkeeper-reel/source-angles.mp4), then compare the [first reel with both angles of the save](examples/goalkeeper-reel/includes-replay.mp4) and the [revised reel with a save and a distribution play](examples/goalkeeper-reel/save-and-distribution.mp4). These are fictional field animations edited locally for this example. The same match clock and the ball’s path identify the duplicate.

| Event | Source range | First reel | Revised reel |
| --- | --- | --- | --- |
| 1H 18:44 · wide save | 0–5 s | 0–5 s | 0–5 s |
| 1H 18:44 · tight angle of the same save | 5–10 s | 5–10 s | Removed |
| 2H 07:12 · receive and pass to the right flank | 10–15 s | — | 5–10 s |

Both reels contain 240 frames at 24 fps. The first 120 decoded picture frames match. The remaining 120 in the revision match the separate distribution play from the source. The keeper, ball and target are visible from the back pass through the teammate’s first touch. [Download the play log](examples/goalkeeper-reel/play-log.csv) to map each event to its source and output.

## Compare editors on one representative match

| Footage you have | Workflow to evaluate | What the sample should prove |
| --- | --- | --- |
| Plays already tagged in a team account | Use the [Hudl highlight workflow](https://support.hudl.com/s/article/recruiting-faq-hudl-v3?language=en_US). | The correct player and source game can be found from the reel. |
| Local files and an editor who needs exact manual control | Build a short assembly in [DaVinci Resolve](https://www.blackmagicdesign.com/products/davinciresolve/edit). | The source in and out points can be changed precisely and the first approved play still appears in the export. |
| Uncut footage and a coach who gives notes by timecode | Use [Valmera’s highlight reel editor](https://valmera.io/tools/highlight-reel?utm_source=github&utm_medium=documentation&utm_campaign=goalkeeper_reel_play_log). | A written brief produces a preview, and a narrowly scoped correction makes it into the downloaded MP4. AI editing needs an eligible subscription. |

> Use the source video times in this play log. Keep the approved wide save from 0–5 seconds. Replace the tight replay in output seconds 5–10 with source seconds 10–15, where the keeper receives under pressure and passes to the right flank. Preserve the first play, its framing and its placement. Include the receiving player’s first touch. Show me the revision before export.

For your own match, sort plays by event rather than camera folder. Mark the opening second where jersey number and position become clear. Check that a coach can see what leads to the intervention, where the ball goes, and why the play matters. Share full-game references separately if the coach needs to see the possessions in context. [Hudl recruiting guidance](https://www.hudl.com/support/athlete-recruiting/guides/how-to-get-noticed)

If your club needs edits across several matches, send one game recording, a play log and your weekly output count to [Valmera Enterprise](https://valmera.io/subscribe?inquiry=highlight-reel&utm_source=github&utm_medium=documentation&utm_campaign=goalkeeper_reel_play_log#enterprise). Include the deadlines and where each version will be published. [Tournament delivery planning](TOURNAMENT-HIGHLIGHT-EDITING-SERVICE.md)
