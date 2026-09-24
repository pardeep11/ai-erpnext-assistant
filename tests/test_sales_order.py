from app.erpnext.sales_order import SalesOrderService


service = SalesOrderService()

result = service.get_sales_orders('sandeep',limit=5)

print(result)