import requests

from data.config import load_erpnext_keys


class ERPNextClient:
    def __init__(self):
        keys = load_erpnext_keys("api_all_keys.json")

        self.base_url = keys["url"]

        self.api_key = (
            keys.get("erpnext_api_key")
            or keys.get("api_key")
        )

        self.api_secret = (
            keys.get("erpnext_api_secret")
            or keys.get("api_secret")
        )

        self.headers = {
            "Authorization": f"token {self.api_key}:{self.api_secret}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    def get(self, endpoint, params=None):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"

        response = requests.get(
            url,
            headers=self.headers,
            params=params,
            timeout=10,
        )

        response.raise_for_status()

        return response.json()