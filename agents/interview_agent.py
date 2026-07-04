from dotenv import load_dotenv
import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

load_dotenv()

# Initialize Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_KEY"),
    temperature=0.3
)


def interview_agent(state):
    """
    Interview Agent

    Input:
        state["parsed_jd"]
        state["selected_candidate"]

    Output:
        state["interview_questions"]
    """

    jd = state["parsed_jd"]
    candidate = state["selected_candidate"]

    prompt = f"""
You are an expert technical interviewer.

Generate interview questions for the candidate.

Rules:
- Questions must be based ONLY on:
  1. Job Description skills
  2. Candidate resume
- Do NOT ask random questions
- Split into:
  - Technical Questions (5)
  - Behavioral Questions (3)

Job Description:
Role: {jd.get("role")}
Skills: {jd.get("skills")}
Experience: {jd.get("experience")}

Candidate Resume:
{candidate.get("text")}

Output format:
Return structured JSON with:
technical: list of questions
behavioral: list of questions
"""

    response = llm.invoke([HumanMessage(content=prompt)])

    # simple cleanup (LLM returns JSON-like text)
    state["interview_questions"] = response.content

    return state