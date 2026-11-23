# Verify a batch of training videos and SRT captions before LMS upload

A correctly named subtitle file can still contain the captions from the previous edit. For a recurring training-video handoff, record a SHA-256 fingerprint for each approved MP4 and SRT at sign-off. Check the files again from the delivery folder before uploading. A mismatch names the exact lesson and file that needs attention.

## Run the check on an existing correction

This example reuses the [recorded caption revision](CAPTION-REVISIONS.md#correct-a-single-misheard-word-and-verify-the-downloaded-video). Its first and corrected SRTs are the same size, and either file could arrive under the same filename. The [approved manifest](evaluation/one-word-caption/approved-delivery.csv) pairs the final render with the corrected SRT.

From the repository root, with Python 3.9 or later:

```sh
sample=docs/evaluation/one-word-caption
delivery=$(mktemp -d)
cp "$sample/final.mp4" "$sample/corrected-words.srt" "$delivery/"
python3 docs/evaluation/verify_lesson_delivery.py "$sample/approved-delivery.csv" "$delivery"
cp "$sample/source-words.srt" "$delivery/corrected-words.srt"
python3 docs/evaluation/verify_lesson_delivery.py "$sample/approved-delivery.csv" "$delivery"
rm "$delivery/final.mp4" "$delivery/corrected-words.srt"
rmdir "$delivery"
```

The first run verifies one lesson. The second flags `corrected-words.srt` and returns status 1. The checker also reports missing, changed and unlisted MP4 or SRT files. It reads files locally. It compares byte identity and leaves playback, subtitle timing and LMS upload to your review.

## Use it for a first paid batch

1. Choose two representative lessons. Include a screen recording whose cursor action must remain visible and a second lesson that needs a caption terminology correction.
2. After playback approval, save one row per lesson in the CSV. Use filenames from the delivery root, with one MP4 and one SRT per lesson. Copy the SHA-256 values from the **approved** files using `shasum -a 256` on macOS or `sha256sum` on Linux. Save the CSV separately from the incoming folder.
3. Run the checker on the copy slated for upload. If the editor revises a lesson, approve its new video and captions before replacing the recorded fingerprints. Leave the other lessons' fingerprints in place.
4. Upload one verified pair to a test lesson and play it as a learner. Toggle captions, check the corrected term and watch a section after the edit for alignment. The test should use the LMS and device your team expects learners to use.

For a forty-video monthly target, send ten lessons per week as a planning assumption. Confirm how many approved pairs the editor can complete after one revision round, when the first set of files will be ready, and how much reviewer time your team needs. Use the [quote and capacity comparison](VIDEO-EDITING-SERVICE-QUOTE-CAPACITY.md) to turn the pilot times into a delivery plan.

Valmera offers done-for-you editing of existing training footage. [See the training video editing service](https://valmera.io/training-video-editing-service?utm_source=github.com&utm_medium=referral&utm_campaign=lms_delivery_verification) and [send your batch scope to Valmera Enterprise](https://valmera.io/subscribe?inquiry=training-video-editing-service&utm_source=github.com&utm_medium=referral&utm_campaign=lms_delivery_verification#enterprise). Include monthly volume, finished length, caption languages and one example of the format you need.
