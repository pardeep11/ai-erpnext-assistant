from app.erpnext.client import ERPNextClient

client = ERPNextClient()

result = client.get(
    "/api/resource/Item",
    params={
        "fields": '["name", "item_code", "item_name"]',
        "limit_page_length": 5,
    },
)

print(result)