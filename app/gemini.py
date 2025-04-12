import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=os.getenv("GEMINI_API_KEY"))


async def generate_summary(text: str) -> str:
    try:
        prompt = f"Summarize the following blog post in a concise paragraph:\n\n{text}"
        response = llm.invoke(prompt)
        return response.content.strip()
    except Exception as e:
        print(f"An error occurred while generating the summary: {e}")
        return "An error occurred while generating the summary."
