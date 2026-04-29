# summarize.py
# Converts a raw experience description into concise resume bullet points using GPT.
# Does NOT write anything to ChromaDB — only returns bullets for human review.
# Called by ingest.py before the user approves bullets for storage.


def summarize_entry(entry: dict, emphasis: str = "technical") -> list[str]:
    # Takes one experience entry (work, project, or course) and an emphasis style.
    # Sends the raw description to GPT and asks it to return 2-4 bullet points.
    # emphasis can be "technical", "leadership", or "impact" — changes the GPT prompt focus.
    # Returns a list of bullet strings. Does not store or embed anything.
    pass
