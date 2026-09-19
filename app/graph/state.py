from typing import TypedDict


class AgentState(TypedDict):
    customer: str
    sales_orders: list
    analysis: str
    reflection: str
    approved: bool
    iteration: int