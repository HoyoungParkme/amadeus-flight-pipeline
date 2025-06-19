# api/amadeus_client.py

import requests
from config.settings import AMADEUS_CLIENT_ID, AMADEUS_CLIENT_SECRET

def get_access_token():
    url = "https://test.api.amadeus.com/v1/security/oauth2/token"
    payload = {
        "grant_type": "client_credentials",
        "client_id": AMADEUS_CLIENT_ID,
        "client_secret": AMADEUS_CLIENT_SECRET
    }
    response = requests.post(url, data=payload)
    return response.json().get("access_token")


def search_flights(access_token, origin, destination, date):
    url = "https://test.api.amadeus.com/v2/shopping/flight-offers"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    payload = {
        "currencyCode": "USD",
        "originDestinations": [
            {
                "id": "1",
                "originLocationCode": origin,
                "destinationLocationCode": destination,
                "departureDateTimeRange": {"date": date}
            }
        ],
        "travelers": [
            {"id": "1", "travelerType": "ADULT"}
        ],
        "sources": ["GDS"]
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()
