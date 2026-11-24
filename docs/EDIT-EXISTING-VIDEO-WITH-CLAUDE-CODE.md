# Edit an existing video with Claude Code and verify the MP4

Claude Code can drive an editor or a local rendering command. For an existing recording, give it the source file or project, a list of source-time ranges, and the output format. Then check the rendered file at the cuts. Use FFmpeg for file-based jobs with precise instructions, Valmera for a hosted review-and-revise workflow, ProofCut for local transcript-led editing, or Remotion for repeatable layouts built in React.

## Play the same revision in two workflows

The [25-second source recording](https://valmera.io/examples/trim-and-reframe/original-source.mp4) is a silent motion graphic with a clock burned into every frame. The first cut kept 00:03–00:07, 00:12–00:16 and 00:19–00:23. The revision shortened only the middle shot to 00:12–00:14. Both cuts use a centered square crop. Endpoints are exclusive.

- **Valmera MCP.** [Watch the first preview](https://valmera.io/examples/agent-revision/first-preview.mp4#t=6) and [watch the revised export](https://valmera.io/examples/agent-revision/revised-final.mp4#t=6). Codex drove the Valmera MCP session for this [recorded edit](MCP-RECORDED-EDIT.md). The final file runs 15 seconds, with 10 seconds of retained footage and a five-second end card.
- **FFmpeg.** [Play or download the local revision](examples/claude-code-timestamp-edit/local-revision.mp4). It runs 10 seconds at 360 × 360 and 30 fps. All 300 decoded frames match the corresponding normalized source frames. [Download the measurements](examples/claude-code-timestamp-edit/measurements.json).

The sample verifies picture timing and framing. For footage with sound, listen across both seams and check dialogue, sync and any fades before accepting the result. The playback links show recorded renders, and the local command below reproduces the picture cut. ProofCut and Remotion are included using their published workflows.

## Choose how the MP4 gets made

| Route | When to use it | Where to check the result |
| --- | --- | --- |
| **Claude Code with FFmpeg** | Your media stays on your machine and the job is a precise file transform. Claude Code can prepare a command for you to review and run. | Inspect the command and decode the MP4. The command below gives you the revised file directly. [FFmpeg trim documentation](https://ffmpeg.org/ffmpeg-filters.html#trim) |
| **Claude Code with Valmera MCP** | A team wants to upload footage, review a rendered cut and ask for targeted changes in conversation. The hosted service takes care of the render. Editing requires an eligible paid account. | Compare the rendered preview with the approved export. [Claude Code connection](https://valmera.io/mcp/claude-code) · [Recorded session](MCP-RECORDED-EDIT.md) |
| **Claude Code with ProofCut** | You want local, transcript-led editing with a Claude Code plugin. Its documented workflow uses local media dependencies and can also export an OpenTimelineIO or Kdenlive project. | Its documentation shows MP4 render and a verification command that compares the rendered words with the edit. [ProofCut setup and demo](https://github.com/tydude001/proofcut) |
| **Claude Code with Remotion** | You have a React project and want to repeat a layout, labels or graphics across many recordings. | Review the composition and render its MP4. The video component documents which source frames to start and stop on. [Video component](https://www.remotion.dev/docs/offthreadvideo) · [Render command](https://www.remotion.dev/docs/cli/render) |

## Give the agent two separate instructions

First cut:

> Work from a copy of the supplied recording. Keep source times 00:03–00:07, 00:12–00:16 and 00:19–00:23, in that order. Use a centered square crop. Treat the ends of ranges as exclusive. Render the first cut to a new file and report the duration and the first source frame of each shot.

Revision:

> In the first cut, shorten only the middle shot by two seconds. End it at source time 00:14. The first and last source ranges, their crop and their order must stay the same. Render the revision to a separate MP4 and report the frame before and after each cut.

Say explicitly whether an end card belongs in the total duration. A clean result can be checked on two clocks. The program clock starts at zero and continues through the cut. The source clock jumps to the file position of the next retained frame.

## Check the frames on either side of each cut

| Program frame, counted from zero | Expected source frame | What it checks |
| ---: | ---: | --- |
| 0 | 90 | Starts at 00:03 |
| 119 → 120 | 209 → 360 | First seam stays put |
| 179 → 180 | 419 → 570 | Shortened middle shot ends just before source 00:14 |
| 299 | 689 | Ends just before source 00:23 |

At 30 fps, the revision jumps to source 00:19 at program 00:06. The first preview makes that jump at program 00:08. Scrub both renders at program 00:06 to see the difference.

## Reproduce the picture revision with FFmpeg

Download [original-source.mp4](https://valmera.io/examples/trim-and-reframe/original-source.mp4) and run this in the directory containing the file. The frame indices and crop are for this specific silent, 30 fps sample. The lossless setting makes a decoded-frame comparison possible.

```sh
ffmpeg -n -hide_banner -i original-source.mp4 \
  -filter_complex '
    [0:v]crop=720:720,scale=360:360,setsar=1,split=3[a][b][c];
    [a]trim=start_frame=90:end_frame=210,setpts=PTS-STARTPTS[first];
    [b]trim=start_frame=360:end_frame=420,setpts=PTS-STARTPTS[middle];
    [c]trim=start_frame=570:end_frame=690,setpts=PTS-STARTPTS[last];
    [first][middle][last]concat=n=3:v=1:a=0[out]
  ' \
  -map '[out]' -an -c:v libx264 -preset fast -crf 0 -pix_fmt yuv420p \
  -movflags +faststart local-revision.mp4
```

Run `ffmpeg -v error -i local-revision.mp4 -map 0:v:0 -f framemd5 -` to produce one checksum per decoded frame. For the source, apply `-vf 'crop=720:720,scale=360:360,setsar=1,format=yuv420p'` before generating the checksums. Compare the output checksum column to source ranges 90–209, 360–419 and 570–689, in that order. For a source with a variable frame rate or an audio track, read its timestamps and specify the sound edit before adapting this command.

## Test a paid workflow on your own footage

Ask for a first cut, one change at an exact source time, and a finished file. Track minutes spent by the reviewer, whether untouched shots survived, and whether the exported file matches the approved preview. Run that test on a real recording before committing to a recurring workflow.

- **Edit in conversation.** [Open Valmera’s edit-by-chat workflow](https://valmera.io/edit-video-by-chatting-with-ai?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=claude_timestamp_edit) or [connect Claude Code](https://valmera.io/mcp/claude-code?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=claude_timestamp_edit).
- **Hand off recurring editing.** [Contact Valmera Enterprise](https://valmera.io/subscribe?inquiry=product-demo-video-editing-service&utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=claude_timestamp_edit#enterprise) with the monthly volume, two sample recordings and one approval requirement the team needs to meet.
