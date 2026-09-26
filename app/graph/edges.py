from debug.debug_graph import log_state


def should_continue(state):
    log_state(f"ROUTING DECISION: {state}", state)
    if state["approved"]:
        return "approved"

    if state["iteration"] >= 3:
        return "max_iterations"

    return "feedback"