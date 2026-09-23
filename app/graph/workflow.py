from langgraph.graph import StateGraph, START, END

from app.graph.state import AgentState
from app.graph.edges import should_continue
from app.graph.nodes import (
    analyzer_node,
    reflector_node,
    feedback_node,
    lesson_node,
)


# Create the graph
graph = StateGraph(AgentState)


# Add nodes
graph.add_node("analyzer", analyzer_node)
graph.add_node("reflector", reflector_node)
graph.add_node("feedback", feedback_node)
graph.add_node("lesson", lesson_node)


# Normal edges
graph.add_edge(START, "analyzer")
graph.add_edge("analyzer", "reflector")
graph.add_edge("feedback", "lesson")
graph.add_edge("lesson", "analyzer")


# Conditional edge
graph.add_conditional_edges(
    "reflector",
    should_continue,
    {
        "approved": END,
        "feedback": "feedback",
        "max_iterations": END,
    },
)


# Compile the graph
workflow = graph.compile()