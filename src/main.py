# import os
# from dotenv import load_dotenv
# from langgraph.graph import StateGraph, START, END
# from langgraph.graph.message import add_messages
# from langchain_core.messages import HumanMessage, AIMessage, BaseMessage, SystemMessage
# from langchain_openai import ChatOpenAI
# from typing import Annotated, Sequence, TypedDict



# load_dotenv()

# llm = ChatOpenAI(
#     base_url="https://freellmapi-seyc.onrender.com/v1",
#     api_key=os.environ.get("FREE_LLM_API"),
#     model="auto",
#     max_completion_tokens= 1000
# )
# class Agent(TypedDict):
#     messages: Annotated[Sequence[BaseMessage], add_messages]


# def agent(state: Agent) -> Agent:
#     response = llm.invoke(state["messages"])

#     return {"messages": response}

# graph = StateGraph(Agent)
# graph.add_node("agent",agent)
# graph.add_edge(START, "agent")
# graph.add_edge("agent", END)
# app = graph.compile()

# user_input = input("Enter: ")
# res = app.invoke({"messages": [("user", user_input)]})
# print(res)




from tools.gmail_tools import read_mail, send_mail
