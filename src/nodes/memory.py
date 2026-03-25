from src.state import ChatState

def update_memory(state: ChatState):
    history = state.get("chat_history", [])

    history.append({
        "user": state["query"],
        "bot": state["response"]
    })

    return {"chat_history": history}