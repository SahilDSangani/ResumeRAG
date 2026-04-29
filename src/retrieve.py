# retrieve.py
# Handles natural language retrieval against the ChromaDB knowledge base.
# Embeds the user's query using text-embedding-3-large and returns the most
# semantically similar bullet points, optionally filtered by category or type.


def retrieve(query: str, category: str = None, top_k: int = 5) -> list[dict]:
    # Embeds the query string using the same model used during ingestion (text-embedding-3-large).
    # Queries the ChromaDB "experiences" collection for the top_k most similar bullets.
    # If category is provided (e.g. "project", "experience", "course"), filters results to that category.
    # Returns a list of result dicts, each containing the bullet text and its metadata
    # (title, company, dates, source_id, etc.) and similarity distance.
    pass
