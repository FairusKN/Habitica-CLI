import json
from datetime import datetime

import requests

from header import headers


def save_cache(data, filename: str = "cache/user_data.json"):
    cache = {"timestamp": datetime.utcnow().isoformat(), "data": data}
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(cache, f, indent=4)


def is_cache_valid(filename: str = "cache/user_data.json", max_age=3600):
    try:
        with open(filename, "r") as f:
            cache = json.load(f)
            last_fetch = datetime.fromisoformat(cache["timestamp"])
            return (datetime.utcnow() - last_fetch).total_seconds() < max_age
    except FileNotFoundError:
        return False


def fetch_func(url: str):
    response = requests.get(url, headers=headers)
    data = response.json()["data"]
    return data


def get_data_with_cache(
    endpoint_name: str = "user_data",
    url: str = "https://habitica.com/api/v3/user",
    max_age=3600,
):
    filename = f"cache/{endpoint_name}.json"
    if is_cache_valid(filename, max_age):
        with open(filename, "r") as f:
            return json.load(f)["data"]
    else:
        data = fetch_func(url)
        save_cache(data, filename)
        return data
