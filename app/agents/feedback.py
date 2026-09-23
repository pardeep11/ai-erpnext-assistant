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

Based on the reflection below, provide a clear and actionable
instruction for improving the next analysis.

Reflection:
{reflection}

Give only the improvement instruction.
Do not invent information.
"""

        response = self.llm.invoke(prompt)

        return response.content