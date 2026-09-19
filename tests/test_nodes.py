from app.graph.nodes import analyzer_node, reflector_node


state = {
    "customer": "sandeep",
    "sales_orders": [
        {
            "name": "SAL-ORD-2026-00001",
            "customer": "sandeep",
            "transaction_date": "2026-09-19",
            "status": "Draft",
        }
    ],
    "analysis": "",
    "reflection": "",
    "approved": False,
    "iteration": 0,
}


print("Initial state:")
print(state)

print("\n--- Analyzer Node ---")

state = analyzer_node(state)

print("Analysis:")
print(state["analysis"])
print("Iteration:", state["iteration"])

print("\n--- Reflector Node ---")

state = reflector_node(state)

print("Reflection:")
print(state["reflection"])
print("Approved:", state["approved"])