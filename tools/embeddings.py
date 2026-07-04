from dotenv import load_dotenv
import os
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_KEY"))


def get_embedding(text: str):
    """
    Convert text → embedding vector
    """

    response = client.models.embed_content(
        model="models/gemini-embedding-001",
        contents=[text]
    )

    return response.embeddings[0].values