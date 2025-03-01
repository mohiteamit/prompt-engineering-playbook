import openai
import os
from dotenv import load_dotenv

class OpenAIClient:
    def __init__(self):
        load_dotenv()
        api_key = os.getenv("OPENAI_API_KEY")
        self.client = openai.OpenAI(api_key=api_key)

    def get_client(self):
        return self.client
