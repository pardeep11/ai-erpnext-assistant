from langchain_ollama import ChatOllama


class SalesOrderAnalyzer:
    def __init__(self):
        self.llm = ChatOllama(
            model="qwen2.5:3b",
            temperature=0,
        )

    def analyze(
        self,
        customer,
        orders,
        order_counts,
        feedback="",
        lesson="",
        previous_attempts=None,
    ):
        prompt = f"""
You are a sales order assistant.

Analyze the CURRENT sales order data and provide a simple,
customer-friendly summary.

Customer:
{customer}

CURRENT ORDERS:
{orders}

VERIFIED ORDER COUNTS:
{order_counts}

FEEDBACK FROM PREVIOUS REVIEW:
{feedback}

LESSON FROM PREVIOUS ATTEMPT:
{lesson}

PREVIOUS ATTEMPTS:
{previous_attempts}

Your response must include:
- Total Orders
- Completed Orders
- Pending Orders
- Cancelled Orders
- A short observation

IMPORTANT:

The VERIFIED ORDER COUNTS were calculated by Python
from the CURRENT ORDERS.

Do NOT recalculate or change these counts.

Use these values exactly:

- Total Orders = order_counts["total"]
- Completed Orders = order_counts["completed"]
- Pending Orders = order_counts["pending"]
- Cancelled Orders = order_counts["cancelled"]
- Draft Orders = order_counts["draft"]
- To Deliver Orders = order_counts["to_deliver"]

STATUS DEFINITIONS:

- Completed Orders: status is exactly "Completed"
- Pending Orders: status is exactly "To Deliver and Bill"
- Cancelled Orders: status is exactly "Cancelled"
- Draft Orders: status is exactly "Draft"
- To Deliver Orders: status is exactly "To Deliver"

IMPORTANT:

- "To Deliver" is NOT a Pending Order.
- "To Deliver" must remain exactly "To Deliver".
- Do not count "To Deliver" as Pending.
- Only "To Deliver and Bill" is Pending.

IMPORTANT FACTUAL ACCURACY RULES:

1. CURRENT ORDERS are the source of truth for individual
   order details and statuses.

2. VERIFIED ORDER COUNTS are the source of truth for
   the numerical counts.

3. Do not modify the verified counts.

4. Do not invent, remove, or change order information.

5. Do not change:
   - Order IDs
   - Customer names
   - Order statuses

6. Do not treat similar status names as equivalent.

7. FEEDBACK, LESSON, and PREVIOUS ATTEMPTS may help
   improve the response, but they must never override
   CURRENT ORDERS or VERIFIED ORDER COUNTS.

8. The short observation must be consistent with the
   actual order statuses.

9. Do not invent future actions, timelines, or outcomes.

10. If an order has status "To Deliver", report it as
    "To Deliver", not Pending.

Use the verified Python counts and current ERPNext
order data to produce the final response.

Do not invent information.
"""

        response = self.llm.invoke(prompt)

        return response.content