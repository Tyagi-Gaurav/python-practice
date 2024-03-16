from datetime import datetime as dt
import requests
from flight_data import FlightData


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def __init__(self):
        self.api_key = "MrYl7HhVZnpnsxF3ptWLY4Kt9HBDL_9p"
        self.locations_base_url = "https://api.tequila.kiwi.com"
        self.search_base_url = "https://api.tequila.kiwi.com/v2/search"

    def get_iata_codes(self, cities):
        iata_codes = {}
        for city in cities:
            params = {
                "term": city,
                "locale": "en-US",
                "location_types": "city",
                "limit": 1,
                "active_only": True
            }
            headers = {
                "apikey": self.api_key
            }
            response = requests.get(url=f"{self.locations_base_url}/locations/query", params=params, headers=headers)
            print(response.json())
            response = response.json()
            iata_codes[city] = response["locations"][0]["code"]

        return iata_codes

    def search(self, search_data: [FlightData]):
        results = []
        for search_param in search_data:
            headers = {
                "apikey": self.api_key
            }
            params = {
                "fly_from": f"city:{search_param.from_city}",
                "fly_to": f"city:{search_param.to_city}",
                "date_from": search_param.date_from,
                "date_to": search_param.date_to,
                "adults": search_param.adults,
                "children": search_param.kids,
                "selected_cabins": search_param.cabin,
                "curr": search_param.curr,
                "locale": search_param.locale,
                # "price_to": search_param.max_price,
                "sort": "price",
                "limit": 3,
                "nights_in_dst_from": 7,
                "nights_in_dst_to": 28,
                "max_stopovers": 0
            }
            response = requests.get(url=f"{self.search_base_url}", params=params, headers=headers)
            response.raise_for_status()
            json_response = response.json()

            for data in json_response.get("data"):
                if data["availability"]["seats"] is not None:
                    results.append(data)

        return results
        # Support for airport changes for direct flights only (Have something in excel sheet)
        # Calculate total price of ticket in GBP
        # Report
        # Increase limit of results and then filter by seats availability
        # Does specifying destination nights cause any changes in response?
        # Use return_from date or return_to date
        # Later - Create HTML UI to show this

        # print(response.json())
