# Can you upload and edit a long 4K video before your deadline?

A 20 GB recording takes **1 hour, 6 minutes and 40 seconds** to transfer at a sustained 40 Mbps. If review is two hours away, that leaves 53 minutes and 20 seconds for the editor to index the file, produce a preview and let you review it. A full-resolution export adds time after the preview. Estimate each stage before committing a large project to a new online editor.

[Download the offline upload planner](examples/long-video-upload-plan/upload-deadline-planner.html) · [Start with Valmera’s long-video workflow](https://valmera.io/long-video-ai-editing?utm_source=github.com&utm_medium=referral&utm_campaign=long_video_upload_deadline)

## Work backward from the preview or delivery time

Open the [planner file](examples/long-video-upload-plan/upload-deadline-planner.html) in GitHub, use **Download raw file**, then open the saved HTML in your browser. Enter the total file size, your measured upstream speed and the post-upload time you need to protect. It runs without selecting, reading or uploading any media.

| Example | Transfer time | What remains |
| --- | ---: | --- |
| 20 GB at 40 Mbps, review in 2 h | 1 h 06 m 40 s | 53 m 20 s for everything after transfer |
| 20 GiB at 40 Mbps, review in 2 h | About 1 h 11 m 35 s | About 48 m 25 s after transfer |
| 50 GB at 20 Mbps, review in 3 h | 5 h 33 m 20 s | Transfer misses review by 2 h 33 m 20 s |
| 50 GB, review in 3 h, 45 m reserved for editing and review | Requires at least 49.39 Mbps sustained | 2 h 15 m budgeted for transfer |

Multiply bytes by eight and divide by sustained bits per second. A decimal GB is 1,000,000,000 bytes. A GiB is 1,073,741,824 bytes. Use byte size or the unit shown by your file tool. Write down when the upload **actually** completes. A fast download speed or short connection burst can overstate the sustained rate to an editor. A short representative upload helps measure that rate.

## Test the bottleneck you actually have

1. **Size or duration.** Check the candidate’s current per-file and per-project limits. Note the longest recording, the largest file, the codec and the total project runtime separately. Confirm the editor can work on the last quiet or visual event you need from the recording.
2. **Time to first preview.** Use a representative excerpt made from the same camera source. Measure transfer, media readiness and preview time independently. An excerpt verifies the format and editing task. Run a full-length pilot when you need to verify long-file limits, indexing coverage, sustained speed or recovery after an interrupted transfer.
3. **Delivery.** Ask for one specific revision and download a final native-resolution export. Check the smallest caption or detail that needs to remain readable and whether the last scene is present. Include revision, render and download time when your deadline is for delivery.

Keep the original files. Use a tiny review copy only when you know how to reconnect the approved cut to the originals before final rendering. If you split a long source around a file limit, record the original time range and filename of each part. Check one cut on each side of the split.

## Match the workflow to the delivery

| Workflow | Published workflow | Pilot question |
| --- | --- | --- |
| [Valmera long-video editing](https://valmera.io/long-video-ai-editing) | Upload existing footage and request cuts, captions, highlights or a revised preview by chat. Valmera describes its final export as rendering from the original. | Can the editor include a moment near the end of your source and revise one earlier passage while preserving the other cuts? |
| [VEED uploads](https://support.veed.io/en/articles/10657034-how-to-upload-video-audio-music-or-image-files) and [exports](https://support.veed.io/en/articles/10531327-how-to-export-your-project) | Browser editor with separate upload and export guidance and multiple quality choices. | Can your account accept the source and export the required size? Time every step on the same file. |
| [Adobe Premiere proxy workflow](https://helpx.adobe.com/premiere/desktop/organize-media/ingest-proxy-workflow/ingest-and-proxy-workflow.html) | Create smaller copies for editing, then reconnect originals for final export. | For a tight upload window, can you keep the originals and final render local? Confirm the export uses the sources intended for delivery. |

For ongoing high-volume editing, send the size and length of a typical recording and the largest one, the weekly cadence, where the source lives, and your required preview and final turnaround. Ask for a one-file pilot before committing the month’s footage. [Discuss recurring long-video editing with Valmera Enterprise](https://valmera.io/subscribe?inquiry=long-video-ai-editing&utm_source=github.com&utm_medium=referral&utm_campaign=long_video_upload_deadline#enterprise)
