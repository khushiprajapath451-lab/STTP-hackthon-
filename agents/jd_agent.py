from dotenv import load_dotenv
import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from models.jd_schema import JD

load_dotenv()

# Initialize Gemini
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_KEY"),
    temperature=0
)

# Structured Output
structured_llm = llm.with_structured_output(JD)


def jd_agent(state):
    """
    Input:
        state["jd_text"]

    Output:
        state["parsed_jd"]
    """

    jd_text = state.get("jd_text", "").strip()

    if not jd_text:
        state["parsed_jd"] = {
            "role": "",
            "skills": [],
            "experience": "",
            "location": "",
            "education": ""
        }
        return state

    prompt = f"""
You are an HR assistant.

Extract structured fields from this Job Description.

Return ONLY structured JSON.

Fields:
- role
- skills
- experience
- location
- education

Job Description:
{jd_text}
"""

    try:
        parsed_jd = structured_llm.invoke(
            [HumanMessage(content=prompt)]
        )

        state["parsed_jd"] = parsed_jd.model_dump()

    except Exception as e:
        state["parsed_jd"] = {
            "role": "",
            "skills": [],
            "experience": "",
            "location": "",
            "education": "",
            "error": str(e)
        }

    return state