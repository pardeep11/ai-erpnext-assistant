from app.erpnext.client import ERPNextClient


class SalesOrderService:
    def __init__(self):
        self.client = ERPNextClient()

    def get_sales_orders(self, customer, limit=10):
        return self.client.get(
            "/api/resource/Sales Order",
            params={
                "fields": '["name", "customer", "transaction_date", "status"]',
                "filters": f'[["customer", "=", "{customer}"]]',
                "limit_page_length": limit,
            },
        )

    def get_order_counts(self, orders):
        order_list = orders.get("data", [])

        counts = {
            "total": len(order_list),
            "completed": 0,
            "pending": 0,
            "cancelled": 0,
            "draft": 0,
            "to_deliver": 0,
        }

        for order in order_list:
            status = order.get("status")

            if status == "Completed":
                counts["completed"] += 1

            elif status == "To Deliver and Bill":
                counts["pending"] += 1

            elif status == "Cancelled":
                counts["cancelled"] += 1

            elif status == "Draft":
                counts["draft"] += 1

            elif status == "To Deliver":
                counts["to_deliver"] += 1

        return counts