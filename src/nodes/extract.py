import re
from src.state import ChatState

def extract_order(state: ChatState):
    match = re.search(r"\d+", state["query"])

    if match:
        return {"order_id": int(match.group())}

    return {"order_id": None}