from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, START, END
from langchain_core.messages.human import HumanMessage
from dotenv import load_dotenv
from typing_extensions import TypedDict
import os
load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash", google_api_key=os.getenv("GOOGLE_API_KEY"))

class LastMessageState(TypedDict):
    messages: list

def call_llm(state: LastMessageState):
    messages = state["messages"]
    call_response = llm_with_tools.invoke(messages)

    return {"messages" : [call_response]}

def deposit_money(name:str , bank_account:str, amount:int) -> dict:
    """Deposit Money in Bank Account
    Args:
        name (str): Name of the person
        bank_account (str): Bank Account Number
        amount (int): Amount of money to be deposited
    Returns:
        dict: a dict
    """
    return {
        "status":f"Successfully Deposited {amount} in {bank_account} for {name}"
    }

llm_with_tools = llm.bind_tools([deposit_money])

# print(call_llm({"messages": [HumanMessage(content=f"deposite 1000 usdt in tahirs account and its account no. is 12333")]}))


builder : StateGraph = StateGraph(LastMessageState)

builder.add_node("call_llm_with_tools", call_llm)

builder.add_edge(START, "call_llm_with_tools")
builder.add_edge("call_llm_with_tools", END)

graph = builder.compile()

final=graph.invoke({"messages" : [HumanMessage(content="deposite 100 doller in tahirs account and account number is 3355544")]})
print(final)