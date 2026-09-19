from langchain_ollama import ChatOllama


class SalesOrderReflector:
    def __init__(self):
        self.llm = ChatOllama(
            model="qwen2.5:3b",
            temperature=0,
        )

    def reflect(self, analysis: str):
        prompt = f"""
You are a reviewer for a sales order assistant.

Review the following analysis:

{analysis}

Your job is to determine whether the analysis is:
1. Correct
2. Clear
3. Consistent with the provided information

Do not create a new analysis.
Do not fetch any data.
Do not calculate business data.

Return your response in exactly this format:

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