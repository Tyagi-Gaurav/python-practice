import json

import requests


class DataManager:

    def __init__(self):
        self.base_url = "https://api.sheety.co/3a70872e35e94b37f72beacdea0fa550/flightDeals/prices"

    def get_routes(self):
        response = requests.get(self.base_url)
        response = response.json()
        return response.get("prices")

    def get_cities_without_iata_codes(self):
        routes = self.get_routes()
        return [route.get("city") for route in routes if route.get("iataCode") == '']

    def update_iata_codes(self, iata_codes):
        response = requests.get(self.base_url)
        response = response.json()
        routes = response.get("prices")

        for route in routes:
            city = route.get("city")
            if route.get("iataCode") == '':
                url = f"{self.base_url}/{route.get("id")}"
                body = json.dumps({
                    "price": {
                        "city": city,
                        "iataCode": iata_codes.get(city)
                    }
                })
                headers = {
                    "Content-Type": "application/json"
                }
                response = requests.put(url=url, data=body, headers=headers)
                response.raise_for_status()
                print (f"Checking return fare from {route.get("from_city")} to {city}")
                print (response.json())
                # Find lowest
