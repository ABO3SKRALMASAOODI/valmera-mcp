# Edit recorded video in Kiro with the Valmera power

Use Kiro’s custom-power installation to connect the hosted Valmera MCP server. The package supplies the connection and a first-edit skill. Editing runs through your authenticated Valmera account. The power contains no credentials.

## Import the public power

1. In the Kiro IDE, open **Powers** and choose **Add Custom Power**.
2. Choose **Import power from a repository URL**. In some versions this appears as **Import power from GitHub**.
3. Paste the public [Valmera power folder](https://github.com/ABO3SKRALMASAOODI/valmera-mcp/tree/main/powers/valmera-video-editor) and choose **Install**.
4. Ask Kiro to list your Valmera projects. When the connector asks for account access, sign in to your Valmera account and complete the authorization in the browser. Return to Kiro and retry the project list.

Kiro documents importing a repository subdirectory and namespacing MCP servers installed with a power. Its MCP client supports streamable HTTP and OAuth. The configured server is `https://valmera.io/mcp/server`. You can also connect it as a plain remote MCP server using Kiro’s workspace or user settings. [Install custom powers](https://kiro.dev/docs/powers/installation/#install-custom-powers) · [Kiro MCP configuration](https://kiro.dev/docs/mcp/configuration/)

## Try one focused edit

[Upload or open a short sample in Valmera Studio](https://valmera.io/studio?utm_source=github.com&utm_medium=referral&utm_campaign=kiro_video_editing_power). Use a recording that you are allowed to edit.

> Use Valmera to find my “Demo interview” project. Inspect the transcript and show me the start and end of the answer about pricing. Make a preview that keeps that complete answer, adds captions and leaves the following answer in place. Share the preview for review.

Try one revision, such as keeping an extra half-second before the answer. Compare the revised preview with the first version. When the reviewed cut is ready, ask for the MP4. [Watch a public edit and revision](MCP-RECORDED-EDIT.md) · [Review the Valmera MCP endpoint and tool declarations](CONNECTION-TROUBLESHOOTING.md#check-a-directory-listing-without-signing-in)

Your organization may manage MCP access in Kiro. Valmera editing requires eligible account access. If the project list connects while editing is unavailable, check your Valmera account’s access and the current [Valmera connection guide](https://valmera.io/mcp/connect?utm_source=github.com&utm_medium=referral&utm_campaign=kiro_video_editing_power).

The package is available as a custom import from the public repository. Kiro’s curated registry reviews entries through a separate publisher submission. [Kiro registry submission](https://kiro.dev/registry/submit/?type=power)
