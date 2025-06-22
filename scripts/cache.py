import json
import os
from datetime import datetime

import requests

from .constant import USER_URL
from .header import headers
from .logger import log


def save_cache(data, filename: str) -> None:
    os.makedirs(
        os.path.dirname(filename), exist_ok=True
    )  # <-- this ensures parent dirs exist
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def is_cache_valid(filename: str = "cache/user_data.json", max_age=45):
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
    url: str = USER_URL,
    max_age=45,
    force_refresh=False,
):
    try:
        filename = f"cache/{endpoint_name}.json"
        if not force_refresh and is_cache_valid(filename, max_age):
            with open(filename, "r") as f:
                return json.load(f)["data"]
        else:
            data = fetch_func(url)
            save_cache(data, filename)
            return data
    except Exception as e:
        message = "An exception of type {0} occurred. Arguments:\n{1!r}".format(
            type(e).__name__, e.args
        )
        log.error("Error", message)
