from app.agents.analyzer import SalesOrderAnalyzer


analyzer = SalesOrderAnalyzer()

orders = [
    {
        "name": "SAL-ORD-2026-00001",
        "customer": "sandeep",
        "transaction_date": "2026-09-19",
        "status": "Draft",
    }
]

result = analyzer.analyze(
    customer="sandeep",
    orders=orders,
)

print(result)