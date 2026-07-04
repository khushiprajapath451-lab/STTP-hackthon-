#  AI Recruitment Multi-Agent System

A LangGraph-powered AI recruitment system that automates:

- Job Description parsing
- Resume screening (RAG)
- Candidate ranking
- Interview question generation
- Salary estimation (web search)
- Human approval workflow

---

#  Features

##  Multi-Agent System
- JD Agent
- Resume Agent
- Screening Agent
- Interview Agent
- Salary Agent
- Approval Agent

##  RAG Pipeline
- Embeddings (Gemini)
- Vector DB (Chroma)
- Semantic resume matching

##  Tool Usage
- Tavily Web Search (salary data)
- Python tools (counting, parsing)

##  Human-in-loop
Recruiter approves final shortlist before output

---

#  Architecture

User → Router → LangGraph → Agents → Tools → Final Output

---

#  Tech Stack

- Python
- LangGraph
- LangChain
- Gemini API
- ChromaDB
- Tavily API
- Pydantic

---

#  Installation

```bash
git clone <repo>
cd AI-Recruitment-System
pip install -r requirements.txt