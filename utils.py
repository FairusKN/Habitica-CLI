"""
Utils
"""

from logger import log

def change_env() -> None:
    """
    Change API_KEY and USER_ID
    """

    from getpass import getpass

    from dotenv import load_dotenv, set_key

    try:
        load_dotenv()

        ENV_PATH = ".env"

        API_KEY = getpass("Habitica Api Key : ")
        USER_ID = input("Habitica User ID : ")

        X_CLIENT = f"{USER_ID}-habitica-cli"

        set_key(ENV_PATH, "API_KEY", API_KEY)
        set_key(ENV_PATH, "USER_ID", USER_ID)
        set_key(ENV_PATH, "X_CLIENT", X_CLIENT)
    except Exception as e:
        log.error(f"Error : {e}")



def get_API_status() -> bool:

    """
    Check if API is working or not
    """

    import requests
    from header import headers
    from constant import HABITICA_API_BASE

    url = f"{HABITICA_API_BASE}/status"
    response = requests.get(url, headers=headers).json()

    if response["success"]:
        if response["data"]["status"].lower() == "up":
            log.info("API is available")
        else:
            log.error("API is not available, will use cache instead")
    else:
        log.error("API is not available, will use cache instead")

