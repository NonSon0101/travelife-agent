import os
import requests
from dotenv import load_dotenv

load_dotenv()  

BASE_URL = os.getenv("BASE_URL")
AUTH_URL = f"{BASE_URL}/api/v1/auth"
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

class SessionManager:
  _access_token = None
  _user = None

  @classmethod
  def login(cls):
    try:
      payload = {
        "email": USERNAME,
        "password": PASSWORD
      }
      response = requests.post(f"{AUTH_URL}/login", json=payload)
      response.raise_for_status()
      metadata = response.json()["metadata"]
      cls._access_token = metadata["accessToken"]
      cls._user = metadata["user"]
    except Exception as e:
      print(f"[AUTH ERROR] Failed to login: {str(e)}")
      raise

  @classmethod
  def get_token(cls) -> str:
    if not cls._access_token:
      cls.login()
    return cls._access_token

  @classmethod
  def get_headers(cls) -> dict:
    token = cls.get_token()
    return {"Authorization": f"Bearer {token}"}

