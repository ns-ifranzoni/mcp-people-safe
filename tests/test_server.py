import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from fastmcp import Client  # noqa: E402

from server import mcp  # noqa: E402


def run(coro):
    return asyncio.run(coro)


def test_only_one_tool():
    async def go():
        async with Client(mcp) as client:
            return await client.list_tools()

    tools = run(go())
    assert [t.name for t in tools] == ["summary_for_pharma_topics"]
    assert "summary especially designed for pharma" in tools[0].description


def test_tool_returns_guidelines_and_text():
    async def go():
        async with Client(mcp) as client:
            return (await client.call_tool("summary_for_pharma_topics", {"text": "Take one tablet daily"})).data

    out = run(go())
    assert "pharmaceutical sector" in out
    assert out.endswith("Take one tablet daily")
