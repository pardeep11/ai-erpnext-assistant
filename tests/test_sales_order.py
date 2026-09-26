from app.erpnext.sales_order import SalesOrderService


service = SalesOrderService()

result = service.get_sales_orders('sandeep',limit=10)
count_orders = service.get_order_counts(result)


print(result)
print(count_orders)