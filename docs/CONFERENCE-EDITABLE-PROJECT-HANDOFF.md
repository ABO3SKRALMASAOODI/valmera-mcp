# Outsource a conference edit and receive an editable project you can reopen

Ask for the project and its linked assets when your team will need to revise titles, captions, clips or speaker permissions after the event. The approved MP4 shows what went live. The editable package lets another editor change it after the vendor hands off.

The [IAMC-TMX conference post-production RFP](https://www.iamc.ca/request-for-proposals-video-editing-post-production-digital-content-services-iamc-tmx-line-wide-gathering/) asks for project files as well as captions, graphics and final exports. The same specification asks the buyer to retain ownership of the source footage and deliverables. Put the rights and handoff requirements in your brief before comparing quotes.

## Try a two-room media handoff

The sample uses two public synthetic room recordings. Both are named `camera.mp4` inside the package. The first edit segment takes three seconds from Room A at 00:04. The second takes three seconds from Room B at 00:06. Each file has its own approved hash.

Create a delivery folder with these files.

| Put this in the folder | Download it |
| --- | --- |
| `conference-recap.mlt` | [Editable MLT timeline](examples/conference-project-handoff/conference-recap.mlt?raw=1) |
| `approved-media.json` | [Approved source fingerprints](examples/conference-project-handoff/approved-media.json?raw=1) |
| `verify_project_handoff.py` | [Local video reference checker](examples/conference-project-handoff/verify_project_handoff.py?raw=1) |
| `room-a/camera.mp4` | [Room A recording](https://raw.githubusercontent.com/ABO3SKRALMASAOODI/valmera-mcp/05b32b8e666d7b4fb0704e976703803c2aa83b99/docs/examples/conference-session-exports/room-a.mp4) |
| `room-b/camera.mp4` | [Room B recording](https://raw.githubusercontent.com/ABO3SKRALMASAOODI/valmera-mcp/05b32b8e666d7b4fb0704e976703803c2aa83b99/docs/examples/conference-session-exports/room-b.mp4) |

Run this in that folder with Python 3.9 or later.

```sh
python3 verify_project_handoff.py conference-recap.mlt approved-media.json
```

Copy the folder to another directory and run the command there. On a disposable copy, replace the Room B file with the Room A file while keeping the same name. The checker reports the wrong footage even though the path exists. If the project points to the same Room A relative path for both clips, it reports that the approved Room B reference is absent.

The checker handles local AVFormat video references in MLT files. It checks path containment and file identity. Open the project in your editor to verify the timeline, plugins, fonts, captions and linked assets that are outside this check. [MLT XML format](https://www.mltframework.org/docs/mltxml/) · [Adobe Premiere Project Manager](https://helpx.adobe.com/premiere/desktop/organize-media/create-projects/copy-project.html)

## Accept the package on a second workstation

1. Specify the editing application and version that your team can open. Agree which camera originals, audio files, fonts, graphics and caption files the vendor will include and document their licenses.
2. Ask for the project and media in one organized folder. Preserve room, camera and session identifiers. Ask the vendor to record the approved source identities before shipping.
3. Copy the delivery to a different folder or workstation. Disconnect the original working drive after your copy completes. Open the copied project and make one small title change. Confirm the Room A and Room B segments show the intended speakers or slides, then export the test change.
4. Compare that test export with the approved MP4. Verify the title stays legible, the captions still line up, the room order is correct and the source files remain available for the next revision.
5. Quote the editable handoff explicitly. Compare the cost and delivery dates for the first pilot, the full batch, a review round and one later revision made from the package.

Valmera Enterprise edits footage your event team already captured. Include the editing application, room count, source hours, expected caption formats and project-file requirements when you [scope a conference editing pilot](https://valmera.io/subscribe?inquiry=conference-video-editing-service&utm_source=github.com&utm_medium=referral&utm_campaign=conference_project_handoff#enterprise). [Conference editing service](https://valmera.io/conference-video-editing-service) · [Multi-room delivery examples](OUTSOURCE-MULTI-ROOM-CONFERENCE-SESSION-EDITS.md)
