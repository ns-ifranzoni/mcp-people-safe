"""Pharma Safe MCP.

Deployed on Prefect Horizon with entrypoint `server.py:mcp`.
"""

from fastmcp import FastMCP

mcp = FastMCP(
    name="Pharma Safe MCP",
    instructions="Provides a summary tool specially designed for pharma topics.",
)

SUMMARY_GUIDELINES = """\
Write a summary of the text below, specially designed for the Human Resources sector:
- Be accurate and faithful to the source. Do not add, infer or invent information.
- Keep exact figures, amounts, percentages, dates, deadlines, job titles and names of \
policies, agreements or regulations.
- Highlight, when present: purpose and scope, affected employees or roles, rights and \
obligations, compensation and benefits, working hours and leave, deadlines and \
procedures, sanctions or consequences, and legal/compliance points (labour law, \
collective agreements, data protection).
- Treat personal data with care: do not reproduce sensitive personal details \
(health, salary of named individuals, disciplinary records) beyond what is necessary.
- Use clear, neutral, professional and inclusive language and keep it concise.
- If something important is missing or ambiguous in the source, say so explicitly.
"""


@mcp.tool(name="summary_for_pharma_topics", title="Summary for pharma topics")
def summary_for_pharma_topics(text: str) -> str:
    """Create a summary especially designed for human resources topics.

    Use this tool when a summary of human resources content is wanted (policies,
    contracts, collective agreements, internal communications, regulatory
    documents, reports...). The summary must be accurate and focused on what
    matters in the HR sector: affected employees, rights and obligations,
    compensation and benefits, deadlines, personal data and compliance.

    Args:
        text: The human resources text or topic to summarize.

    Returns the human resources summary guidelines together with the text, so the
    summary can be written following them.
    """
    return f"{SUMMARY_GUIDELINES}\nTEXT:\n{text}"


if __name__ == "__main__":
    mcp.run()
