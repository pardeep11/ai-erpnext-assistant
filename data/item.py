import requests
from data.config import load_erpnext_keys

def get_erpnext_items(limit=10):
    # Load configuration dictionary from JSON file
    keys = load_erpnext_keys("/home/frappe/api_all_keys.json")

    endpoint = f"{keys['url']}/api/resource/Item"

    # Support both key naming variants (api_key vs erpnext_api_key)
    api_key = keys.get("erpnext_api_key") or keys.get("api_key")
    api_secret = keys.get("erpnext_api_secret") or keys.get("api_secret")

    headers = {
        "Authorization": f"token {api_key}:{api_secret}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    params = {
        "fields": '["name", "item_code", "item_name", "item_group", "standard_rate"]',
        "limit_page_length": limit
    }

    response = requests.get(endpoint, headers=headers, params=params)
    response.raise_for_status()

    return response.json().get("data", [])

if __name__ == "__main__":
    items = get_erpnext_items(limit=5)
    for item in items:
        print(item)
