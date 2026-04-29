# ResumeRAG — Part 1: Grounded Experience Retrieval System

## Overview

ResumeRAG is a Retrieval-Augmented Generation (RAG) system that converts a user’s real work history, projects, skills, and coursework into a searchable professional knowledge base.

Instead of generating fake resume content, ResumeRAG stores verified user experiences and retrieves the most relevant information for future resume tailoring, job matching, and career queries.

This repository contains **Part 1** of the project: ingestion, summarization, embedding, storage, and retrieval.

---

# Problem

Students and job seekers often need to rewrite resumes for every application while trying to remember:

* what they accomplished in each role
* which projects fit a target job
* what skills are most relevant
* which coursework should be highlighted

Most AI resume tools focus on generation and may exaggerate or fabricate experience.

ResumeRAG focuses on **truthful retrieval first**.

---

# Core Idea

Users describe their experiences in natural language.

Example:

## Work Experience Input

* **Position Title***
* Company
* Location
* Experience Type (Internship / Full-Time / Part-Time / Freelance)
* Start Month / Year
* End Month / Year
* Currently Work Here (boolean)
* **Description***

Example Description:

> I worked at a startup where I used AI tools to gather research papers, testimonials, white papers, and news related to agricultural chemical products. I performed sentiment analysis on each source and built an interactive website so farmers could make informed purchasing decisions.

---

# Processing Pipeline

## 1. LLM Summarization

Uses GPT models (initially GPT-4o family) to convert long descriptions into concise resume-ready bullet points.

Example Output:

* Researched industry papers, testimonials, and news related to agricultural chemical products
* Performed sentiment analysis on external sources to evaluate product perception
* Built an interactive web platform to help farmers compare products and make informed decisions

### Design Goals

* Preserve meaning
* Remove redundancy
* Avoid overlapping bullets
* Improve clarity

Users manually review summaries before saving.

Users may also request emphasis changes such as:

* focus on technical work
* focus on leadership
* focus on business impact

---

## 2. Embedding + Storage

Approved bullet points are embedded using **text-embedding-3-large** and stored in **ChromaDB**.

Each entry stores metadata such as:

* category (experience / project / course)
* title
* company
* dates
* location
* experience type
* source id

---

## 3. Retrieval

Users can search their stored history in natural language.

Example Queries:

* Tell me about Work Experience 1
* What is my most relevant teaching experience?
* Which projects match data analyst roles?
* What experience shows leadership?
* Which work history is strongest for AI jobs?

Initial ranking strategy:

* semantic similarity
* metadata filtering
* recency weighting (planned)
* hybrid reranking (future)

---

# Skills Basket

Users maintain one master list of skills.

Example Raw Skills:

Python, SQL, R, Tableau, Pandas, NumPy, PyTorch, Docker, Git, LangChain, Communication

The system:

1. Deduplicates skills
2. Normalizes naming (JS → JavaScript, PCA → Principal Component Analysis)
3. Matches skills to job descriptions
4. Groups them into recruiter-friendly categories

Example Output:

### Programming Languages

Python, SQL, R, JavaScript

### Data & Analytics

Pandas, NumPy, Tableau, Excel

### ML & Statistics

PyTorch, Scikit-learn, Regression, PCA

### GenAI Tools

LangChain, LLM Workflows, RAG

### Tools & Collaboration

Git, Docker, Communication, Teamwork

---

# Coursework Matching

Users input completed courses with optional descriptions.

Example:

* Machine Learning
* Database Systems
* Statistical Modeling
* Linear Algebra

When given a job description, ResumeRAG ranks the most relevant courses to display.

---

# Tech Stack

## Backend

* Python
* FastAPI (planned)

## Models

* GPT-4o / OpenAI models
* text-embedding-3-large

## Database

* ChromaDB

## Future Local Privacy Mode

* llama.cpp
* all-MiniLM embeddings

---

# Why This Matters

Most resume tools generate text.

ResumeRAG builds a **truthful memory layer** first.

That means future resume generation can be:

* personalized
* faster
* more accurate
* less repetitive
* resistant to hallucination

---

# MVP Scope

## Included in Part 1

* Experience ingestion
* GPT summarization
* Human verification loop
* Vector storage
* Natural language retrieval
* Skill grouping
* Course relevance matching

## Future (Part 2)

* Tailored resume generation
* ATS optimization
* LaTeX resume templates
* PDF export

---

# Example End Goal

Input:

> Tailor my resume for a Data Analyst internship.

Part 1 supplies:

* best matching experiences
* relevant projects
* strongest skills
* top coursework

Part 2 will convert this into a polished resume.