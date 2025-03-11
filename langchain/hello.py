from langchain_openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()

llm1 = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"))

response = llm1.invoke("hi")
print(response)