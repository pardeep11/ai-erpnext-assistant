from app.agents.analyzer import SalesOrderAnalyzer
from app.agents.reflector import SalesOrderReflector
from app.agents.feedback import FeedbackAgent
from app.agents.lesson import LessonAgent
from app.graph.state import AgentState
from debug.debug_graph import log_state


analyzer = SalesOrderAnalyzer()
reflector = SalesOrderReflector()
feedback = FeedbackAgent()
lesson = LessonAgent()



def analyzer_node(state: AgentState):
    analyzer_result = analyzer.analyze(
        state["customer"],
        state["sales_orders"],
        state["order_counts"],
        state["feedback"],
        state["lesson"],
        state["previous_attempts"],
    )

    log_state("AFTER ANALYZER", state)

    return {
        **state,
        "analysis": analyzer_result,
        "iteration": state["iteration"] + 1,
    }

def reflector_node(state: AgentState):
    result =reflector.reflect(
        state["analysis"],
        state["sales_orders"],
        state["order_counts"]
)
    
    log_state("AFTER REFLECTOR", state)

    return {
        **state,
        "reflection": result["reflection"],
        "approved": result["approved"],
    }


def feedback_node(state: AgentState):
    feedback_result = feedback.generate_feedback(
        state["reflection"]
    )
    
    log_state(f"After FEEDBACK: {feedback_result}", state)

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
    
    log_state(f"After LESSON: {lesson_result}", state)
    
    return {
        **state,
        "lesson": lesson_result,
        "previous_attempts": previous_attempts,
    }