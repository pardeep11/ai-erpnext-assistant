def should_continue(state):
    if state["approved"]:
        return "approved"

    if state["iteration"] >= 3:
        return "max_iterations"

    return "retry"