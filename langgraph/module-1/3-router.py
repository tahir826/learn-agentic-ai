from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, START, END , MessagesState
from langgraph.graph.state import CompiledStateGraph
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.prebuilt import tools_condition, ToolNode
from dotenv import load_dotenv
import os

load_dotenv()

def multiply(a:int , b: int) -> int:
    """Multiply a and b.
    arg:
    a (int): first int
    b (int): second int
    returns: a * b
    """
    return a * b

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash", api_key=os.getenv("GOOGLE_API_KEY"))

llm_with_tools = llm.bind_tools([multiply])

def llm_calling_node(state:MessagesState)-> MessagesState:
    return {"messages":[llm_with_tools.invoke(state["messages"])]}

builder = StateGraph(MessagesState)
builder.add_node("llm_calling_node", llm_calling_node)
builder.add_node("tools", ToolNode([multiply]))
builder.add_edge(START, "llm_calling_node")
builder.add_conditional_edges(
    "llm_calling_node",
    tools_condition
)
builder.add_edge("tools",END)

graph:CompiledStateGraph = builder.compile()

messages = [HumanMessage(content="multiply 5 with 3")]
messages = graph.invoke({"messages":messages})
print(messages)