# import os
# import json
# import uuid
# from dotenv import load_dotenv
# from langgraph.graph import StateGraph, START, END
# from langgraph.graph.message import add_messages
# from langgraph.types import Command
# from langchain_core.messages import BaseMessage, SystemMessage
# from langchain_openai import ChatOpenAI
# from typing import Annotated, Sequence, TypedDict

# from langchain_core.messages import ToolMessage # Passes data back to LLM after it calls a tool such as the content and the tool_call_id
# from langchain_core.tools import tool
# from langgraph.prebuilt import ToolNode

# from langgraph.checkpoint.memory import InMemorySaver
# from tools.gmail_tools import read_mail, send_mail
# from src.function_call import tool_executor
# from monitoring.spans import track_span, span_stack, spans, start_trace
 
# track_id = start_trace()

# load_dotenv()

# tools = [read_mail, send_mail]
# llm = ChatOpenAI(
#     base_url="https://freellmapi-seyc.onrender.com/v1",
#     api_key=os.environ.get("FREE_LLM_API"),
#     model="auto",
#     max_completion_tokens= 1000
# ).bind_tools(tools)

# class Agent(TypedDict):
#     messages: Annotated[Sequence[BaseMessage], add_messages]


# def agent(state: Agent) -> Agent:
#     with track_span("llm_call"):
#         response = llm.invoke(state["messages"])
#         print(state["messages"])
#         return {"messages": response}
    

# builder = StateGraph(Agent)
# builder.add_node("agent",agent)
# builder.add_node("tools", tool_executor)

# builder.add_edge(START, "agent")
# builder.add_conditional_edges(
#     "agent",
#     lambda state: "tools" if state["messages"][-1].tool_calls else END,
# )

# builder.add_edge("tools", "agent")

# checkpointer = InMemorySaver()
# graph = builder.compile(checkpointer=checkpointer)
# # -------------
# thread = {"configurable": {"thread_id": "user-123"}}

# user_input = input("Enter: ")
# for event in graph.stream({"messages": [("user", user_input)]}, thread):
#     print(event)

# state = graph.get_state(thread)
# if state.next:  # non-empty means the graph is paused
#     interrupt_data = state.tasks[0].interrupts[0].value
#     print("--- APPROVAL NEEDED ---")
#     print(interrupt_data["preview"])

#     answer = input("Proceed? [y/n]: ").strip().lower()
#     resume_payload = {"approved": answer == "y"}

#     for event in graph.stream(Command(resume=resume_payload), thread):
#         print(event)

# traces_file = "./monitoring/records/traces.json"
# if os.path.exists(traces_file):
#     with open(traces_file, "r") as file:
#         traces = json.load(file)
#         print(traces)

#     traces.append({"trace_id":track_id, "spans":spans})
#     with open(traces_file, 'w') as file:
#         json.dump(traces, file, indent=4)

import json
with open("./monitoring/records/traces.jsonl", 'r', encoding="utf-8") as file:
    print(file)
