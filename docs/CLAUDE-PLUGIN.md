# Valmera video editing plugin for Claude

Bring a recording, describe the result and refine your video through conversation. Valmera's Claude plugin combines an authenticated video editor with three editing skills: a complete edit, several shorts from a long recording, and a website or product walkthrough.

## Choose your installation route

The [Claude plugin 1.0.2 release](https://github.com/ABO3SKRALMASAOODI/valmera-mcp/releases/tag/claude-v1.0.2) includes `valmera-claude-1.0.2.zip`, a standalone package for manual upload. This is a Valmera repository release, not an approved Anthropic directory listing.

**Claude chat or Cowork:** download the ZIP from the release, then use **Customize → Plugins → Add → Upload plugin** in claude.ai. After installation, open the plugin's **Connectors** tab and connect Valmera. Complete sign-in with the Valmera account that owns your recording. Installing the skills and authenticating the editor are separate steps. Available controls depend on your plan and organization policies; an organization owner may need to add the connector first.

**Claude Code:** add Valmera's repository marketplace and install the plugin inside a Claude Code session:

```text
/plugin marketplace add ABO3SKRALMASAOODI/valmera-mcp
/plugin install valmera@valmera
```

Open `/mcp` and authenticate the Valmera connection. These commands follow the marketplace's current version; the downloadable ZIP is the fixed 1.0.2 package. If you already added Valmera as a separate MCP server, inspect your connections before enabling a second copy.

**Connection only:** follow the [Claude custom-connector guide](https://valmera.io/mcp/claude). That adds the editing tools without these bundled skills. Do not install another route just because an existing connection needs authentication.

## Start with your recording

Account creation and uploads are free. Editing requires a paid [Valmera plan](https://valmera.io/subscribe); Claude access and usage are separate. Installing the ZIP does not upload footage, buy credits or begin an edit.

1. Upload your recording in [Valmera Studio](https://valmera.io/studio), or choose an existing project. A file attached to a Claude conversation is not automatically in Valmera.
2. Ask Claude to list your Valmera projects and select the intended recording. An empty list can mean that connection works but this account has no projects yet. Wait for the selected source to finish analysis.
3. Describe the destination, length, framing, captions and sound. Establish the editing scope and cost expectations before billable work.
4. Review the rendered preview, request any corrections and export the approved version. A queued job is not a finished video.

Try this first-edit brief, changing the requirements to fit your footage:

```text
Use Valmera to edit the recording I select. Make a 45-second vertical video
with readable captions. Preserve the speaker's meaning and keep names accurate.
Confirm the project and cost expectations before billable work. Show me the
rendered preview, explain what changed, and wait for approval before export.
```

## Three workflows

| Skill | Use it for | Review before delivery |
| --- | --- | --- |
| `edit-video-with-valmera` | A chosen recording with cuts, captions, framing, sound or visual treatments | Meaning at cuts, text, framing, sound and the approved version |
| `turn-long-video-into-shorts` | Interviews, podcasts, talks and webinars | Each clip's source range, beginning, ending and standalone meaning |
| `website-demo-video` | A public website walkthrough or uploaded screen recording | Approved pages and actions, private information, narration and final sequence |

In Claude Code, the skills use the `valmera` namespace, for example `/valmera:edit-video-with-valmera`. In chat, ask Claude which Valmera skills are available, then name the workflow in your request. Skills supply instructions; the connected Valmera server performs edits. See the [workflow guide and starting prompts](https://valmera.io/mcp/skills).

## When something is missing

| What you see | Next step |
| --- | --- |
| Skills appear, but no editing tools | Open the plugin's Connectors tab in chat/Cowork, or `/mcp` in Claude Code, and complete authentication |
| Tools appear, but the skills do not | Confirm you installed the plugin, rather than only adding a custom connector; refresh the session and inspect the installed version |
| The ZIP is rejected | Upload the release asset unchanged; `.claude-plugin/plugin.json` must remain at its root |
| Your project does not appear | Check the Valmera account and upload completion; do not guess a project ID |
| A render stays queued or running | Follow the existing job; do not launch duplicate renders while it is active |
| Preview ready, but no final download | Approve export of the reviewed version, follow that job and retrieve the final link |

For authentication errors, use [connection troubleshooting](https://github.com/ABO3SKRALMASAOODI/valmera-mcp/blob/main/docs/CONNECTION-TROUBLESHOOTING.md).

## Package, data and verification

The standalone ZIP contains the manifest, HTTPS MCP configuration, icon, this README, MIT license and three skill files. It has no install scripts, hooks, executable server or bundled dependencies. The repository also contains maintenance scripts and packages for other clients; those are excluded from this ZIP.

The connector sends editing requests and tool arguments to `https://valmera.io/mcp/server` after authentication. Valmera returns project information, transcripts, sampled frames and preview/export links to the connected Claude session. Uploads and edits remain in your Valmera account; editing creates versions without overwriting the original. Review the [privacy policy](https://valmera.io/legal#privacy). Support: [support@valmera.io](mailto:support@valmera.io).

Package validation checks file structure and metadata, not editing quality or directory approval. The release notes state the checks actually performed. Authenticated installation and an end-to-end paid edit in each Claude surface have not been verified for this package. The [trim-and-reframe example](https://valmera.io/examples/trim-and-reframe) documents a separate recorded editing result.

The setup follows Anthropic's [plugin structure and testing guidance](https://claude.com/docs/plugins/build). Public directory distribution has its own [submission and review process](https://claude.com/docs/directory/publish).
