from langchain_ollama import ChatOllama


class LessonAgent:
    def __init__(self):
        self.llm = ChatOllama(
            model="qwen2.5:3b",
            temperature=0,
        )

    def generate_lesson(self, reflection, feedback):
        prompt = f"""
You are a lesson agent.

Based on the reflection and feedback below, create one simple,
general lesson that can help improve future analyses.

Reflection:
{reflection}

Feedback:
{feedback}

Give only the lesson.
Do not invent information.
"""

        response = self.llm.invoke(prompt)

        return response.content