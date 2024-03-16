# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from datetime import datetime as dt, timedelta

# KiwiFlightSearch https://partners.kiwi.com/
# https://tequila.kiwi.com/portal/docs/tequila_api
dm = DataManager()
fs = FlightSearch()


# cities = dm.get_cities_without_iata_codes()
# iata_codes = fs.get_iata_codes(cities)
# dm.update_iata_codes(iata_codes)
# print("Iata codes updated")

def report(data):
    # print (data)
    departure_date_and_time = dt.fromisoformat(data["route"][0]["local_departure"]).strftime("%d/%m/%Y %H:%M")
    departure_flight = f"{data["route"][0]["airline"]} {data["route"][0]["flight_no"]}"

    arrival_date_and_time = dt.fromisoformat(data["route"][1]["local_departure"]).strftime("%d/%m/%Y %H:%M")
    arrival_flight = f"{data["route"][1]["airline"]} {data["route"][1]["flight_no"]}"

    print(f"From: {data["cityFrom"]}\n"
          f"To: {data["cityTo"]}\n"
          f"Number of Nights: {data["nightsInDest"]}\n"
          f"Departure Date & Time: {departure_date_and_time}\n"
          f"Departure Flight: {departure_flight}\n"
          f"Arrival Date & Time: {arrival_date_and_time}\n"
          f"Arrival Flight: {arrival_flight}\n"
          f"Price: £{data["price"]}\n\n")


routes = dm.get_routes()
# routes = [
#     {'city': 'Paris', 'iataCode': 'PAR', 'id': 2, 'lowestPrice': 1000},
#     {'city': 'Tokyo', 'iataCode': 'TYO', 'id': 3, 'lowestPrice': 1000}
# ]
print("Got routes to check")

today = dt.now()
six_month_from_today = dt.today().date() + timedelta(days=180)

formatted_today = today.strftime("%d/%m/%Y")
formatted_end_date = six_month_from_today.strftime("%d/%m/%Y")

print(f"Checking from {formatted_today} to {formatted_end_date}")

flights_data = [
    FlightData(date_from=formatted_today,
               date_to=formatted_end_date,
               to_city=route["iataCode"],
               max_price=route["lowestPrice"])
    for route in routes]

results = fs.search(flights_data)
for result in results:
    report(result)
