import csv


# Read & Validate Routes
# Airline	2-letter (IATA) or 3-letter (ICAO) code of the airline.
# Airline ID	Unique OpenFlights identifier for airline (see Airline).
# Source airport	3-letter (IATA) or 4-letter (ICAO) code of the source airport.
# Source airport ID	Unique OpenFlights identifier for source airport (see Airport)
# Destination airport	3-letter (IATA) or 4-letter (ICAO) code of the destination airport.
# Destination airport ID	Unique OpenFlights identifier for destination airport (see Airport)
# Codeshare	"Y" if this flight is a codeshare (that is, not operated by Airline, but another carrier), empty otherwise.
# Stops	Number of stops on this flight ("0" for direct)
# Equipment	3-letter codes for plane type(s) generally used on this flight, separated by spaces

class Routes:
    def __init__(self, airline_code, airline_id,
                 src_apt, src_apt_id, dest_apt,
                 dest_apt_id, code_share, num_stops,
                 equip_code):
        self.airline_code = airline_code
        self.airline_id = airline_id
        self.src_apt = src_apt
        self.src_apt_id = src_apt_id
        self.dest_apt = dest_apt
        self.dest_apt_id = dest_apt_id
        self.code_share = code_share
        self.num_stops = num_stops
        self.equip_code = equip_code

    def __str__(self):
        return "airline_code: {0}, " \
               "airline_id: {1}, " \
               "source_airport: {2}, " \
               "source_airport_id: {3}, " \
               "dest_airport: {4}, " \
               "dest_airport_id: {5}, " \
               "num_stops: {6}, " \
               "code_share: {7}, " \
               "equip_code: {8}".format(
            self.airline_code,
            self.airline_id,
            self.src_apt,
            self.src_apt_id,
            self.dest_apt,
            self.dest_apt_id,
            self.num_stops,
            self.code_share,
            self.equip_code,
        )


def parse_routes():
    routes = []
    with open("data/routes.dat") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            line_count += 1
            routes.append(Routes(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
        print(f'Processed {line_count} lines.')
    #print(*routes, sep='\n')
    return routes
