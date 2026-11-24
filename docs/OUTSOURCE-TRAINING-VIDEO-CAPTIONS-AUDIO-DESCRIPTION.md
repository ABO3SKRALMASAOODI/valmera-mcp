# Outsource software training video editing with captions and audio description

For a recurring batch of software tutorials, order the picture edit, corrected captions, and any audio description as separate deliverables. A caption file carries dialogue and meaningful sounds. Audio description conveys needed visual information, such as a permission changing from Viewer to Publisher or a confirmation that appears without narration. Have the editing and accessibility owners agree on when a lesson’s timing is approved. [W3C guide to captions](https://www.w3.org/WAI/media/av/captions/) · [W3C guide to description](https://www.w3.org/WAI/media/av/description/)

## Try this 15-second delivery check

The fictional lesson shows a workspace permission change. Play the standard export with your eyes closed. You can hear what action to take, then save, but the narration leaves out the original role and the confirmation message. The described export adds those details in the gaps. This example uses synthetic speech and was rendered locally. It demonstrates what to request in a pilot.

| Deliverable | Video | Timed captions |
| --- | --- | --- |
| Standard lesson | [Download standard MP4](examples/described-training-video/standard.mp4) | [Standard WebVTT](examples/described-training-video/standard.vtt) |
| Lesson with audio description | [Download described MP4](examples/described-training-video/described.mp4) | [Described WebVTT](examples/described-training-video/described.vtt) |

Both files run 15 seconds, at 640 × 360 and 30 fps. All 450 decoded picture frames matched. The description starts at 4.15 seconds and 12.15 seconds, in gaps between the original lines. The matching WebVTT includes the extra narration so captions stay complete in the described edition. [Download cue timings and verification results](examples/described-training-video/measurements.json)

**Described transcript**

1. At 0.50 seconds, the instructor says “Open Permissions for this workspace.”
2. At 4.15 seconds, description adds “The role is Viewer. The status says Draft.”
3. At 9.15 seconds, the instructor says “After changing the role, save your changes.”
4. At 12.15 seconds, description adds “The role is now Publisher. Saved.”

## Choose who owns the picture cut and the accessible versions

| Route | What to ask the provider to quote |
| --- | --- |
| **Valmera Enterprise for the recurring footage edit** | Send recorded lessons and scope a staffed edit, picture review, corrected captions and an approved master. If audio description is required, state it up front and agree who writes, reviews, records, and checks it in your player before ordering. [Valmera training video editing](https://valmera.io/training-video-editing-service?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=training_audio_description) |
| **3Play Media for a finished master that needs accessibility work** | Get a separate quote for captions and standard or extended description. Ask what voice and file types are available for your LMS. [3Play Media audio description](https://www.3playmedia.com/platform/audio-description/) |
| **Verbit for recurring caption and description delivery** | Ask about human review, turnarounds, and how to receive captions and description together for the final master. [Verbit audio description](https://verbit.ai/audio-description/) |
| **ViddyScribe for an in-house pilot** | Test its script review and described export using approved footage, with your own reviewer checking UI names and decisions. [ViddyScribe workflow and export documentation](https://viddyscribe.com/resources) |

Base the comparison on the combined cost of the edit, description, captions, and review. For example, a 25-lesson month can include simple walkthroughs with space for narration and dense tutorials that need a longer described edition. Measure the count in each group during the pilot before asking for a monthly quote.

## Send two lessons with different challenges

Start with a short lesson that has good gaps for audio description. Pair it with a lesson that has continuous narration or critical on-screen text that changes quickly. Include the product vocabulary, the canonical UI version, and one named reviewer who can confirm what the learner needs to know. Send the target player and caption formats along with source and audio tracks.

1. **Approve the picture before timing accessibility files.** Review the final instructions, source screens, and cut order. Lock a version identifier for the master sent to the captioning and description owners.
2. **Agree on what the learner must be able to do.** Mark important state changes, warnings and controls. In the sample, a listener should be able to name the role before and after the change and tell whether it was saved.
3. **Separate editions when timing changes.** Ask for standard description where it fits the existing gaps. For a dense lesson, ask whether the instructor can revise the script or the vendor should make an extended described version. If the picture is paused, get a caption file timed to that edition. [W3C description options](https://www.w3.org/WAI/media/av/description/)
4. **Test files in the target LMS.** Check each video with captions on and off. Verify access to the described edition, then spot-check the opening, a middle cue and the final status. A working file on an editor’s desktop establishes only that it can be played there.
5. **Request one revision before agreeing to volume.** Change an early cut or correct a product term. Ask which files were replaced, and verify that later descriptions and captions still align with the new picture. [Training-video delivery verification](VERIFY-TRAINING-VIDEO-HANDOFF.md)

## Brief Valmera Enterprise for a recurring editing pilot

Include the monthly number of lessons, expected run time, the target LMS, whether the source audio is separate, and any requirements for corrected captions or a described edition. Share a short example you can disclose and one success criterion that the learner must be able to demonstrate. [Send the training-video scope to Valmera Enterprise](https://valmera.io/subscribe?inquiry=training-video-editing-service&utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=training_audio_description#enterprise)
