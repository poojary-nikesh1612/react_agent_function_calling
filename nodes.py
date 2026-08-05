from dotenv import load_dotenv
from langgraph.graph import MessagesState
from langgraph.prebuilt import ToolNode
from react import llm, tools

load_dotenv()

SYSTEM_PROMPT = """
You are an helpful assistent that can use tools to answer user query.
"""


def run_agent_reasoning(state: MessagesState) -> MessagesState:
    """Run the agent reasoning node"""
    response = llm.invoke(
        [{"role": "system", "content": SYSTEM_PROMPT}, *state["messages"]]
    )
    return {"messages": [response]}


tool_node = ToolNode(tools)
