"""Check Valmera's public registry, authorization metadata, tool descriptions and example MP4."""
import hashlib
import json
import sys
from datetime import datetime, timezone
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ORIGIN = "https://valmera.io"
ENDPOINT = ORIGIN + "/mcp/server"
METADATA = ORIGIN + "/.well-known/oauth-protected-resource"
CARD = ORIGIN + "/.well-known/mcp/server-card.json"
REGISTRY = "https://registry.modelcontextprotocol.io/v0.1/servers/io.valmera%2Fvideo-editor/versions/latest"
EXAMPLE = ("https://raw.githubusercontent.com/ABO3SKRALMASAOODI/valmera-mcp/"
           "798e873006467bb0bab6f5332e83f9b99e69aba9/docs/evaluation/recorded-run-20261107/")


def get(url):
    request = Request(url, headers={"User-Agent": "Valmera-public-connector-check/1.0"})
    with urlopen(request, timeout=20) as response:
        return response.read()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def check():
    registry = json.loads(get(REGISTRY))
    server = registry["server"]
    official = registry["_meta"]["io.modelcontextprotocol.registry/official"]
    require(official["status"] == "active" and server["name"] == "io.valmera/video-editor",
            "Expected an active Valmera listing in the official registry.")
    remote = {"type": "streamable-http", "url": ENDPOINT}
    require(any(all(r.get(k) == v for k, v in remote.items()) for r in server["remotes"]),
            "The registry points to a different endpoint or transport.")
    try:
        get(ENDPOINT)
    except HTTPError as error:
        challenge = error.headers.get("WWW-Authenticate", "")
        require(error.code == 401 and 'resource_metadata="' + METADATA + '"' in challenge,
                "The anonymous response did not identify the expected authorization metadata.")
    else:
        raise ValueError("The endpoint no longer gives the expected anonymous challenge.")

    resource = json.loads(get(METADATA))
    require(resource["resource"] == ENDPOINT and "valmera.edit" in resource["scopes_supported"],
            "The resource URL or advertised edit scope changed.")
    card = json.loads(get(CARD))
    tools = {tool["name"]: tool for tool in card["tools"]}
    require(len(tools) == len(card["tools"]), "The card contains duplicate tool names.")
    examples = {}
    for name, expected_read_only in (("list_projects", True), ("cut_range", False),
                                     ("render_preview", False), ("export_final", False)):
        tool = tools[name]
        hint = tool.get("annotations", {}).get("readOnlyHint")
        require(hint is expected_read_only, f"Check the new annotation for {name}.")
        examples[name] = {"readOnlyHint": hint, "requiredInputs": tool["inputSchema"].get("required", [])}
    counts = {"true": 0, "false": 0, "unspecified": 0}
    for tool in tools.values():
        value = tool.get("annotations", {}).get("readOnlyHint")
        key = "true" if value is True else "false" if value is False else "unspecified"
        counts[key] += 1

    receipt = json.loads(get(EXAMPLE + "evidence.json"))
    digest = hashlib.sha256(get(EXAMPLE + "revised-final.mp4")).hexdigest()
    require(digest == receipt["export"]["sha256"], "The example MP4 differs from its pinned export receipt.")
    return {
        "checkedUtc": datetime.now(timezone.utc).isoformat(),
        "registry": {"record": REGISTRY, "version": server["version"], "remote": remote},
        "anonymousEndpointStatus": 401,
        "protectedResourceMetadata": METADATA,
        "scopesAdvertised": resource["scopes_supported"],
        "publicCard": CARD,
        "publishedToolCount": len(tools),
        "readOnlyHintCounts": counts,
        "declaredOperations": examples,
        "recordedDelivery": {"runDate": receipt["testedDate"], "receipt": EXAMPLE + "evidence.json",
                             "mp4": EXAMPLE + "revised-final.mp4", "sha256": digest},
        "authenticatedEditPerformedByThisCheck": False,
    }


if __name__ == "__main__":
    try:
        print(json.dumps(check(), indent=2, ensure_ascii=False))
    except (KeyError, ValueError, OSError, URLError) as error:
        sys.exit(f"Public connector check failed: {error}")
