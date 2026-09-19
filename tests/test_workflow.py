from app.graph.workflow import workflow


initial_state = {
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


result = workflow.invoke(initial_state)


print("\n--- Final Result ---")

print("Customer:", result["customer"])
print("Iteration:", result["iteration"])

print("\nAnalysis:")
print(result["analysis"])

print("\nReflection:")
print(result["reflection"])

print("\nApproved:", result["approved"])