# Record a website demo for desktop and portrait

Record a separate portrait take when a website changes its layout at a narrow width. A desktop clip can show the whole workflow in one frame. A portrait capture may need an extra scroll and a longer pause on the result. Check both from the exported files before you send a demo to customers.

## The same click in two live browser layouts

Open Valmera’s [public slideshow builder](https://valmera.io/tools/ai-slideshow-maker#photo-sequence). The initial order is **Earthrise (2 s), Bootprint (3 s), Lunar module (1 s)**. Activate **Earlier** on the third photo, whose accessible button name is `Move photo 3 earlier`. The resulting order must be **Earthrise (2 s), Lunar module (1 s), Bootprint (3 s)**.

We ran that exact click in fresh Chromium sessions at two viewport sizes. The browser stayed on the same URL, and the duration moved with each photo in both cases. These screenshots are browser evidence. The [recorded landscape MP4](examples/website-photo-reorder/reorder.mp4) shows the same action in a Valmera export.

| Capture | Before and after | What the take needs |
| --- | --- | --- |
| Desktop, 1280 × 800 CSS px | [Before the click](examples/responsive-website-demo/desktop-before.png) · [Result](examples/responsive-website-demo/desktop-after.png) | All three cards sit on one row, with the action and result visible together. |
| Narrow portrait, 390 × 844 CSS px | [Before the click](examples/responsive-website-demo/portrait-before.png) · [Result](examples/responsive-website-demo/portrait-after.png) | The cards stack. Show the third card’s button, then hold where the second and third card labels and durations can be read. |

The desktop photo boxes span x = 313–967. A centered 9:16 crop of the 1280 × 800 viewport would cover x = 415–865, clipping the two outside boxes. In the narrow browser layout, all three images are 320 CSS px wide and fit between x = 35 and 355. You gain readable width for each card. You still have to show the relevant part of the vertical stack. [Browser measurements](examples/responsive-website-demo/measurements.json)

## Show the result in both exports

1. **Choose one task.** Write what changes on the page in terms a reviewer can spot with sound off. For this example, the result is “Lunar module is #2 at 1 second and Bootprint is #3 at 3 seconds.”
2. **Plan each width.** In landscape, show the full list before the click. In portrait, scroll to the third card, show its label and button, then make room for the two changed labels after the click. Check sticky headers, drawers and banners in the actual frame.
3. **Review the downloaded MP4.** Have a reviewer identify the old state, the click and the new state. Confirm they can read the labels without pausing or zooming. If the result needs more room, use two readable holds and a short step label. Reserve real-device testing for claims about Safari, Android or touch behavior.

> Record one landscape and one portrait MP4 from [public URL]. The viewer needs to learn [task]. Click [control or accessible name]. End by showing [exact changed values]. Let the page use its native layout at each width. In portrait, scroll or hold after the action so both values remain readable. Send the two previews and identify where each final MP4 shows the result.

Use a public page or a safe demonstration environment with sample data. If the workflow requires a private login, capture it in a session you control and supply the approved recording. For a clickable tour, evaluate preview and sharing separately from MP4 delivery. [Walnut mobile and desktop capture](https://help.walnut.io/help/demos/capture/mobile-and-desktop-apps) · [ArcDemo capture modes](https://chromewebstore.google.com/detail/arcdemo-interactive-demo/dagnalajbdbdmdgemcmdmlpnhliegkne)

**[Prepare a desktop or portrait brief in Valmera](https://valmera.io/tools/record-website-demo?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=responsive_website_demo#start-demo)**. Brief preparation and the public example are free. Starting a new site recording in Studio requires an eligible plan. If your team updates multiple demos after each release, [scope an Enterprise pilot](https://valmera.io/product-demo-video-editing-service?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=responsive_website_demo) with your workflows, target widths and review deadline.
