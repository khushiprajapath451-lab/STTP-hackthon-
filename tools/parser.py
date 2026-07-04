from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
import os
from dotenv import load_dotenv
from tools.parser import JDModel

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_KEY"),
    temperature=0
)

structured_llm = llm.with_structured_output(JDModel)


def parse_jd(text: str):
    """
    Convert JD → structured format
    """

    prompt = f"""
Extract structured job details:

{text}
"""

    result = structured_llm.invoke(
        [HumanMessage(content=prompt)]
    )

    return result.model_dump()