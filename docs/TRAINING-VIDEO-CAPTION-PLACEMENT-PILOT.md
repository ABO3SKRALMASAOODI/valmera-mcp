# Can learners see the button? A caption placement test for software training videos

When you outsource software training video editing, ask bidders to return one lesson in your actual course player before you commit to a recurring batch. A caption can be accurate and still cover the exact button a learner is meant to click. Use the test below to catch that problem at the player width your learners use and to compare what a vendor charges to fix it.

## Try the same frame with two caption placements

[Download the offline caption placement simulator](examples/training-caption-placement.html?raw=1) and open the HTML file in a browser. Select **Compact** and change **Over the control** to **Above the control**. In the simulated account settings screen, the first caption covers **Save settings**. The second displays the same words and leaves the button visible. The simulator shows one synthetic frame and illustrates the geometry. Use the recorded lesson and your own player for sign-off.

W3C describes captions covering relevant information as a failure of the prerecorded-caption criterion. WebVTT supports setting the line for individual cues. A course player’s caption rendering and controls can change what viewers actually see. [W3C’s caption obstruction example](https://www.w3.org/WAI/WCAG22/Techniques/failures/F8) · [WebVTT cue settings](https://www.w3.org/TR/webvtt1/#webvtt-cue-settings)

## Give each vendor the same short pilot

1. Send a 15–30 second screen recording with a real task and one critical button or confirmation near the bottom edge. Use a demo account. Write down the exact timestamp when the critical control first becomes readable and the action the learner should take.
2. Ask for the edited MP4, the caption file accepted by your player and a note naming any cue repositioned, any framing change and the reason. Ask vendors to quote the first edit, one revision round and the expected weekly volume separately.
3. Upload the files to a test course. Write down the actual player widths in CSS pixels. Play with captions on at the smallest width you support and at the usual desktop width. Repeat when the player controls are visible.
4. Ask a reviewer who has never seen the recording to name the button and complete the task from the lesson. Record the timestamp, width, browser and verdict. Repeat after publishing the fix. Check the cue just before and just after the critical frame for a new collision.

| Record during review | Pass condition |
| --- | --- |
| Critical button or confirmation | Reviewer can read it while the relevant caption is on screen. |
| Caption and player controls | Caption stays legible at both widths with player controls visible. |
| Learner task | Reviewer completes the action using the lesson. |
| Delivered files | Replacement caption file matches the final MP4 and works in the course player. |
| Revision turnaround | Record elapsed time from sending the timestamped issue to accepting the replacement. Compare vendors using the same review window. |

### A two-cue example for a WebVTT-capable player

The first cue uses the player’s default position. The second asks to place the relevant instruction near the top for the few seconds when the button matters. Adjust both times and line placement for your own footage.

```vtt
WEBVTT

00:00:01.000 --> 00:00:03.000
Review the changes to your account.

00:00:03.000 --> 00:00:06.000 line:20%
Select Save settings to apply your changes.
```

If your player drops cue positioning during import, reframe the screen recording to leave room for the captions and check button legibility again. If your player accepts SRT, test its actual import. Use an edited MP4 with burned-in captions when you need fixed positions, and agree with your team whether a selectable caption version must also be delivered. Keep a copy of the clean master and approved caption file for future revisions.

## Scope a done-for-you batch with Valmera

Valmera’s Enterprise editing service is for teams with recurring footage that want a team to handle the edits. Share your monthly volume, one representative recording, the player or LMS, caption format and supported widths. Include the time of one important click or confirmation and your release deadline. Ask for the pilot deliverables and revision timing in the same quote.

[Contact Valmera about Enterprise training video editing](https://valmera.io/subscribe?inquiry=training-video-editing-service&utm_source=github.com&utm_medium=referral&utm_campaign=training_caption_placement_pilot#enterprise) · [See Valmera’s training video editing service](https://valmera.io/training-video-editing-service) · [Check delivery formats for a course player](TRAINING-VIDEO-MP4-WEBVTT-OR-SCORM.md)
