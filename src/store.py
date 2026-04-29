# store.py
# Handles embedding and storing approved bullet points in ChromaDB.
# Each bullet is embedded individually using text-embedding-3-large and stored
# as its own document, with the parent entry's metadata attached (title, company, dates, etc.).
# Called by ingest.py only after the user has approved the bullets.


def embed_texts(texts: list[str]) -> list[list[float]]:
    # Calls the OpenAI embeddings API with text-embedding-3-large.
    # Takes a list of strings and returns a list of embedding vectors (one per string).
    pass


def store_bullets(entry: dict, bullets: list[str]) -> None:
    # Takes an experience entry (for its metadata) and the approved list of bullet strings.
    # Embeds each bullet via embed_texts(), then upserts into the ChromaDB "experiences" collection.
    # IDs are formatted as <entry_id>_b0, <entry_id>_b1, etc. to allow re-ingestion safely.
    # Metadata stored per bullet: source_id, category, title, company, dates, location, type.
    pass
