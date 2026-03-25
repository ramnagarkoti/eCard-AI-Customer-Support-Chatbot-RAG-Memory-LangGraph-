from src.state import ChatState
from src.utils.vectorstore import get_vectorstore

vectorstore = get_vectorstore()

def fetch_policy(state: ChatState):
    docs = vectorstore.similarity_search(state["query"], k=2)

    context = " ".join([doc.page_content for doc in docs])

    return {"context": context}