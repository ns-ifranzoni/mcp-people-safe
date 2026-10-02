"""Pharma Safe MCP.

Deployed on Prefect Horizon with entrypoint `server.py:mcp`.
"""

from fastmcp import FastMCP

mcp = FastMCP(
    name="Pharma Safe MCP",
    instructions="Provides a summary tool specially designed for pharma topics.",
)

SUMMARY_GUIDELINES = """\
Write a summary of the text below, specially designed for the pharmaceutical sector:
- Be accurate and faithful to the source. Do not add, infer or invent information.
- Keep exact figures, units, dosages, dates and product/active ingredient names.
- Highlight, when present: indication, dosage and administration, contraindications, \
warnings, adverse effects, interactions, storage and regulatory/compliance points.
- Use clear, neutral, professional language and keep it concise.
- If something important is missing or ambiguous in the source, say so explicitly.
"""


@mcp.tool(name="summary_for_pharma_topics", title="Summary for pharma topics")
def summary_for_pharma_topics(text: str) -> str:
    """Create a summary especially designed for pharma topics.

    Use this tool when a summary of pharmaceutical content is wanted (leaflets,
    labels, clinical or regulatory documents, reports...). The summary must be
    accurate and focused on what matters in the pharma sector: active ingredients,
    dosage, indications, contraindications, warnings, adverse effects and compliance.

    Args:
        text: The pharma text or topic to summarize.

    Returns the pharma summary guidelines together with the text, so the summary
    can be written following them.
    """
    return f"{SUMMARY_GUIDELINES}\nTEXT:\n{text}"


if __name__ == "__main__":
    mcp.run()
