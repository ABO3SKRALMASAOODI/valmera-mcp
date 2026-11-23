# Keep a quiet guest reaction in a multicamera podcast edit

An automatic multicam cut follows the speaker. Review one moment where the audience should see the listener instead, such as a guest recognizing an important point before they answer. Switch the picture for that moment and keep the approved dialogue WAV on the original timeline. Start the buyer trial with a synced host angle, guest angle and approved mix.

## Watch the same dialogue with two camera cuts

| Edited time | [Speaker cut MP4](examples/podcast-camera-reaction/speaker-cut.mp4) | [Reaction cut MP4](examples/podcast-camera-reaction/reaction-cut.mp4) |
| --- | --- | --- |
| 0.00–0.80 s | Host camera | Host camera |
| 0.80–1.60 s | Host camera | Guest camera, with the host’s dialogue continuing |
| 1.60–2.40 s | Host camera | Host camera |

Both 16:9 exports contain 60 frames at 25 fps. We decoded the files and compared every frame. The picture differs on frames 20–39, counting from zero, and all other picture frames match. The decoded audio hashes match. These are held images and a dialogue excerpt from an animated trailer assembled as an editing reference. Use your own synced cameras to test motion, lip sync and the editor’s automatic switching. [Measurements and file hashes](examples/podcast-camera-reaction/measurements.json)

## Compare the revision workflow before buying

| If you work in… | What you can try | What to verify in your export |
| --- | --- | --- |
| Descript | Run Automatic Multicam using speaker labels, then set the guest angle in one scene. [Automatic Multicam documentation](https://help.descript.com/visuals/automatic-multicam) | Can you hold that scene on the guest without changing the dialogue edit or letting an automatic cutaway replace the shot? |
| Premiere Pro with AutoPod | Generate a multicam sequence with AutoPod, then change one video cut in Premiere. [AutoPod multicamera editor](https://www.autopod.fm/) | Can you keep the approved WAV in its own track while swapping the picture? Test with your actual audio layout. |
| Eddie AI with a timeline editor | Generate the speaker-based cuts, then adjust the chosen angle through the exported timeline. The Eddie guide describes different exports for Premiere, Resolve and Final Cut. [Eddie multicam workflow](https://www.heyeddie.ai/learn/eddie/multicam-podcast-edit) | Is the guest angle still available after relinking, and does the rendered MP4 use only the intended dialogue mix? |

Time the revision from feedback to playable MP4. A fast first pass matters less if a producer must relink footage or repair the audio after every picture note. If the editor needs separate microphones to infer who is speaking, keep them available as analysis inputs and explicitly select the approved mix for delivery.

## A revision brief you can send to any editor

> Keep the episode cut and the dialogue mix as approved. From [edited time in] up to [edited time out], replace only the host picture with the corresponding guest camera. Return to the original angle on the out frame. Preserve captions, crop, duration and dialogue timing. Send a landscape MP4 and a short preview around both cuts.

Confirm the timecodes are on the edited sequence. Review the frame before, the first guest frame and the frame that returns to the host. Then listen across both switches. If two MP4s use different audio encoding settings, check sync, the absence of doubled voices, and the level through the switch. Compare decoded audio hashes when both deliveries use the same audio settings.

[Try an edit from a written brief in Valmera](https://valmera.io/ai-video-editor?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=podcast_camera_reaction). For done-for-you editing, send Valmera Enterprise one representative episode, the number of episodes per month, and a revision like the one above. [Discuss a recurring editing pilot](https://valmera.io/subscribe?inquiry=podcast-video-editing-service&utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=podcast_camera_reaction#enterprise).

© copyright Blender Foundation | [durian.blender.org](https://durian.blender.org/). The stills and audio are from the [Sintel trailer](https://download.blender.org/durian/trailer/sintel_trailer-1080p.mp4), licensed under [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/). Modifications include cropping, layout, a picture switch, and a shortened dialogue excerpt.
