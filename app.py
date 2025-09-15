from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, START, END
from langchain_core.messages import BaseMessage, HumanMessage,  AIMessage
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()
class AgentState(TypedDict):
    messages: Annotated[list[BaseMessage], lamba x, y: x + y]

def call_model(state: AgentState):
    print("---CALLING MODEL---")
    llm = ChatOpenAI(model="gpt-4o-mini")
    response = llm.invoke(state["messages"])
    return {"messages": [response]}
A
workflow = StateGraph(AgentState)
workflow.add_edge(START, "chatbot_node")
workflow.add_edge("chatbot_node", END)

app = workflow.compile()
initial_state = {"messages": [HumanMessage(content="What is langgraph?")]}
output = app.invoke(initial_state)

print("\nFinal Output:")
print(output["messages"][-1].content)