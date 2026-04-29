# main.py
# CLI entrypoint for ResumeRAG Part 1.
# Supports three subcommands:
#   ingest  — summarize and store experiences from profile_raw.json into ChromaDB
#   query   — retrieve relevant bullets from ChromaDB using a natural language query
#   skills  — normalize and group the skills basket, optionally filtered by a job description
#
# Usage:
#   python main.py ingest
#   python main.py ingest --id work_001
#   python main.py ingest --emphasis leadership
#   python main.py query "machine learning experience"
#   python main.py query "backend projects" --category project
#   python main.py skills
#   python main.py skills --jd data/sample_jd.txt


def run_ingest(args) -> None:
    # Handles the "ingest" subcommand.
    # If --id is provided, ingests only that single entry from profile_raw.json.
    # Otherwise calls ingest_all() to process every work, project, and course entry.
    # Passes --emphasis to control GPT summarization style (default: technical).
    pass


def run_query(args) -> None:
    # Handles the "query" subcommand.
    # Calls retrieve() with the query string and optional --category filter.
    # Prints each returned bullet with its metadata (title, company, dates) to the terminal.
    pass


def run_skills(args) -> None:
    # Handles the "skills" subcommand.
    # Loads the raw skills list from profile_raw.json.
    # If --jd is provided, reads that file and passes it to group_skills() for JD-filtered grouping.
    # Otherwise calls group_skills() with no JD to produce general category groupings.
    # Prints the grouped skills to the terminal.
    pass


if __name__ == "__main__":
    # Parse subcommand (ingest / query / skills) and dispatch to the appropriate run_* function.
    pass
