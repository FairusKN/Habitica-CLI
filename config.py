from getpass import getpass

from dotenv import load_dotenv, set_key

load_dotenv()

ENV_PATH = ".env"


def change_env():
    API_KEY = getpass("Habitica Api Key : ")
    USER_ID = input("Habitica User ID : ")

    X_CLIENT = f"{USER_ID}-habitica-cli"

    set_key(ENV_PATH, "API_KEY", API_KEY)
    set_key(ENV_PATH, "USER_ID", USER_ID)
    set_key(ENV_PATH, "X_CLIENT", X_CLIENT)
