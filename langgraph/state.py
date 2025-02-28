from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages.human import HumanMessage
from dotenv import load_dotenv
from typing_extensions import TypeDict
import os
load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash", google_api_key=os.getenv("GOOGLE_API_KEY"))


class llm_with_tools_state(TypeDict):
    messages: list

def call_llm(state: llm_with_tools_state):
    messages = state["messages"]
    call_response = llm_with_tools.invoke(messages)

    return {"messages" : [call_response]}

print(call_llm({"messages": [HumanMessage(content=f"deposite 1000 usdt in tahirs account and its account no. is 12333")]}))