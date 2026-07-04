from dotenv import load_dotenv
import os
import json

load_dotenv()

# Tavily tool (web search)
from langchain_community.tools.tavily_search import TavilySearchResults


# Initialize Tavily
tavily_tool = TavilySearchResults(
    max_results=3,
    api_key=os.getenv("TAVILY_API_KEY")
)


def salary_agent(state):
    """
    Salary Agent (Tool Calling - Web Search)

    Input:
        state["parsed_jd"]

    Output:
        state["salary_data"]
    """

    jd = state["parsed_jd"]

    role = jd.get("role", "")
    location = jd.get("location", "India")

    query = f"""
    salary for {role} in {location} India 2026
    average salary, top companies, market range
    """

    try:
        # 🔍 Web search
        results = tavily_tool.run(query)

        # Extract useful summary (simple hackathon parsing)
        salary_data = {
            "role": role,
            "location": location,
            "raw_results": results,
            "source": "Tavily Web Search"
        }

    except Exception as e:
        # fallback (important for hackathon demo stability)
        salary_data = {
            "role": role,
            "location": location,
            "average_salary": "₹10–18 LPA (cached estimate)",
            "top_companies": ["Google", "Microsoft", "Amazon"],
            "source": "Fallback Cache",
            "error": str(e)
        }

    state["salary_data"] = salary_data

    return state