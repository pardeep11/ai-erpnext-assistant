from langchain_ollama import ChatOllama


class SalesOrderAnalyzer:
    def __init__(self):
        self.llm = ChatOllama(
            model="qwen2.5:3b",
            temperature=0,
        )

    def analyze(self, customer, orders, lesson="", previous_attempts=None):
        prompt = f"""
You are a sales order assistant.

Analyze the following sales order information and provide a
simple, customer-friendly summary.

Customer: {customer}

Orders:
{orders}

Lesson from previous attempt:
{lesson}

Previous attempts:
{previous_attempts}

Include:
- Total Orders
- Completed Orders
- Pending Orders
- Cancelled Orders
- A short observation

Use the lesson and previous attempts to improve the current analysis.

IMPORTANT RULES:
- Use only the information provided in Orders.
- Do not invent or change any order information.
- Do not change Order IDs.
- Do not change customer names.
- Do not change order statuses.
- Do not invent completed, pending, or cancelled orders.
- The order counts must match the provided Orders data.
- Previous attempts and lessons are only for improving the analysis.
  They are not a source of factual information.
- Do not use previous attempts to replace or modify the current Orders data.
- Draft orders are NOT pending delivery and billing.
- "To Deliver and Bill" orders are pending delivery and billing.
- Do not say all orders have the same status when they have different statuses.
- The Short Observation must match the order data exactly.

Do not invent information.
"""

        response = self.llm.invoke(prompt)

        return response.content