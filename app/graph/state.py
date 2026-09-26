from typing import TypedDict


class AgentState(TypedDict):
    customer: str
    sales_orders: dict
    order_counts: dict
    analysis: str
    reflection: str
    approved: bool
    iteration: int
    feedback: str
    lesson: str
    previous_attempts: list