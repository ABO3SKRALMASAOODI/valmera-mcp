# Keep both microphones when editing a split-stereo podcast video

If the camera recorded the host on the left and the guest on the right, treat those channels as two microphone sources. Listen to them separately and label each one before you trim. Then make a centered dialogue mix, or give the editor both isolated tracks and tell them which delivery mix you want. Duplicating the left channel into both ears makes the host sound centered and can make the guest disappear.

[Edit a prepared long recording in Valmera](https://valmera.io/long-video-ai-editing?utm_source=github.com&utm_medium=referral&utm_campaign=podcast_split_microphones) · [Scope recurring podcast editing with Valmera Enterprise](https://valmera.io/subscribe?inquiry=podcast-video-editing-service&utm_source=github.com&utm_medium=referral&utm_campaign=podcast_split_microphones#enterprise)

## Listen to the same picture with three audio layouts

These six-second practice files use synthetic speech and two speaker cards. Play them in stereo with headphones, then check each side on its own. The host starts near **00:00.30**, and the guest starts near **00:03.30**.

| MP4 | What you hear | What to check |
| --- | --- | --- |
| [Split-mic source](examples/podcast-split-mic/split-mic-source.mp4) | Host left, guest right. | Each voice is isolated to one channel in this fixture. |
| [Left mic duplicated](examples/podcast-split-mic/left-mic-only.mp4) | Host in both ears. The guest card plays in silence. | A centered first voice does not prove the second mic survived. |
| [Both mics centered](examples/podcast-split-mic/both-mics-centered.mp4) | Host and guest in both ears. | Check the guest sentence with either side muted. |

All three MP4s have **144 identical decoded video frames**. The guest’s interval measures zero on both decoded channels in the left-only file. In the centered file it measures about **2,048 RMS sample units per channel**. That number describes this fixture, and the appropriate level for your release depends on delivery requirements. [Decoded channel measurements and file hashes](examples/podcast-split-mic/measurements.json)

## Choose how to prepare the microphone tracks

| Workflow | Where to handle the channels | What to test before paying |
| --- | --- | --- |
| [Premiere Pro](https://helpx.adobe.com/premiere/desktop/add-audio-effects/advanced-audio-techniques/change-source-audio-channel-mapping.html) | Use the source clip’s audio channel mapping to assign the left and right sources separately. | Mute each source track in turn, then check the downloaded delivery mix. |
| [DaVinci Resolve](https://help.rode.com/hc/en-us/articles/14264466339343-How-To-Separate-Stereo-Recordings-in-Davinci-Resolve) | Use the channel assignments in RØDE’s split-microphone workflow to put the two channels on individual mono tracks. | Confirm the host and guest are on the intended tracks and both feed the main output. |
| [Audacity](https://manual.audacityteam.org/man/splitting_and_joining_stereo_tracks.html) | On an extracted stereo audio file, use Split Stereo to Mono to work on the two channels separately. | Retain the original start and duration when returning WAV files to a video editor. |
| [Valmera](https://valmera.io/long-video-ai-editing) | Upload a sync-checked recording with the dialogue mix you intend to publish, then brief the edit in chat. | Check the full export and a short clip. Listen for both speakers at named moments. |

Valmera publishes this guide. Tool descriptions come from public documentation. The three files test channel routing with local renders.

For a file whose first audio stream has a confirmed stereo layout, these FFmpeg commands extract its two channels to WAV while leaving the camera file intact. Swap the names if the recording uses the opposite assignments. [FFmpeg pan filter reference](https://ffmpeg.org/ffmpeg-filters.html#pan)

```sh
ffmpeg -i camera.mp4 -map 0:a:0 -af 'pan=mono|c0=FL' host-left.wav
ffmpeg -i camera.mp4 -map 0:a:0 -af 'pan=mono|c0=FR' guest-right.wav
```

If the source already contains one mono mix of both people, the left and right extraction will not give you the originals. If both microphones picked up the room, listen to the combined mix for echoes, phase problems and level jumps before using it in an edit.

## Give every editor the same acceptance test

> The host and guest were recorded on the left and right channels of the camera file. Preserve both voices at their original times. Export a full episode and one clip that includes both speakers. We will listen with headphones and in mono. Tell us which file contains the final dialogue mix and which files are the isolated tracks.

Use a representative passage with a quiet response, an interruption and an editor’s cut. Play the exports from the actual destination, including a phone speaker. Check the quiet response and both sides of the cut. If the job needs separate stems for a later remix, request and inspect them in addition to the delivered MP4.

For a recurring quote, send Valmera the number and length of episodes, the number of mic channels, the desired clips, and whether you need a delivery mix, separate stems or both. [Open the Enterprise inquiry](https://valmera.io/subscribe?inquiry=podcast-video-editing-service&utm_source=github.com&utm_medium=referral&utm_campaign=podcast_split_microphones#enterprise)
