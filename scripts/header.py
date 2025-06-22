import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
USER_ID = os.getenv("USER_ID")
X_CLIENT = os.getenv("X_CLIENT")

headers = {"x-api-user": USER_ID, "x-api-key": API_KEY, "x-client": X_CLIENT}
