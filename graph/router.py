from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_KEY"),
    temperature=0
)


def router(state):
    """
    Classifies user intent
    """

    query = state["query"]

    prompt = f"""
Classify the intent into ONE of these:

- jd_upload
- resume_count
- screening
- interview
- salary
- rewrite_agent

User Query:
{query}

Return only the intent name.
"""

    result = llm.invoke([HumanMessage(content=prompt)])

    state["intent"] = result.content.strip()

    return state