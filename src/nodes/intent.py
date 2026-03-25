from src.state import ChatState

def classify_intent(state: ChatState):
    query = state["query"].lower()

    if "order" in query or "status" in query:
        return {"intent": "order"}
    return {"intent": "policy"}