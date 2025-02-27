from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages.human import HumanMessage
from dotenv import load_dotenv
import os
load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash", google_api_key=os.getenv("GOOGLE_API_KEY"))

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

call = llm_with_tools.invoke([HumanMessage(content=f"deposite 1000 usdt in tahirs account and its account no. is 12333")])

print(call)