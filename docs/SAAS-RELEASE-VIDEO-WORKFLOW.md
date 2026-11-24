# Choose a SaaS release video workflow for weekly updates

A changelog clip shows what shipped in a specific release. A help-center walkthrough teaches today’s steps. If you use one editable project for both, publish the release MP4 as a separate, dated file. Let the help-center player point to the latest approved walkthrough. Replacing a shared file can quietly change a release note people still use as a record.

## Compare tools by what actually needs to change

| Workflow | When to shortlist it | What to prove in a one-release pilot |
| --- | --- | --- |
| **Demofy** | You want short, narrated clips of public features, with published release clips preserving the product as it appeared on release day. Demofy documents live-product capture from a URL and a description, with narration edits. [Release-notes workflow](https://demofy.io/use-cases/release-notes-videos) | Open the old changelog after publishing the second clip. Cycle through both and verify that each shows the appropriate screen and result. Test the actual links your changelog will use. |
| **Storyship** | You want a narrated draft from either a public URL, a Chrome tab you can already access, or an existing recording. Storyship documents an editable narration workflow and click-based zooms. [Capture paths and editing](https://storyship.app/) | Use a sample account with your real permission levels. Make a wording correction after the first export. Verify that the exact UI action still appears at a readable size and the narration describes it correctly. |
| **Redemo** | You want selected walkthroughs to re-record when your product changes. Redemo describes an opt-in update path for approved flows and retaining the previous version if a check or render fails. [Automatic updates and publication history](https://redemo.io/) | Move a control on a non-customer test build, then test a broken path. Check which version a fresh viewer actually receives and how a team member is notified. Keep release-day copies outside the automatic update path. |
| **Valmera** | You have the footage, or can capture a public flow, and want a specific cut or revision that keeps the important click and result. For recurring editing from team-supplied footage, ask Valmera Enterprise to scope the batch. [Recorded click revision](RECORD-A-LOCALHOST-PRODUCT-DEMO.md) · [Done-for-you scope](SAAS-DEMO-EDITING-SERVICES.md) | Send the editor an old export, a new take and one focused revision. Approve the click and outcome from the downloaded MP4. Ask who maintains the two publication destinations. |

Provider capabilities above come from their own documentation. The downloadable test below verifies delivery of the Valmera examples. It is an edit of a recorded workflow and a test of the two-file publishing rule.

## Test the archive and the live walkthrough separately

The two example files are cuts of the same recorded Valmera documentation walkthrough. Use the [earlier cut](examples/product-demo-refresh/earlier-cut.mp4) as the archive and the [revised captions walkthrough](examples/uae-bilingual-video-editing/product-demo.mp4) as the current copy. In the revised cut, check that the viewer can see the pointer reach **Captions** and the resulting page heading. The two cuts do not represent different versions of the app.

From the repository root, verify the archive URL against the archive file, then verify the current URL against the current file. In the third command, deliberately point the archive check at the current URL to model an accidental replacement.

```sh
base=https://raw.githubusercontent.com/ABO3SKRALMASAOODI/valmera-mcp/30ffe202b73002fcb0914fcdf960360d4c6be8d3
archive=docs/examples/product-demo-refresh/earlier-cut.mp4
current=docs/examples/uae-bilingual-video-editing/product-demo.mp4

python3 docs/evaluation/verify_published_demo.py --approved "$archive" "$base/$archive"
python3 docs/evaluation/verify_published_demo.py --approved "$current" "$base/$current"
python3 docs/evaluation/verify_published_demo.py --approved "$archive" "$base/$current"
```

The expected sequence is **match**, **match**, **different**. Both URLs serve playable files. The last check detects that an archived location would serve the wrong bytes. For a hosted player that transcodes uploads, compare the provider’s downloadable rendition to its approved counterpart and watch both viewer-facing embeds. Check captions, chapter links and the visible outcome in each one.

## Send a scope that can be quoted

If four monthly releases each call for a changelog MP4 and a help-center MP4, scope **eight MP4s per month**. Add any caption files, portrait cutdowns or additional languages on their own lines. Give each output an owner, an approval deadline and a publication destination. Decide who tests the old changelog after the new release is live.

> For our pilot, we’ll send the older export and a recording of the new step. Return a dated changelog MP4 and a separate help-center MP4. Each must show the correct action and result on mute. After the first review, we’ll request one wording correction and check both files. Quote monthly volume separately from delivery to the existing embeds.

[Request an Enterprise quote](https://valmera.io/subscribe?inquiry=product-demo-video-editing-service&utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=saas_release_video_pilot#enterprise) or [email the release-video brief](mailto:support@valmera.io?subject=Enterprise%20editing%20inquiry%20-%20weekly%20SaaS%20release%20videos&body=Company%3A%0ACountry%3A%0AReleases%20per%20month%3A%0AMP4s%20per%20month%3A%0AFormats%20and%20caption%20languages%3A%0AFirst%20publish%20deadline%3A%0AOne%20public%20example%20link%3A).
