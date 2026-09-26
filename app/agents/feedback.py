from langchain_ollama import ChatOllama


class FeedbackAgent:
    def __init__(self):
        self.llm = ChatOllama(
            model="qwen2.5:3b",
            temperature=0,
        )

    def generate_feedback(self, reflection):
        prompt = f"""
You are a feedback agent.

The reflection below identifies a factual mistake in a sales order
analysis.

Your job is to convert the reflection into a clear correction
instruction for the next analysis.

Reflection:
{reflection}

STRICT RULES:

1. Do not change any facts from the reflection.

2. Do not invent any information.

3. ERPNext status names must be preserved exactly.

4. "To Deliver" and "To Deliver and Bill" are different statuses.

5. "To Deliver" is NOT a Pending Order.

6. ONLY "To Deliver and Bill" is considered Pending.

7. If the reflection says the actual status is "To Deliver",
   the feedback MUST say:
   - use the exact status "To Deliver"
   - do NOT classify it as Pending

8. Do not replace the actual status with a similar status.

9. Do not reinterpret the status.

10. Tell the next analyzer to use the actual ERPNext data
    as the source of truth.

Give only the correction instruction.
"""

        response = self.llm.invoke(prompt)

        return response.content.strip()