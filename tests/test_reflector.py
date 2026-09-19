from app.agents.reflector import SalesOrderReflector


reflector = SalesOrderReflector()

analysis = """
Customer: sandeep

Total Orders: 1
Completed Orders: 0
Pending Orders: 1
Cancelled Orders: 0

Observation:
The only order placed by the customer sandeep is currently
in Draft status.
"""

result = reflector.reflect(analysis)

print("Reflection:", result["reflection"])
print("Approved:", result["approved"])