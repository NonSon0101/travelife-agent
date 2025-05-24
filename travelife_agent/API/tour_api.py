import requests
from travelife_agent.API.auth_session import BASE_URL, SessionManager

TOUR_URL = f"{BASE_URL}/api/v1/tours"


def get_all_tours(filter_query=""):
  try:
    url = f"{TOUR_URL}/all{filter_query}"
    headers = SessionManager.get_headers()
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()["metadata"]
  except Exception as e:
    print(f"[TOUR API] get_all_tours error: {str(e)}")
    raise


def get_active_tours(filter_query=""):
  try:
    url = f"{TOUR_URL}/active-tours/all{filter_query}"
    headers = SessionManager.get_headers()
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()["metadata"]["tours"]
  except Exception as e:
    print(f"[TOUR API] get_active_tours error: {str(e)}")
    raise


def search_tour(input_value: str):
  try:
    print("data type to call api 1 % s" % type(input_value))
    print("data to call api 1 % s" % input_value)
    url = f"{BASE_URL}/api/v1/search/{input_value}?limit=5"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()["metadata"]
  except Exception as e:
    print(f"[TOUR API] search_tour error: {str(e)}")
    raise

def get_tour_detail(tour_id: str):
  try:
    url = f"{TOUR_URL}/{tour_id}"
    headers = SessionManager.get_headers()
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()["metadata"]
  except Exception as e:
    print(f"[TOUR API] get_tour_detail error: {str(e)}")
    raise
