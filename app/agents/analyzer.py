from langchain_ollama import ChatOllama


class SalesOrderAnalyzer:
    def __init__(self):
        self.llm = ChatOllama(
            model="qwen2.5:3b",
            temperature=0,
        )

    def analyze(self, customer, orders):
        prompt = f"""
You are a sales order assistant.

Analyze the following sales order information and provide a
simple, customer-friendly summary.

Customer: {customer}

Orders:
{orders}

Include:
- Total Orders
- Completed Orders
- Pending Orders
- Cancelled Orders
- A short observation

Do not invent information.
"""

        response = self.llm.invoke(prompt)

        return response.content