"""Verify the published Valmera demo export and current public API declaration."""

import hashlib
import json
import re
from urllib.request import urlopen

ORIGIN = "https://valmera.io"
CARD = "/.well-known/mcp/server-card.json"
EXAMPLE = "/examples/product-demo"
MEDIA = EXAMPLE + "/valmera-product-demo.mp4"
TOOLS = {
    "cut_range": {"project_id", "start", "end"},
    "add_captions": {"project_id"},
    "render_preview": {"project_id"},
    "export_final": {"project_id", "edl_version"},
    "wait_for_job": {"job_id"},
    "download_url": {"project_id"},
}


def read_json(path):
    with urlopen(ORIGIN + path, timeout=15) as response:
        return json.load(response)


def check_public_contract(card):
    tools = {tool["name"]: tool for tool in card["tools"]}
    for name, required in TOOLS.items():
        tool = tools.get(name, {})
        declared = set(tool.get("inputSchema", {}).get("required", []))
        if not required <= declared:
            raise ValueError(f"{name} changed or is missing from the public declaration")
    if tools["export_final"]["annotations"].get("idempotentHint") is not True:
        raise ValueError("The public export declaration no longer marks retries as idempotent")


def find_receipt(evidence):
    export, = [call for call in evidence["calls"] if call["tool"] == "export_final"]
    download, = [
        call for call in evidence["calls"]
        if call["tool"] == "download_url" and call["args"].get("kind") == "final"
    ]
    version = export["args"]["edl_version"]
    if download["args"]["edl_version"] != version:
        raise ValueError("Export and download point to different edit versions")
    digest = re.fullmatch(r"sha256 ([0-9a-f]{64})", download["result"])
    if digest is None:
        raise ValueError("Missing SHA-256 in the published receipt")
    return version, digest[1], evidence["file"]["bytes"]


def verify_file(stream, expected_digest, expected_bytes):
    digest = hashlib.sha256()
    byte_count = 0
    for chunk in iter(lambda: stream.read(64 * 1024), b""):
        digest.update(chunk)
        byte_count += len(chunk)
    if byte_count != expected_bytes or digest.hexdigest() != expected_digest:
        raise ValueError("Downloaded file does not match the published receipt")
    return byte_count


def main():
    check_public_contract(read_json(CARD))
    version, digest, expected_bytes = find_receipt(read_json(EXAMPLE + "/evidence.json"))
    with urlopen(ORIGIN + MEDIA, timeout=25) as response:
        if response.headers.get_content_type() != "video/mp4":
            raise ValueError("The public example URL did not return an MP4")
        byte_count = verify_file(response, digest, expected_bytes)
    print(f"Public example verified: edit version {version}, {byte_count:,} bytes")
    print(f"SHA-256: {digest}")
    print("Current public API declaration matches the checked tool requirements.")


if __name__ == "__main__":
    main()
