from math import sin, cos, sqrt, atan2, radians
from Routes import parse_routes
from airlines import parse_airlines
from airports import parse_airports, Airports
from ParsePlane import parse_planes
from pymongo import MongoClient
from math import sin, cos, sqrt, atan2, radians
import json


# read CSV into a list of object
# Deserialize CSV into json
# Store Json into Mongo
def insert_objects(db, collection, data, attribute):
    print('Number of records to process {0} for table {1}'.format(len(data), collection))
    # for item in data:
    #     print(item, data[item])
    db[collection].insert_many([{attribute: data[item].__dict__} for item in data])
    print('Created {0} records for table {1}'.format(db[collection].count_documents({}), collection))


def drop_objects(db, collections):
    for table in collections:
        db[table].drop()
        print("Dropped {}".format(table))


'''
Route : {
    "source" : "",
    "destination" : "",
    "sourceAirport" : "",
    "destinationAirport" : "",
    "distance" : "",
    "time" : "",
    "price" : "",
    "plane" : "",
    "airline" : ""
}
'''


def augment_routes_information(routes, airports):
    default_src_airport = Airports(507, "London Heathrow Airport", "London", "United Kingdom", "LHR", "EGLL", 51.4706,
                                  -0.461941, 83, 0, "E", "Europe/London", "airport")
    default_dst_airport = Airports(3797, "John F Kennedy International Airport", "New York", "United States", "JFK",
                                  "KJFK", 40.63980103, -73.77890015, 13, -5, "A", "America/New_York", "airport")
    price_per_km = 0.1
    route_map = {}
    i = 1
    for rt in routes:
        src_apt = airports.get(rt.src_apt, default_src_airport)
        dest_apt = airports.get(rt.dest_apt, default_dst_airport)
        rt.distance_in_km = calculate_distance(src_apt.latitude, src_apt.longitude, dest_apt.latitude,
                                               dest_apt.longitude)
        rt.price = price_per_km * rt.distance_in_km
        route_map[i] = rt
        # print(json.dumps(routes[i].__dict__))
        i = i + 1
    return route_map


def calculate_distance(src_lat, src_long, dest_lat, dest_long):
    # approximate radius of earth in km
    R = 6373.0

    lat1 = radians(float(src_lat))
    lon1 = radians(float(src_long))
    lat2 = radians(float(dest_lat))
    lon2 = radians(float(dest_long))

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c


def query(db, query, table):
    doc = db[table].find(query)
    for x in doc:
        print(x)


def main():
    client = MongoClient("mongodb+srv://m220student:m220password@mflix-hnyn8.mongodb.net")
    db = client.airdata

    planes = parse_planes()
    routes = parse_routes()
    airlines = parse_airlines()
    airports = parse_airports()

    drop_objects(db, ["planes", "airports", "routes", "airlines"])
    insert_objects(db, "planes", planes, "plane")
    insert_objects(db, "airlines", airlines, "airline")
    insert_objects(db, "airports", airports, "airport")
    drop_objects(db, ["routes"])
    route_aug = augment_routes_information(routes, airports)
    insert_objects(db, "routes", route_aug, "route")
    query(db, {"plane.iata_code": "ND2"}, "planes")
    query(db, {"airline.icao_code": "BL"}, "airlines")
    query(db, {"airport.iata_code": "THU"}, "airports")
    # Direct Routes
    query(db, {"$and": [{"route.dest_apt": "LHR"}, {"route.src_apt": "JFK"}]}, "routes")

    # 1 Stop routes
    query(db,
          {"$or": [{"$and": [{"route.dest_apt": "LHR"}, {"route.src_apt": {"$ne": "JFK"}}]},
                   {"$and": [{"route.src_apt": "JFK"}, {"route.dest_apt": {"$ne": "LHR"}}]}]},
          "routes")


if __name__ == '__main__':
    main()
