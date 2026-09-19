from langgraph.graph import StateGraph, START, END

from app.graph.state import AgentState
from app.graph.nodes import analyzer_node, reflector_node
from app.graph.edges import should_continue


# Create the graph
graph = StateGraph(AgentState)


# Add nodes
graph.add_node("analyzer", analyzer_node)
graph.add_node("reflector", reflector_node)


# Normal edges
graph.add_edge(START, "analyzer")
graph.add_edge("analyzer", "reflector")


# Conditional edge
graph.add_conditional_edges(
    "reflector",
    should_continue,
    {
        "approved": END,
        "retry": "analyzer",
        "max_iterations": END,
    },
)


# Compile the graph
workflow = graph.compile()