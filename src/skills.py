# skills.py
# Processes the user's raw skills list from profile_raw.json.
# Skills are NOT stored in ChromaDB — they are handled entirely in this module.
# Pipeline: normalize → deduplicate → (optional) filter by JD relevance → group into categories.


def normalize_skills(raw_skills: list[str]) -> list[str]:
    # Cleans and standardizes skill names in the raw list.
    # Examples: "JS" → "JavaScript", "PCA" → "Principal Component Analysis", removes duplicates.
    # Returns a deduplicated list of normalized skill strings.
    pass


def group_skills(skills: list[str], job_description: str = None) -> list[dict]:
    # Takes a normalized skills list and optionally a job description string.
    # If no job description is provided: groups all skills into logical categories using GPT.
    # If a job description is provided: first filters out irrelevant skills, then groups the rest.
    # Example: a data science JD would exclude Java but include Python, Pandas, PyTorch.
    # Returns a list of dicts: [{"category": "Languages", "items": ["Python", "SQL"]}, ...]
    pass
