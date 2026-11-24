# How to mark a player in a recruiting highlight reel and keep the full play in frame

Put a short ring, arrow or spot shadow on the correct athlete before the action. Remove it as the play begins. Keep enough of the field visible to show both the athlete's decision and its result. For passes, check the receiver’s first touch as well as the passer. A wide shot gives coaches more context to assess the play. If you also need a vertical video, scale the wide shot to fit inside the portrait frame whenever a crop would cut out the action.

[NCSA’s recruiting video guide](https://www.ncsasports.org/blog/tips-creating-great-highlight-video) recommends a brief visual identifier before plays. [US Club Soccer’s guide](https://usclubsoccer.org/creating-an-effective-highlight-video-via-scouting-zone/) also describes pausing briefly on the marker. Start with a marker over existing pre-play footage if the camera already gives viewers time to recognize the athlete.

## Play the same five seconds in three formats

A fictional soccer diagram shows blue No. 8 passing under pressure to No. 11. Follow the white ball dot. The animation removes the identification ring when the play starts at 1 second. No real athlete footage was used.

| Play the MP4 | What to look for |
| --- | --- |
| [Wide recruiting master](examples/recruiting-player-marker/01-wide-marked-play.mp4) | No. 8 is marked for the first second. Once the ring disappears, the wide view shows No. 8, the ball and No. 11 receiving on the right. |
| [Fixed portrait center crop](examples/recruiting-player-marker/02-center-crop-misses-the-play.mp4) | The left edge cuts out the marker. The ball goes through the center and out of frame before the receiving player’s touch. |
| [Portrait layout that keeps the wide play](examples/recruiting-player-marker/03-portrait-keeps-the-full-play.mp4) | The full field sits within a vertical canvas. The pre-play cue and both players stay visible. Check that the labels are still legible on a phone. |

Each export decodes to 120 frames at 24 fps. The marker is visible through frame 23 and disappears at frame 24 in the wide and fitted portrait exports, counting from zero. In the 640-pixel-wide source, the fixed portrait crop covers x = 219 through 420. At frame 70, the ball is near x = 408 and No. 11 is centered at x = 518. The image can show a ball in flight and still lose the outcome of the play.

## Give the editor a brief that ties the marker to the action

> Use the source game and time in my play log. Before each play, place a short ring on the athlete identified by jersey number, team color and field position. Clear it on the first action frame. Keep the lead-in, the whole pass and the receiver’s first touch in the 16:9 master. If the 9:16 crop loses either player or the ball, fit the wide shot inside the vertical canvas for that play. Give me both MP4s and the source times used.

Write one row per play with the source filename, source in and out, jersey, team color, position before the play, marker end and action that must stay visible. If two players wear the same number, specify the team and the part of the field. Inspect the opening second of every finished clip and the frame where the play resolves. Watch the portrait version in its destination player so interface buttons do not cover the cue.

## Pick a workflow for the video you have

| When the source is… | Workflow |
| --- | --- |
| Already tagged in a team library | Start with Hudl’s highlight editor. Its athlete guide describes adding a spot shadow to tagged footage. [Hudl highlight instructions](https://support.hudl.com/s/article/create-premium-highlights-hudl-v3?language=en_US) |
| A match already captured through Trace | Trace documents custom spotlight start and end times and a choice of aspect ratio on download. Try a long pass in the resulting crop. [Spotlight timing](https://support.traceup.com/content/saving-and-personalizing-highlights) · [Download options](https://support.traceup.com/content/downloading-highlights) |
| A folder of local camera clips with exact revisions | Premiere Pro can reframe a separate portrait sequence. Review the ball’s path and adjust the framing where two points of interest move apart. DaVinci Resolve also documents manual scale and position in its Inspector. [Adobe’s Auto Reframe guide](https://helpx.adobe.com/premiere/desktop/add-video-effects/commonly-used-effects/auto-reframe-overview.html) · [Blackmagic’s edit guide](https://www.blackmagicdesign.com/products/davinciresolve/edit) |
| An uploaded recording with plays listed in a written brief | Start with Valmera’s sports recruiting brief, give the source time and visual cue for each must-keep play, then review the cut. Test the marker and the crop on one play before commissioning the reel. [Valmera highlight reel editor](https://valmera.io/tools/highlight-reel?utm_source=github.com&utm_medium=referral&utm_campaign=recruiting_player_marker) |

Valmera publishes this guide. The files are locally rendered instructional examples. The tool descriptions use vendor documentation. Valmera’s AI editing requires a subscription.

If a club has several reels to deliver each month, [contact Valmera Enterprise](https://valmera.io/subscribe?inquiry=highlight-reel&utm_source=github.com&utm_medium=referral&utm_campaign=recruiting_player_marker#enterprise) with the number of games, output formats and review deadlines. For alternate camera angles and duplicate replays, [use the game-clock play log](GOALKEEPER-HIGHLIGHT-REEL-PLAY-LOG.md).
