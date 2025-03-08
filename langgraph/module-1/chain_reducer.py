from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages, MessagesState
from typing import Annotated
from typing_extensions import TypedDict
from langchain_core.messages import AnyMessage

# Load OpenAI API key from environment variable
from dotenv import load_dotenv
load_dotenv()
import os
openai_api_key = os.getenv("OPENAI_API_KEY")

create_llm = ChatOpenAI(model="gpt-4o", api_key=openai_api_key)

class MessageState(TypedDict):
    messages = Annotated[list[AnyMessage], add_messages]