import requests
from header import headers
from logger import log
from constant import HABITICA_API_BASE

def get_API_status() -> bool:
    url = f"{HABITICA_API_BASE}/status"
    response = requests.get(url, headers=headers).json()

    if response["success"]:
        if response["data"]["status"].lower() == "up":
            log.info("API is available")
        else:
            log.error("API is not available, will use cache instead")
    else:
        log.error("API is not available, will use cache instead")
