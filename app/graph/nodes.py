from app.agents.analyzer import SalesOrderAnalyzer
from app.agents.reflector import SalesOrderReflector
from app.agents.feedback import FeedbackAgent
from app.agents.lesson import LessonAgent
from app.graph.state import AgentState


analyzer = SalesOrderAnalyzer()
reflector = SalesOrderReflector()
feedback = FeedbackAgent()
lesson = LessonAgent()


def analyzer_node(state: AgentState):
    analysis = analyzer.analyze(
        customer=state["customer"],
        orders=state["sales_orders"],
        lesson=state["lesson"],
        previous_attempts=state["previous_attempts"],
    )

    return {
        **state,
        "analysis": analysis,
        "iteration": state["iteration"] + 1,
    }


def reflector_node(state: AgentState):
    result = reflector.reflect(
        state["analysis"]
    )

    return {
        **state,
        "reflection": result["reflection"],
        "approved": result["approved"],
    }


def feedback_node(state: AgentState):
    feedback_result = feedback.generate_feedback(
        state["reflection"]
    )

    return {
        **state,
        "feedback": feedback_result,
    }


def lesson_node(state: AgentState):
    lesson_result = lesson.generate_lesson(
        state["reflection"],
        state["feedback"],
    )

    previous_attempts = state["previous_attempts"]

    previous_attempts.append({
        "answer": state["analysis"],
        "critique": state["reflection"],
        "feedback": state["feedback"],
        "lesson": lesson_result,
    })

    return {
        **state,
        "lesson": lesson_result,
        "previous_attempts": previous_attempts,
    }