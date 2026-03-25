import pandas as pd
from src.state import ChatState

df = pd.read_csv("data/orders.csv")

def fetch_order(state: ChatState):
    order_id = state.get("order_id")

    if order_id is None:
        return {"context": "No order ID found."}

    result = df[df["order_id"] == order_id]

    if result.empty:
        return {"context": "Order not found."}

    return {"context": str(result.to_dict(orient="records")[0])}