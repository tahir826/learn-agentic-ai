from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, START, END, MessagesState
from langgraph.graph.state import CompiledStateGraph
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
load_dotenv()
import os

def multiply(a:int , b:int)->int:
    """Multipy a into b
    arg:
        a: int
        b: int
        return a * b
    """
    return a*b

def addition(a:int , b:int)->int:
    """addition of a and b
    arg:
        a: int
        b: int
        return a + b
    """
    return a+b

def subtraction(a:int , b:int)->int:
    """subtraction of a into b
    arg:
        a: int
        b: int
        return a-b
    """
    return a-b

def divide(a:int , b:int)->int:
    """dvide a into b
    arg:
        a: int
        b: int
        return a-b
    """
    return a/b

tools:list = [addition, multiply, divide, subtraction]

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", api_key=os.getenv("GOOGLE_API_KEY"))

llm_with_tools = llm.bind_tools(tools)
sys_msg = SystemMessage(content="You are help full assistant which do some airthmetic operations")
def tool_calling_llm(state:MessagesState)->MessagesState:
    return {"messages":[llm_with_tools.invoke([sys_msg]+state["messages"])]}

builder:StateGraph = StateGraph(MessagesState)

builder.add_node("llm",tool_calling_llm)
builder.add_node("tools", ToolNode(tools))
builder.add_edge(START, "llm")
builder.add_conditional_edges(
    "llm",
    tools_condition
)
builder.add_edge("tools", "llm")

graph:CompiledStateGraph = builder.compile()



messages = [HumanMessage(content="first add 2 and 8 and then multipy with 6 and then divide with 4 and then subtract with 2")]

messages = graph.invoke({"messages":messages})

for m in messages['messages']:
    m.pretty_print()