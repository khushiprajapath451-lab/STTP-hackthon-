from dotenv import load_dotenv
import os

from langchain_community.tools.tavily_search import TavilySearchResults

load_dotenv()

tavily = TavilySearchResults(
    api_key=os.getenv("TAVILY_API_KEY"),
    max_results=3
)


def search_web(query: str):
    """
    Web search tool for salary / trends
    """

    results = tavily.run(query)

    return results