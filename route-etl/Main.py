from ParsePlane import parse_planes
from Routes import parse_routes
from airlines import parse_airlines
from airports import parse_airports
from pymongo import MongoClient
from math import sin, cos, sqrt, atan2, radians


# read CSV into a list of object
# Deserialize CSV into json
# Store Json into Mongo
def insert_objects(db, collection, data, attribute):
    db[collection].drop()
    db[collection].insert_many([{attribute: item.__dict__} for item in data])
    print('Created {0} records'.format(db[collection].count_documents({})))


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


def augmentRoutesInformation(routes, airports):
    for i in range(0, 10):
        src_apt = airports[routes[i].src_apt]
        dest_apt = airports[routes[i].dest_apt]
        routes[i].distance_in_km = calculate_distance(src_apt.latitude, src_apt.longitude, dest_apt.latitude, dest_apt.longitude)
        print(routes[i])


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


def main():
    # client = MongoClient("mongodb+srv://m220student:m220password@mflix-hnyn8.mongodb.net")
    # db = client.airdata

    # planes = parse_planes()
    routes = parse_routes()
    # airlines = parse_airlines()
    airports = parse_airports()
    #print(*airports.values(), sep='\n')

    # insert_objects(db, "planes", planes, "plane")
    # insert_objects(db, "airlines", airlines, "airline")
    # sinsert_objects(db, "airports", airports, "airport")
    augmentRoutesInformation(routes, airports)
    # insert_objects(db, "routes", routes, "route")


if __name__ == '__main__':
    main()
