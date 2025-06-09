import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
USER_ID = os.getenv("USER_ID")
X_CLIENT = os.getenv("X_CLIENT")

headers = {"x-api-user": USER_ID, "x-api-key": API_KEY, "x-client": X_CLIENT}


def get_API_status() -> bool:
    url = "https://habitica.com/api/v3/status"
    response = requests.get(url, headers=headers).json()

    if response["success"]:
        if response["data"]["status"].lower() == "up":
            return True
        else:
            return False
    else:
        return False
