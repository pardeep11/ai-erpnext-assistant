from app.erpnext.client import ERPNextClient


class SalesOrderService:
    def __init__(self):
        self.client = ERPNextClient()

    def get_sales_orders(self, limit=10):
        return self.client.get(
            "/api/resource/Sales Order",
            params={
                "fields": '["name", "customer", "transaction_date", "status"]',
                "limit_page_length": limit,
            },
        )