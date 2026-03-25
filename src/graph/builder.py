from langgraph.graph import StateGraph, END

from src.state import ChatState
from src.nodes.intent import classify_intent
from src.nodes.extract import extract_order
from src.nodes.csv_retriever import fetch_order
from src.nodes.pdf_retriever import fetch_policy
from src.nodes.generator import generate_response
from src.nodes.memory import update_memory


def route_intent(state: ChatState):
    return "order_flow" if state["intent"] == "order" else "policy_flow"


def build_graph():
    builder = StateGraph(ChatState)

    builder.add_node("intent", classify_intent)
    builder.add_node("extract", extract_order)
    builder.add_node("csv", fetch_order)
    builder.add_node("pdf", fetch_policy)
    builder.add_node("generate", generate_response)
    builder.add_node("memory", update_memory)

    builder.set_entry_point("intent")

    builder.add_conditional_edges(
        "intent",
        route_intent,
        {
            "order_flow": "extract",
            "policy_flow": "pdf"
        }
    )

    builder.add_edge("extract", "csv")
    builder.add_edge("csv", "generate")

    builder.add_edge("pdf", "generate")

    builder.add_edge("generate", "memory")
    builder.add_edge("memory", END)

    return builder.compile()