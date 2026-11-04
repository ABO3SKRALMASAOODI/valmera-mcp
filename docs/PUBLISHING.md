# Maintaining Valmera's MCP directory listings

This is the publication and verification guide for the public documentation repository. Last checked November 4, 2026. Public listings are external records: a file update or a submitted form does not prove that a directory has refreshed, accepted or ranked the product.

## Source of truth

Verify these before publishing product claims:

- [Live server card](https://valmera.io/.well-known/mcp/server-card.json): endpoint, authentication, enabled tool groups, session tools and explicit exclusions.
- An authenticated connection's `tools/list`: tool names, argument schemas and constraints available to that account.
- [Plans](https://valmera.io/subscribe): current access terms and included credits.
- [File uploads](https://valmera.io/docs/file-uploads) and [exports](https://valmera.io/docs/publishing): input and delivery behavior.

The public endpoint is `https://valmera.io/mcp/server`. The older `entrepreneur-bot-backend.onrender.com/mcp` address serves the same service, but every listing should use the branded endpoint. MCP clients can export the final MP4 with `export_final` and `download_url`, and Studio export is still available. Account creation and uploads are free and editing requires a subscription. Don't put prices, trials or credit grants in directory copy; link to https://valmera.io/subscribe instead.

Avoid a fixed undated tool count in directory descriptions. Configuration can change the catalog. If a count is useful, attach the date and link to the live server card.

## Verified state on November 4, 2026

| Surface | Verified result | Next action |
| --- | --- | --- |
| [Official MCP Registry](https://registry.modelcontextprotocol.io/v0.1/servers?search=valmera) | `io.valmera/video-editor` version `0.2.0` is active and latest; its sole remote is `https://valmera.io/mcp/server`. Versions `0.1.0` and `0.1.1` are deprecated | Maintain the current record; a stale mirror does not require another registry version |
| [Glama repository listing](https://glama.ai/mcp/servers/ABO3SKRALMASAOODI/valmera-mcp) | Author verified; listing name, description and Valmera thumbnail updated | Maintain the owned listing and public README |
| [Glama hosted connector](https://glama.ai/mcp/connectors/io.valmera/video-editor) | Ownership verified; Healthy; OAuth works in Glama; tool-definition quality B, 3.3/5 | Use the connector's current public evaluation when describing its status |
| [Domain verification file](https://valmera.io/.well-known/glama.json) | Public HTTPS JSON verified by Glama | Keep this public claim file published to retain verification |
| [Awesome Remote MCP Servers](https://github.com/punkpeye/awesome-remote-mcp-servers#multimedia) | Valmera is already listed under Multimedia with its endpoint, OAuth marker and connector badge | Maintain this existing entry; do not submit a duplicate |
| [Older Awesome MCP Servers submission](https://github.com/punkpeye/awesome-mcp-servers/pull/11560#issuecomment-6634448930) | Public follow-up posted with verified ownership, hosted evaluation and the existing remote-directory entry | Follow the current contribution scope, which routes remote-only services to the remote directory |
| [MCP Servers](https://mcpservers.org/servers/abo3skralmasaoodi/valmera-mcp) | README refresh requested; the UI acknowledged the request, but the refreshed copy was not yet visible | Verify the public copy before repeating a request |
| [MCPBeat](https://mcpbeat.com/mcp-servers/valmera/video-editor/) | Owner confirmed through the public repository verification file; the official setup guide is published beside the connection configuration. The generated command still prefers the legacy backend address. [Ownership follow-up on issue #3](https://github.com/mcpbeat/best-mcp-servers/issues/3#issuecomment-6642732264) is published | The owner dashboard exposes the setup-guide link, not an endpoint editor. Maintainer correction remains pending; do not submit a duplicate |
| [Odel](https://odel.app/modules/valmera/video-editor) | Branded endpoint and version are current; the mirrored README is older and the AI assessment says the editor only reads information. Tools could not be listed without sign-in | The live-check control returned an expected sign-in requirement but did not correct the assessment. No correction submission is confirmed; locate a supported maintainer correction route |
| [ExtOps](https://extops.dev/plugins/mcp/io.valmera/video-editor) | A correction request about the “Not responding” label received an explicit success acknowledgment through its feedback form | Public correction remains unverified. Preserve the existing submission; do not repeat it merely because the label persists |

The latest registry record was published at `2026-10-05T21:42:45.941368Z`. The older records were marked deprecated on October 7, with status messages pointing to the branded endpoint. These facts supersede the September registry observation below. A directory may retain historical endpoints for monitoring; its new-client setup instructions should use the active/latest record.

MCPBeat ownership was confirmed using [`mcpbeat-verification.txt`](../mcpbeat-verification.txt), published in [PR #12](https://github.com/ABO3SKRALMASAOODI/valmera-mcp/pull/12). Keep the public proof file available. The owner dashboard acknowledged saving [the official setup guide](https://valmera.io/mcp/setup), and the public listing showed both that link and the owner-confirmed badge. Those two changes are complete; the generated endpoint correction is not. Verify the generated command itself before updating that status.

The hosted connector's grade is separate from the repository's deployable-package grade. This repository contains documentation, configuration and skills for the hosted service; its package grade remains ungraded. Do not report the connector's B grade as a repository-package evaluation.

Glama's connector listing currently preserves its manually maintained name, description and endpoint when registry marketing metadata changes. Technical connection settings still sync. If the service endpoint changes, update both the registry and the owned listing.

The [interactive editing brief builder](https://valmera.io/prompts#prompt-builder) and [creator workflow guide](CREATOR-WORKFLOWS.md) provide useful first-project links for listings. Two Valmera-authored tutorials are also public on DEV: [the MCP review workflow](https://dev.to/valmera/a-reviewable-workflow-for-ai-video-editing-through-mcp-85j) and [the six-field prompt workflow](https://dev.to/valmera/write-a-better-ai-video-editing-prompt-six-fields-one-brief-4258). These are our own publications, not independent endorsements.

## Changes on October 6, 2026

- `server.json` version `0.2.0` moves the registry remote to the branded endpoint `https://valmera.io/mcp/server` and drops the outdated "final export in Studio" wording.
- `smithery.yaml` now uses the branded endpoint and accurate export behavior.
- The README, `docs/CLIENTS.md`, `docs/TOOLS.md` (143 tools per the live server card) and `docs/PROMPTS.md` were rewritten or added.
- At that date, the Glama ownership claim and maintainer review of PR #11560 were still open. See the November 4 verification record above for the current state.

## Earlier record: public state on September 5, 2026

| Surface | Observed state | Follow-up |
| --- | --- | --- |
| [Public GitHub repository](https://github.com/ABO3SKRALMASAOODI/valmera-mcp) | Exists; its old README still described free credits, a trial and MCP final exports | Publish the reviewed documentation correction, then verify the default-branch content |
| [Official MCP Registry search](https://registry.modelcontextprotocol.io/v0.1/servers?search=valmera) | `io.valmera/video-editor` version `0.1.0` is active and latest; published August 5, 2026 | Publish revised metadata as a new version after authorization; verify the returned public record |
| [MCP Servers listing](https://mcpservers.org/fr/servers/abo3skralmasaoodi/valmera-mcp) | Listing exists and reproduces the old README; a request-update control is present | After the source correction is public, request refresh and verify the refreshed page |
| [Glama server listing](https://glama.ai/mcp/servers/ABO3SKRALMASAOODI/valmera-mcp) | Mirrors the old README; license not detected, quality untested, owner unverified | Publish the reviewed metadata and license-format correction, then complete claim and verify a fresh scan |
| [Glama hosted connector](https://glama.ai/mcp/connectors/io.valmera/video-editor) | Exists; listed as unhealthy and grouped under No Auth, although the endpoint requires authentication | Review authenticated health details with Glama; an anonymous HTTP 401 is not an authorized health test |
| [Awesome MCP Servers submission](https://github.com/punkpeye/awesome-mcp-servers/pull/11560) | Existing PR updated with accurate paid-editing and Studio-export wording; automated check replaced missing-glama with has-glama | Glama quality evaluation and maintainer acceptance remain outstanding |
| [appcypher/awesome-mcp-servers](https://github.com/appcypher/awesome-mcp-servers) | Archived and read-only since August 1, 2026 | Not accepting new submissions; do not create a duplicate fork merely to claim a listing |
| Smithery, PulseMCP and other directories | This revision does not establish a completed submission or a current public listing | Inspect the actual directory before creating a duplicate or claiming success |

The earlier guide's statement that the official registry was empty was a dated observation from before the August 5 publication. It is no longer the current state. Existing listings can be discovered through more than one route; do not assume an undocumented ingestion schedule.

## Publish a documentation correction

1. Review the README, workflow guide, `server.json`, `smithery.yaml` and `glama.json` against the current product and maintainer identity.
2. Check that every documented tool example is available and every linked product route resolves.
3. Publish the reviewed source changes using the repository's normal authorization and review process.
4. Read the default-branch files again and record the commit identifier.
5. Ask directories that mirror the repository to refresh. Verify their public content separately; source publication is not a refresh receipt.

No website deployment or production database operation is needed to edit this repository's documentation.

## Publish registry metadata

The official registry's [publisher documentation](https://github.com/modelcontextprotocol/registry/tree/main/docs) is the source for the current publishing and namespace-verification process. Re-read it before using publisher commands; older command examples and authentication details in previous versions of this guide may no longer apply.

Use the version and description in the reviewed `server.json`; editing that file does not publish a registry version. Use the official publisher's supported authentication for the `io.valmera` namespace and validate the manifest before publishing. Keep authentication material out of repository files and logs.

After publication, inspect the registry's public response and verify all of:

- Name is `io.valmera/video-editor`.
- Version is the intended new version.
- Status is active and the version is marked latest.
- Endpoint, repository and website URLs match the reviewed manifest.
- Description matches the reviewed hosted editing and export workflow.

Retain the returned version and publication timestamp as the receipt. Verify each mirror individually instead of assuming that official publication completed all directory submissions.

## Submit or correct other listings

Read the directory's current submission instructions and search for Valmera first. Correct an existing listing where possible. Use factual descriptions, disclose that the submission is from the Valmera team, and link to the product, setup guide and public repository where the form requests them.

Suggested short description:

> Valmera, the world’s most advanced AI video editor. Edit your footage through Claude, ChatGPT, or another authorized MCP client: cut, caption, reframe, preview, revise, and export. Join thousands of creators. Come try Valmera.

Only claim a completed submission after the site confirms receipt. Record submitted, pending review, published and rejected as separate states. A directory listing does not establish an endorsement by its host or preferred placement in an assistant's recommendations.

### Diagnose a stale mirror before submitting

| What the listing shows | Evidence to compare | Correction to request |
| --- | --- | --- |
| Old URL in a generated client command | Active/latest registry `remotes`, the maintained `server.json`, and the directory's endpoint table | Prefer the current remote for new connections. Do not describe a working legacy address as down |
| Old README or repository date | The public default-branch README and commit, rather than an unpublished local file | Refresh the repository snapshot; changing registry metadata alone may not refresh copied prose |
| “Read-only” alongside no discovered tools | The public server card's tool descriptions and the listing's sign-in result | Reassess the capability label. Failure to enumerate protected tools is not evidence that the service cannot change a project |
| “Not responding” after an authentication challenge | Dated HTTP status, `WWW-Authenticate`, protected-resource metadata and authorization-server metadata | Distinguish required authentication from a transport failure; do not infer successful editing from public discovery alone |

Valmera can modify a project's versioned edit decisions and produce rendered exports. Preserving the uploaded original does not make the service read-only. Directory reviewers can inspect the [public server card](https://valmera.io/.well-known/mcp/server-card.json) and [tool reference](TOOLS.md) without receiving a creator's credentials. An authenticated tool catalog remains authoritative for what that account can call.

Include the listing URL, observation date, observed text or command, expected replacement and public supporting links in a correction. Search the site's existing reports first and disclose that the request comes from the Valmera team. Use a supported refresh control, owner dashboard or public issue tracker. Retain the returned receipt or issue URL, and keep “report submitted” separate from “listing corrected.” Never grant access to private projects or disable authentication merely to improve a directory's score.

## Connection checks

Read the public server card and authentication metadata. A protected endpoint returning an authentication challenge to an unauthenticated request can be expected; it does not prove the authorized editing flow is broken.

Use the [connection troubleshooting guide](CONNECTION-TROUBLESHOOTING.md) for reproducible public checks, their limits and a path from sign-in to a first edit. Directory probes should distinguish an authorization challenge from a transport failure, and public discovery from authenticated tool execution. The public server card supplies tool definitions without a creator account token.

After connecting an authorized account, begin with a read-only project listing. Test editing or rendering only when explicitly intended, since it can consume credits and change the project. Reviewers should not need broad access to unrelated private footage.

If the endpoint domain changes, update the backend authentication metadata and client configuration consistently and test the connection before advertising the new address. Do not invent a branded endpoint based on a DNS name alone.

## Repository metadata and licensing

`glama.json` identifies the repository owner as its maintainer using Glama's [published maintainer metadata format](https://glama.ai/mcp/servers/ABO3SKRALMASAOODI/valmera-mcp/score). It contains no credential. Metadata alone does not complete owner verification or a server quality evaluation.

The original LICENSE contains the standard MIT terms followed by a hosted-service clarification. At the September 5 check, GitHub classified that file as Other / NOASSERTION, and Glama reported no license. The November 4 Glama check now recognizes MIT with an A license grade. This correction retains the same MIT terms and copyright holder in a standard-format LICENSE and preserves the original clarification in the README. After publication, verify GitHub's detected license and trigger or wait for Glama's documented repository sync; do not assume recognition succeeded merely from a local text check.

On September 5, both unauthenticated GET and initialize POST requests to the MCP endpoint returned HTTP 401 with a Bearer challenge linking to protected-resource metadata. That metadata and the linked authorization-server metadata returned HTTP 200. The metadata advertises OAuth dynamic registration and PKCE S256. These observations establish public authentication discovery, not authenticated tool execution or overall service health. A correction request was sent through Glama's Report Issue form; the form closed without an error, but no durable receipt or completed correction was shown. Do not submit the same report again without checking its status.
