# Google Gemini
from langchain.chat_models import init_chat_model
from langchain_tavily import TavilySearch
import os
from dotenv import load_dotenv
load_dotenv()


model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")

# Tavily Tool
web_search = TavilySearch(max_results=5)

tools = [web_search]
