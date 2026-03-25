from src.graph.builder import build_graph

def run_chat():
    graph = build_graph()

    state = {
        "chat_history": []
    }

    while True:
        query = input("\nAsk: ")

        if query.lower() == "exit":
            break

        state["query"] = query

        result = graph.invoke(state)

        print("\nBot:", result["response"])

        state["chat_history"] = result["chat_history"]


if __name__ == "__main__":
    run_chat()