from typing import TypedDict, Optional, List

class ChatState(TypedDict):
    query: str
    intent: Optional[str]
    order_id: Optional[int]
    context: Optional[str]
    response: Optional[str]
    chat_history: Optional[List]