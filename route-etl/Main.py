from ParsePlane import parse_planes
from Routes import parse_routes
from airlines import parse_airlines
from airports import parse_airports
from pymongo import MongoClient


# read plane CSV into a list of plane object
# Assign each record a unique ID.
# Deserialize CSV into json
# Store Json into Mongo
# Be able to query data
def insert_objects(db, collection, data, attribute):
    db[collection].drop()
    db[collection].insert_many([{attribute: item.__dict__} for item in data])
    print('Created {0} records'.format(db[collection].count_documents({})))


def main():
    client = MongoClient("mongodb+srv://m220student:m220password@mflix-hnyn8.mongodb.net")
    db = client.airdata

    planes = parse_planes()
    routes = parse_routes()
    airlines = parse_airlines()
    airports = parse_airports()

    insert_objects(db, "planes", planes, "plane")
    insert_objects(db, "routes", routes, "route")
    insert_objects(db, "airlines", airlines, "airline")
    insert_objects(db, "airports", airports, "airport")


if __name__ == '__main__':
    main()
