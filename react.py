from dotenv import load_dotenv
from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearch

load_dotenv()


@tool
def triple(num: float) -> float:
    """Returns triple of the input number.
    param num: a number to triple
    returns: the triple of the input number.
    """
    return float(num) * 3


tools = [TavilySearch(max_results=1), triple]

llm = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite").bind_tools(tools)
