# ResumeRAG — Part 1 Implementation Plan

**Focus:** Grounded experience retrieval system — ingestion, summarization, storage, and retrieval. No resume generation (that's Part 2).

---

## What Part 1 Builds

A searchable professional knowledge base built from a user's real history.

Given natural language input about work experience, projects, skills, and coursework:
1. Summarize into clean bullet points via GPT
2. Human reviews and approves bullets before storage
3. Embed approved bullets with `text-embedding-3-large` and store in ChromaDB
4. Allow natural language retrieval queries against the stored history
5. Process the skills basket: deduplicate, normalize, group by category for a given JD

---

## File Structure

```
FinalProject398/
├── data/
│   └── profile_raw.json      # user's raw input (descriptions, skills, courses)
├── src/
│   ├── config.py             # loads .env, exports constants
│   ├── summarize.py          # GPT summarization: raw description → bullet points
│   ├── store.py              # embed bullets (text-embedding-3-large) + upsert to ChromaDB
│   ├── ingest.py             # orchestrates: summarize → human review loop → store
│   ├── retrieve.py           # natural language queries against ChromaDB
│   └── skills.py             # deduplicate, normalize, group skills for a JD
├── main.py                   # CLI: ingest or query
├── requirements.txt
├── .env
├── .env.example
└── .gitignore
```

---

## Input Schema (`data/profile_raw.json`)

```json
{
  "work_experience": [
    {
      "id": "work_001",
      "title": "Data Science Intern",
      "company": "Acme Corp",
      "location": "Chicago, IL",
      "type": "Internship",
      "start": "May 2024",
      "end": "Aug 2024",
      "current": false,
      "description": "I worked at a startup where I used AI tools to gather research papers..."
    }
  ],
  "projects": [
    {
      "id": "proj_001",
      "name": "RAG Resume Tailor",
      "start": "Jan 2026",
      "end": null,
      "current": true,
      "stack": ["Python", "ChromaDB", "OpenAI"],
      "description": "Built a pipeline that semantically matches user experiences to job descriptions..."
    }
  ],
  "skills": ["Python", "SQL", "R", "Pandas", "PyTorch", "Git", "Docker", "LangChain", "Java"],
  "coursework": [
    {"id": "course_001", "name": "Machine Learning", "description": "Supervised and unsupervised learning, neural nets, model evaluation"},
    {"id": "course_002", "name": "Database Systems", "description": "Relational databases, SQL, indexing, transactions"}
  ]
}
```

---

## Pipeline

```
profile_raw.json
      │
      ▼
  summarize.py  ◄──► GPT-4o
      │
  (returns 2-4 bullet points per entry)
      │
      ▼
  Human review loop (CLI: approve / edit / regenerate)
      │
      ▼
   store.py  ◄──► text-embedding-3-large
      │
   ChromaDB (persistent local)
      │
      ▼
  retrieve.py  ◄──► natural language query
      │
      ▼
  ranked results (semantic similarity + metadata filter)
```

---

## Module Responsibilities

### `src/summarize.py`
- Input: one experience entry dict
- Calls GPT-4o to produce 2–4 bullet points
- Supports emphasis flags: `technical`, `leadership`, `impact` (same query, different system prompt)
- Returns list of bullet strings — does NOT write to ChromaDB

### `src/store.py`
- Input: approved bullets list + entry metadata
- Calls `text-embedding-3-large` to embed each bullet individually
- Upserts into ChromaDB collection `"experiences"`
- Metadata stored per bullet: `category`, `title`, `company`, `dates`, `location`, `type`, `source_id`

### `src/ingest.py`
- Orchestrates the full flow for one entry at a time:
  1. Call `summarize.py`
  2. Print bullets to terminal, ask user: `[a]pprove / [e]dit / [r]egenerate / [s]kip`
  3. On approve → call `store.py`
- Loops through all entries in `profile_raw.json`

### `src/retrieve.py`
- Accepts a free-text query string
- Embeds query with `text-embedding-3-large`
- Queries ChromaDB with optional `where` filter on `category` or `type`
- Returns top-N results with metadata
- Example queries: `"What experience shows leadership?"`, `"Which projects match data analyst roles?"`

### `src/skills.py`
- Input: raw skills list from `profile_raw.json` + optional job description string
- Step 1: Normalize (e.g. `JS → JavaScript`, `PCA → Principal Component Analysis`)
- Step 2: Deduplicate
- Step 3 (if JD provided): Call GPT to filter relevant skills and group into recruiter-friendly categories
- Returns list of `{category: str, items: [str]}` dicts

---

## ChromaDB Design

- **Local** `PersistentClient`
- **One collection**: `"experiences"` covering work, projects, coursework
- **Embedding model**: `text-embedding-3-large` via OpenAI (override ChromaDB default)
- Bullets stored individually — each bullet is its own document
- Skills are NOT stored in ChromaDB; they are processed on-demand by `skills.py`

---

## `main.py` CLI

```
python main.py ingest                          # run full ingestion loop
python main.py ingest --id work_001            # ingest one entry by id
python main.py query "leadership experience"   # retrieval query
python main.py query "data analyst" --category project
python main.py skills                          # print grouped skills (no JD)
python main.py skills --jd data/sample_jd.txt # filter + group skills for JD
```

---

## Dependencies

```
chromadb>=0.5
openai>=1.0
python-dotenv>=1.0
```

No Jinja2, no LaTeX — those are Part 2.

---

## Environment Variables

```
OPENAI_API_KEY=sk-...
LLM_MODEL=gpt-4o
EMBED_MODEL=text-embedding-3-large
CHROMA_DB_PATH=./chroma_db
PROFILE_PATH=./data/profile_raw.json
```

---

## Implementation Checklist

- [ ] Fill `data/profile_raw.json` with real experiences
- [ ] `src/config.py` — load env vars
- [ ] `src/summarize.py` — GPT summarization with emphasis flags
- [ ] `src/store.py` — embed + upsert to ChromaDB
- [ ] `src/ingest.py` — human review loop (approve / edit / regenerate / skip)
- [ ] `src/retrieve.py` — natural language query interface
- [ ] `src/skills.py` — normalize, deduplicate, group with optional JD filter
- [ ] `main.py` — wire all subcommands
- [ ] End-to-end test: ingest 2–3 entries, run retrieval queries, check returned bullets

---

## Verification

```bash
# Ingest all entries with human review
python main.py ingest

# Query the knowledge base
python main.py query "machine learning experience"
python main.py query "what projects involve backend development"

# Skills grouping (no JD)
python main.py skills

# Skills filtered for a specific role
python main.py skills --jd data/sample_jd.txt
```

---

## Out of Scope for Part 1

- LaTeX resume templates
- PDF generation
- ATS optimization
- FastAPI backend (planned for later)
- Tailored resume assembly (Part 2)
