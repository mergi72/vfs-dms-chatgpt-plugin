import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_TOOLS = {
    "bridge_health",
    "list_connections",
    "list_items",
    "search_items",
    "open_share_url",
    "get_item_info",
    "read_document",
}


def load_json(relative_path: str) -> dict:
    return json.loads((ROOT / relative_path).read_text(encoding="utf-8"))


def test_manifest_and_folder_names_match() -> None:
    manifest = load_json(".codex-plugin/plugin.json")
    assert manifest["name"] == ROOT.name
    assert manifest["version"] == "0.1.0"
    assert manifest["mcpServers"] == "./.mcp.json"


def test_plugin_uses_http_mcp_service() -> None:
    server = load_json(".mcp.json")["mcpServers"]["vfs-dms"]
    assert server == {"type": "http", "url": "http://127.0.0.1:8781/mcp"}
    assert ".venv" not in json.dumps(server)


def test_required_tool_scope_matches_demi() -> None:
    settings = load_json("config/plugin.json")
    assert settings["plugin"]["mode"] == "read-only"
    assert set(settings["mcp"]["requiredTools"]) == EXPECTED_TOOLS


def test_skill_requires_explicit_document_read_request() -> None:
    skill = (ROOT / "skills" / "vfs-dms" / "SKILL.md").read_text(encoding="utf-8")
    assert "only when the user explicitly asks" in skill
    assert "Never contact Provider Bridge" in skill
