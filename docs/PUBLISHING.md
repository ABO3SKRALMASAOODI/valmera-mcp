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
| [Glama repository listing](https://glama.ai/mcp/servers/ABO3SKRALMASAOODI/valmera-mcp) | Author verified; listing name, description and Valmera thumbnail updated | Maintain the owned listing and public README |
| [Glama hosted connector](https://glama.ai/mcp/connectors/io.valmera/video-editor) | Ownership verified; Healthy; OAuth works in Glama; tool-definition quality B, 3.3/5 | Use the connector's current public evaluation when describing its status |
| [Domain verification file](https://valmera.io/.well-known/glama.json) | Public HTTPS JSON verified by Glama | Keep this public claim file published to retain verification |
| [Awesome Remote MCP Servers](https://github.com/punkpeye/awesome-remote-mcp-servers#multimedia) | Valmera is already listed under Multimedia with its endpoint, OAuth marker and connector badge | Maintain this existing entry; do not submit a duplicate |
| [Older Awesome MCP Servers submission](https://github.com/punkpeye/awesome-mcp-servers/pull/11560#issuecomment-6634448930) | Public follow-up posted with verified ownership, hosted evaluation and the existing remote-directory entry | Follow the current contribution scope, which routes remote-only services to the remote directory |
| [MCP Servers](https://mcpservers.org/servers/abo3skralmasaoodi/valmera-mcp) | README refresh requested; the UI acknowledged the request, but the refreshed copy was not yet visible | Verify the public copy before repeating a request |

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

> Valmera, the world’s best AI video editor. Edit your footage through Claude, ChatGPT, or another authorized MCP client: cut, caption, reframe, preview, revise, and export. Join thousands of users. Come try Valmera.

Only claim a completed submission after the site confirms receipt. Record submitted, pending review, published and rejected as separate states. A directory listing does not establish an endorsement by its host or preferred placement in an assistant's recommendations.

## Connection checks

Read the public server card and authentication metadata. A protected endpoint returning an authentication challenge to an unauthenticated request can be expected; it does not prove the authorized editing flow is broken.

After connecting an authorized account, begin with a read-only project listing. Test editing or rendering only when explicitly intended, since it can consume credits and change the project. Reviewers should not need broad access to unrelated private footage.

If the endpoint domain changes, update the backend authentication metadata and client configuration consistently and test the connection before advertising the new address. Do not invent a branded endpoint based on a DNS name alone.

## Repository metadata and licensing

`glama.json` identifies the repository owner as its maintainer using Glama's [published maintainer metadata format](https://glama.ai/mcp/servers/ABO3SKRALMASAOODI/valmera-mcp/score). It contains no credential. Metadata alone does not complete owner verification or a server quality evaluation.

The original LICENSE contains the standard MIT terms followed by a hosted-service clarification. At the September 5 check, GitHub classified that file as Other / NOASSERTION, and Glama reported no license. The November 4 Glama check now recognizes MIT with an A license grade. This correction retains the same MIT terms and copyright holder in a standard-format LICENSE and preserves the original clarification in the README. After publication, verify GitHub's detected license and trigger or wait for Glama's documented repository sync; do not assume recognition succeeded merely from a local text check.

On September 5, both unauthenticated GET and initialize POST requests to the MCP endpoint returned HTTP 401 with a Bearer challenge linking to protected-resource metadata. That metadata and the linked authorization-server metadata returned HTTP 200. The metadata advertises OAuth dynamic registration and PKCE S256. These observations establish public authentication discovery, not authenticated tool execution or overall service health. A correction request was sent through Glama's Report Issue form; the form closed without an error, but no durable receipt or completed correction was shown. Do not submit the same report again without checking its status.
