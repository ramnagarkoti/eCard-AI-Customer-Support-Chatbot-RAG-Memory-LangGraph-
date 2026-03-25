import streamlit as st
from src.graph.builder import build_graph

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(
    page_title="🛒 eCard AI Support",
    layout="centered"
)

st.title("🛒 eCard AI Customer Support")
st.markdown("Ask about your orders, refunds, or policies")

# ----------------------------
# Load Graph (cached)
# ----------------------------
@st.cache_resource
def load_graph():
    return build_graph()

graph = load_graph()

# ----------------------------
# Session State (Memory)
# ----------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "messages" not in st.session_state:
    st.session_state.messages = []

# ----------------------------
# Sidebar (extra feature 🔥)
# ----------------------------
with st.sidebar:
    st.title("⚙️ Settings")

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.session_state.chat_history = []

# ----------------------------
# Display Messages
# ----------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ----------------------------
# Input Box
# ----------------------------
user_input = st.chat_input("Ask something...")

if user_input:

    # Show user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    # Prepare state for graph
    state = {
        "query": user_input,
        "chat_history": st.session_state.chat_history
    }

    # Call LangGraph
    result = graph.invoke(state)

    bot_response = result["response"]

    # Show bot response
    with st.chat_message("assistant"):
        st.markdown(bot_response)

    # Save messages
    st.session_state.messages.append({
        "role": "assistant",
        "content": bot_response
    })

    # Update memory
    st.session_state.chat_history = result["chat_history"]