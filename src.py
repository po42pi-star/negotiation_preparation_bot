import os
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENAI_API_BASE=os.getenv("https://openrouter.ai/api/v1")
ASSISTANT_ID = os.getenv("ASSISTANT_ID")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")