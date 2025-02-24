from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize the Gemini model
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=os.getenv("GOOGLE_API_KEY"))


# while True:
#     userInput = input("define query :- ")
#     result = llm.invoke(userInput)
#     print(result.content)
#     if userInput=="exit":
#         break

# Generate a response
# result = llm.invoke("hi")
# print(result.content)
