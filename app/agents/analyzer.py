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

Analyze the CURRENT sales order data and provide a simple,
customer-friendly summary.

Customer:
{customer}

CURRENT ORDERS:
{orders}

Lesson from previous attempt:
{lesson}

Previous attempts:
{previous_attempts}

Your response must include:
- Total Orders
- Completed Orders
- Pending Orders
- Cancelled Orders
- A short observation

STATUS DEFINITIONS:
- Completed Orders: status is exactly "Completed"
- Pending Orders: status is exactly "To Deliver and Bill"
- Cancelled Orders: status is exactly "Cancelled"
- Draft Orders: status is exactly "Draft"

IMPORTANT FACTUAL ACCURACY RULES:

1. CURRENT ORDERS ARE THE ONLY SOURCE OF FACTUAL INFORMATION.
   Use only the order data provided under CURRENT ORDERS.

2. Do NOT invent, modify, remove, or assume any order information.

3. Do NOT change:
   - Order IDs
   - Customer names
   - Order statuses
   - Number of orders

4. Counts MUST be calculated from CURRENT ORDERS.
   - Total Orders = total number of provided orders.
   - Completed Orders = orders with status "Completed".
   - Pending Orders = orders with status "To Deliver and Bill".
   - Cancelled Orders = orders with status "Cancelled".
   - Draft Orders must NOT be counted as Pending Orders.

5. The status must be interpreted exactly as provided.
   Do not treat Draft orders as Pending.
   Do not treat any other status as Completed, Pending, or Cancelled.

6. The short observation MUST be consistent with CURRENT ORDERS.
   Do not make claims that are not directly supported by the current order data.

7. LESSON and PREVIOUS ATTEMPTS are NOT sources of factual information.
   They may only be used to improve the structure, clarity, or quality of the analysis.

8. NEVER use a previous attempt to replace, modify, or override CURRENT ORDERS.

9. If the current order data differs from a previous attempt,
   always use the CURRENT ORDERS data.

10. If information required for the analysis is missing,
    explicitly state that the information is missing.
    Do NOT guess or infer the missing information.

11. Do not say that all orders have the same status unless
    every order in CURRENT ORDERS actually has the same status.

12. Do not invent completed, pending, cancelled, or draft orders.

13. Before producing the final answer, verify that:
    - Total Orders matches the number of CURRENT ORDERS.
    - Completed count matches orders with status "Completed".
    - Pending count matches orders with status "To Deliver and Bill".
    - Cancelled count matches orders with status "Cancelled".
    - The observation matches the current order data.

14. Do not infer future actions, timelines, or outcomes from an order status.
    For example, "To Deliver and Bill" means the order is pending
    delivery and billing, but do not say it will be delivered soon,
    will be delivered on a particular date, or will definitely be completed
    unless that information is explicitly present in CURRENT ORDERS.

15. The Short Observation must account for ALL current orders correctly.
    Do not use vague statements such as "all other orders",
    "the remaining orders", or similar wording if it could create
    ambiguity or contradict the order counts.

16. The Short Observation must not imply that an order has a status
    different from its actual CURRENT ORDERS status.

17. If there are multiple different statuses, explicitly describe
    each relevant status and its count.

Use the lesson and previous attempts only to improve the current analysis.
CURRENT ORDERS always have higher priority than previous attempts or lessons.

Do not invent information.
"""

        response = self.llm.invoke(prompt)

        return response.content
