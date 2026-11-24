# Check multicamera audio sync before editing a long recording

Match the same three events in both recordings before you cut a long interview, podcast or conference. A fixed shift moves all three matches by the same amount. A clock-rate correction changes how far apart they are. Fit the first and last events, then use the middle one to see whether a single correction is credible.

[Download the three-anchor sync check](examples/multicam-sync-check/check-camera-sync.html) · [Edit an aligned long recording in Valmera](https://valmera.io/long-video-ai-editing?utm_source=github.com&utm_medium=referral&utm_campaign=three_anchor_multicam_sync)

## Run the check before exporting a long pilot

1. Pick a camera or master track to use as the reference. Choose a shared clap, a visible sound on both scratch tracks, or another clear event near the start, middle and end.
2. Read the matching elapsed timestamps in each original file. Download the HTML file using **Download raw file** on GitHub and open it in your browser. Enter the six times. It runs offline.
3. Set a tolerance suitable for your job and the precision of your measurements. At 30 fps one frame is about 33.33 milliseconds. Use a waveform or matching transients when the needed tolerance is smaller than a frame.
4. Review the opening shift, then read the middle and closing differences. If these exceed your tolerance, check whether the suggested speed and shift also fit the middle. When a single speed misses a reliable middle match, look for a restart, a dropped interval or a wrong anchor. Align uninterrupted spans separately when the sources require it.

The speed estimate divides the second recording’s outer interval by the reference interval. A second recording taking 600.30 seconds to cover 600.00 reference seconds needs about **100.05%** speed over that interval. After changing speed, align the opening event again and check the middle and end. Use additional matches near suspected recording changes.

## Check the result against a measured example

The calculator’s practice data comes from a synthetic two-hour camera and external microphone fixture. After aligning the opening, the mic arrives **449 ms late** in the middle and **898 ms late** near the end. The outer anchors imply a speed of **100.0125%**, with about **0.13 ms** remaining at the held-out middle match. The separate verified render placed the decoded microphone beep within one millisecond of all three flashes. [Fixture, outputs and measurement method](FIX-AUDIO-DRIFT-IN-LONG-RECORDINGS.md)

[Listen to the end with an opening shift only](examples/audio-drift-two-hour/start-aligned-last-anchor.mp4) · [Listen to the end after rate correction](examples/audio-drift-two-hour/rate-corrected-last-anchor.mp4)

The calculator compares the points you enter. Check the source waveforms and the completed export independently. A match at three anchors can miss an interruption between them.

## Compare an editor on the part of the job you need

| Tool or workflow | What the vendor documents | What to ask for in a trial |
| --- | --- | --- |
| [ChatCut Multicam Editor](https://chatcut.io/docs/multicam-edit) | Aligns separate recordings with offsets and can draft a speaker-cut timeline over program audio. Its [sync guide](https://chatcut.io/blog/how-to-sync-audio-and-video) describes checking for changing offsets before retiming. | Ask for the alignment report and confirm the held-out middle cue. Request continuous program audio while one camera changes. |
| [Clam Sync](https://clamsync.com/) | A sync and handoff utility that describes clock correction and export to Premiere Pro, Final Cut Pro and DaVinci Resolve. | Import a sample in the destination editor. Recheck sync at the end and after any recording break. |
| [DaVinci Resolve Fairlight](https://documents.blackmagicdesign.com/UserManuals/DaVinci-Resolve-18-Fairlight-Audio-Post.pdf) | Elastic Wave controls for adjusting audio timing. | Work on a copy of a short section. Record the actual anchors and check that the spoken delivery still sounds natural. |
| [Valmera](https://valmera.io/long-video-ai-editing) | Upload long footage, describe the edits, review the cut and export. | Start with a sync-checked master. Ask for one cut over a camera change, then verify that the original voice and the next action stay aligned. |

Valmera publishes this guide. The comparison describes public workflows, and the timing example tests a controlled fixture.

> Keep the time-aligned master audio and make the requested camera switch. Preserve the complete following sentence. Export a review MP4 and tell us where the three reference events now occur in the cut so we can check the actual delivered file.

[Open Valmera’s long-form editor](https://valmera.io/long-video-ai-editing?utm_source=github.com&utm_medium=referral&utm_campaign=three_anchor_multicam_sync). AI editing requires an eligible subscription. To get a recurring production quote, [send Valmera Enterprise your source mix, episode length and review dates](https://valmera.io/subscribe?inquiry=podcast-video-editing-service&utm_source=github.com&utm_medium=referral&utm_campaign=three_anchor_multicam_sync#enterprise).
