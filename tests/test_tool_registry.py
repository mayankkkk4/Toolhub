from tool_registry import (
    get_all_tools, get_all_categories, get_tool_by_id,
    get_tools_by_category, search_tools
)

def test_tool_registry_integrity():
    tools = get_all_tools()
    assert len(tools) >= 30, "Registry should contain at least 30 tools"

    for tool in tools:
        assert "id" in tool
        assert "name" in tool
        assert "category" in tool
        assert "description" in tool
        assert "client_side" in tool

def test_categories():
    categories = get_all_categories()
    assert len(categories) == 8
    cat_ids = [c["id"] for c in categories]
    assert "developer" in cat_ids
    assert "text" in cat_ids
    assert "calculator" in cat_ids
    assert "image" in cat_ids

def test_tool_lookup():
    json_tool = get_tool_by_id("json-formatter")
    assert json_tool is not None
    assert json_tool["name"] == "JSON Formatter & Minifier"

def test_search_tools():
    results = search_tools("json")
    assert len(results) > 0
    assert any(t["id"] == "json-formatter" for t in results)
