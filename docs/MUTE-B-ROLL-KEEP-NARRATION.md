# Add B-roll without losing the original narration

Put the B-roll over the picture and set the inserted clip’s own volume to zero. Leave the main recording’s audio on. Export an MP4 and listen through both joins. If you hear a scanner beep, room noise, or a second voice, the insert’s audio is still in the mix. If the speaker goes quiet, check the main audio underneath the overlay.

## Hear three exports with the same picture

The main recording describes packing an order. At 2 seconds the picture switches to the cutaway slate and at 5 seconds it returns to the main slate. Play each export from the beginning with audio on. The source narration and the scanner tone are synthesized for this listening test.

| Play the MP4 | What you hear at the cutaway | What you check in an editor |
| --- | --- | --- |
| [Narration only](examples/b-roll-audio/01-narration-only.mp4) | The sentence continues through both picture changes. | Keep the main audio on at its original level. |
| [Cutaway audio leaks](examples/b-roll-audio/02-cutaway-audio-leaks.mp4) | A short beep masks part of the sentence around 3 seconds. | Mute the inserted clip or remove its separate audio track. |
| [Narration drops out](examples/b-roll-audio/03-narration-drops-out.mp4) | Part of the sentence disappears until the main picture returns. | Restore the main audio through the entire cutaway. |

All three exports have the same 312 decoded video frames at 24 fps. The clean version’s decoded audio matches the narration reference sample for sample. From 3.2 to 3.6 seconds, the leaked beep's 1,320 Hz component was about 37 dB higher than in the narration reference, and the third file decoded to silence over that interval. These measurements describe the controlled listening test. [Download the measurements](examples/b-roll-audio/measurements.csv).

## Give an AI editor a brief you can verify

> Use my packaging walkthrough as the main recording and my label-scan clip as the visual cutaway over “scan the carton label.” Mute the label-scan clip. Keep the main recording’s entire voice track at its current level, with the same timing and duration. Show me both picture joins and export the approved version as MP4.

Next, ask for the picture to return one word earlier. The start and end of the voice should stay in the same place. Listen for the full sentence, then check the exported MP4 even if the preview sounded right. If the beep is already baked into the original narration file, muting the cutaway cannot remove it. Bring a clean mic track or request a separate audio repair.

## Choose an editing workflow for your clips

| If you want to… | Start with… |
| --- | --- |
| Describe the phrase, file and audio behavior in one request | Valmera documents picture-only cutaways, uploaded B-roll, review in chat and MP4 export. [Valmera’s B-roll workflow](https://valmera.io/tools/add-b-roll) |
| Set placement and audio levels by hand | Import the shot, layer it above the main recording and set the overlay volume independently. [Descript’s layer controls](https://help.descript.com/hc/en-us/articles/27197208246797-Adjust-layer-properties) |
| Compare narration-driven matching from a batch of your own clips | AgentReel documents using a talking-head clip as narration and matching a batch of uploaded supporting footage. Try the second revision above and listen to what happens to the original sound. [AgentReel’s B-roll docs](https://agentreel.ai/docs/ai-broll-editor) |

Valmera publishes this guide. Workflow descriptions for other editors come from their public documentation. The files above are a controlled listening fixture. To see a Valmera product export with an uploaded swatch shot and original narration, [play the recorded cutaway demo](OWN-FOOTAGE-B-ROLL-CUTAWAY-TEST.md).

[Prepare your own cutaway brief in Valmera](https://valmera.io/tools/add-b-roll?utm_source=github.com&utm_medium=referral&utm_campaign=clean_b_roll_audio). Hosted AI editing requires a subscription. If your team supplies footage for recurring demos, lessons or interviews, [contact Valmera Enterprise](https://valmera.io/subscribe?utm_source=github.com&utm_medium=referral&utm_campaign=clean_b_roll_audio#enterprise) with the monthly volume and a sample that needs the main audio preserved.
