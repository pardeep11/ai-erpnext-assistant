from app.graph.edges import should_continue


print("---- Retry Case ----")

state = {
    "approved": False,
    "iteration": 1,
}

print("Decision:", should_continue(state))


print("\n---- Maximum Iteration Case ----")

state = {
    "approved": False,
    "iteration": 3,
}

print("Decision:", should_continue(state))


print("\n---- Approved Case ----")

state = {
    "approved": True,
    "iteration": 1,
}

print("Decision:", should_continue(state))