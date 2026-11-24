# Outsource internal training video editing with a clean delivery package

Review everything that will reach learners: the MP4, its audio and metadata, the captions and transcript, the poster, the visible filenames, and any other versions you plan to publish. An editor can cover the correct field in every video frame while the same value remains in a separate caption or the file title.

Before sharing the pilot, use fictional material or two recordings your team has approved for the vendor. If the vendor should never receive a particular customer or employee detail, remove it in your own authorized environment before handoff. Agree on who may access the source, what the editor can retain, who approves the downloads, and who checks the final learner view.

## Find three leaks in a package with a clean picture

Both versions below use the same six-second [redacted sample recording](SCREEN-RECORDING-REDACTION-AUDIT.md#try-it-on-a-six-second-recording). Their 144 decoded picture frames match. Both videos are silent. The fictional value `DEMO-4276` appears in three other places in the first delivery.

| Surface | Failing package | Corrected package | What to check |
| --- | --- | --- | --- |
| MP4 title | [Video with the practice value in the title tag](examples/training-delivery-privacy/failed/lesson.mp4) | [Video with the title cleared](examples/training-delivery-privacy/corrected/lesson.mp4) | Inspect file properties or container metadata. The picture alone gives the same result in both files. |
| Separate caption | [Caption track with the practice value](examples/training-delivery-privacy/failed/lesson.vtt) | [Revised caption track](examples/training-delivery-privacy/corrected/lesson.vtt) | Display the first cue in learner view. The revised text removes the value and keeps the cue's timing. |
| Poster filename | [Poster with the practice value in its name](examples/training-delivery-privacy/failed/poster-DEMO-4276.jpg) | [Renamed poster](examples/training-delivery-privacy/corrected/poster.jpg) | Inspect the file list or delivery link. The poster image is identical. |

These synthetic files illustrate ways details can surface outside the picture. [See the decoded-frame and package checks](examples/training-delivery-privacy/measurements.json).

## Test your delivery review before sending the source batch

Download the [local practice-token checker](examples/training-delivery-privacy/check-practice-token.py) and the files above. Put the first three files in a folder called `failed` and the revised files in a folder called `corrected`. The checker uses Python 3 and FFprobe and reads local files. Run it from the folder containing both examples.

```sh
python3 check-practice-token.py failed DEMO-4276
python3 check-practice-token.py corrected DEMO-4276
```

The first run reports a match in the MP4 title, the first caption and the poster name. The second run finds none. Use only a distinct fictional marker for this rehearsal. The checker reads recognized text files, filenames and common media tags. Review the actual picture, sound, image contents, links, documents and embedded caption tracks separately. When testing a ZIP delivery, expand it in your approved workspace and check both the archive name and its contents.

After sign-off, have a second person open the exact files learners will see. Test the subtitles with audio off. Watch the opening, any blurred dialog, the transition into each new view and the final frame. Download the poster if the platform offers one. If approval includes a portrait edition, translated caption track or separate accessible version, add its own row to the delivery list. If you receive revisions, check the new files against the approved version before publishing.

## Ask vendors to quote the same two-lesson pilot

> Edit one short talking-head lesson and one short screen-recorded lesson using our approved sample source. Return the two MP4s and separate WebVTT files. Include the poster for each lesson. The mock screen identifier in the practice example is visible in the source and may be copied to other files. Keep the surrounding instructions legible. Show which parts of the delivery your team checks and return a revised package after one review round. Quote the recurring work with the same checks in scope.

At 52 edits per month, a four-wave schedule is 13 lessons per wave. If each has an MP4, captions and a poster, the reviewer receives 39 files each wave. Ask how long the approved wave takes after one round of corrections, which changes cost extra, who tests the delivered copies, and how the vendor handles deletion of files after the agreed period. Use the actual pilot to estimate review time and set deadlines. [Batch planning worksheet](PLAN-TRAINING-VIDEO-DELIVERY-CAPACITY.md)

Valmera offers done-for-you editing of existing training footage. To discuss a pilot, send the monthly volume, the types of footage, and the review requirements in your first note. Share an approved sample once you have agreed on the handoff. [Valmera’s training video editing service](https://valmera.io/training-video-editing-service?utm_source=github.com&utm_medium=referral&utm_campaign=training_delivery_privacy) · [Contact Valmera Enterprise](https://valmera.io/subscribe?inquiry=training-video-editing-service&utm_source=github.com&utm_medium=referral&utm_campaign=training_delivery_privacy#enterprise) · [Valmera’s published policies](https://valmera.io/legal#privacy)
