from langchain_ollama import ChatOllama


class SalesOrderReflector:
    def __init__(self):
        self.llm = ChatOllama(
            model="qwen2.5:3b",
            temperature=0,
        )

    def reflect(
        self,
        analysis: str,
        sales_orders: dict,
        order_counts: dict,
    ):
        expected_pending = order_counts["pending"]
        print("EXPECTED:", f"**Pending Orders:** {expected_pending}")
        print("ANALYSIS:", repr(analysis))
        if f"**Pending Orders:** {expected_pending}" not in analysis:
            return {
                    "reflection": (
                    f"Pending Orders count is incorrect. "
                    f"Expected {expected_pending}."
        ),
        "approved": False,
    }
            
        prompt = f"""
You are a strict fact-checking reviewer for a sales order assistant.

ACTUAL SALES ORDER DATA:
{sales_orders}

ANALYSIS TO REVIEW:
{analysis}

Review only the factual statements about order statuses.

IMPORTANT RULES:

1. Compare statuses with the EXACT status in the actual data.

2. "To Deliver" and "To Deliver and Bill" are different statuses.

3. "To Deliver" is NOT Pending.

4. ONLY "To Deliver and Bill" is Pending.

5. Do not invent or change order information.

6. Do not check numerical counts.
   Python has already verified the numerical counts.

If the analysis correctly describes the actual statuses,
approve it.

Return ONLY:

APPROVED: True or False
REFLECTION: <short explanation>
"""

        response = self.llm.invoke(prompt)

        content = response.content.strip()

        approved = "APPROVED: True" in content

        reflection = content.replace(
            "APPROVED: True", ""
        ).replace(
            "APPROVED: False", ""
        ).replace(
            "REFLECTION:", ""
        ).strip()

        return {
            "reflection": reflection,
            "approved": approved,
        }