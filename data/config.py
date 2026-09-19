import json
import os

def load_erpnext_keys(filename="data/api_all_keys.json"):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, filename) if not os.path.isabs(filename) else filename

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Configuration file '{file_path}' not found.")

    with open(file_path, "r") as file:
        data = json.load(file)

    # Automatically prepend http:// if missing
    url = data.get("url", "").strip().rstrip("/")
    if url and not (url.startswith("http://") or url.startswith("https://")):
        data["url"] = f"http://{url}"
    else:
        data["url"] = url

    return data
