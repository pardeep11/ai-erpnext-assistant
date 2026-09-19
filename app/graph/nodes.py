from app.agents.analyzer import SalesOrderAnalyzer
from app.agents.reflector import SalesOrderReflector
from app.graph.state import AgentState


analyzer = SalesOrderAnalyzer()
reflector = SalesOrderReflector()


def analyzer_node(state: AgentState):
    analysis = analyzer.analyze(
        customer=state["customer"],
        orders=state["sales_orders"],
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