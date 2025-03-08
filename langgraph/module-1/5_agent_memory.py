from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import START, StateGraph, END, MessagesState
from langgraph.graph.state import CompiledStateGraph
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.memory import MemorySaver
from dotenv import load_dotenv
import os
load_dotenv()

memory:MemorySaver = MemorySaver()

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

llm_tools = llm.bind_tools(tools)
sys_msg = SystemMessage(content="you are helpfull asistant which perform airthematic operations")
def assistant(state:MessagesState)->MessagesState:
    return {"messages": [llm_tools.invoke([sys_msg]+state["messages"])]}

builder:StateGraph = StateGraph(MessagesState)

builder.add_node("assistant", assistant)
builder.add_node("tools", ToolNode(tools))
builder.add_edge(START,"assistant")
builder.add_conditional_edges(
    "assistant",
    tools_condition
)
builder.add_edge("tools","assistant")

state_graph:CompiledStateGraph = builder.compile(checkpointer=memory)

config1 = {"configurable":{"thread_id":"1"}}

messages = [HumanMessage(content="add 3 and 4")]

messages = state_graph.invoke({"messages":messages},config1)

for m in messages["messages"]:
    m.pretty_print()


messages = [HumanMessage(content="and multiply with 7")]

messages = state_graph.invoke({"messages":messages},config1)

for m in messages["messages"]:
    m.pretty_print()
