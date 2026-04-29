# ingest.py
# Orchestrates the full ingestion pipeline for one or all entries in profile_raw.json.
# For each entry: summarize → show bullets to user → human review loop → store approved bullets.
# This is the main script to run when adding or updating experiences in the knowledge base.


def load_profile(path: str) -> dict:
    # Reads and parses profile_raw.json from the given path.
    # Returns the full profile dict with keys: work_experience, projects, skills, coursework.
    pass


def review_loop(entry: dict, bullets: list[str]) -> list[str]:
    # Presents the generated bullets to the user in the terminal.
    # Prompts: [a]pprove / [e]dit / [r]egenerate / [s]kip
    # On approve: returns the bullets as-is.
    # On edit: opens a simple line-by-line edit flow, returns the edited bullets.
    # On regenerate: calls summarize_entry() again and re-presents the result.
    # On skip: returns an empty list (entry is not stored).
    pass


def ingest_entry(entry: dict, emphasis: str = "technical") -> None:
    # Runs the full pipeline for a single entry:
    # 1. Calls summarize_entry() to get bullet candidates.
    # 2. Passes them through review_loop() for human approval.
    # 3. If approved, calls store_bullets() to embed and persist them.
    pass


def ingest_all(profile_path: str, emphasis: str = "technical") -> None:
    # Loads profile_raw.json and calls ingest_entry() for every work, project, and course entry.
    # Skills are not ingested into ChromaDB — they are handled separately by skills.py.
    pass
