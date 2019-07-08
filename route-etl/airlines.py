import csv


# Airline ID	Unique OpenFlights identifier for this airline.
# Name	Name of the airline.
# Alias	Alias of the airline. For example, All Nippon Airways is commonly known as "ANA".
# IATA	2-letter IATA code, if available.
# ICAO	3-letter ICAO code, if available.
# Callsign	Airline callsign.
# Country	Country or territory where airline is incorporated.
# Active	"Y" if the airline is or has until recently been operational, "N" if it is defunct. This field
#       is not reliable: in particular, major airlines that stopped flying long ago, but have not had their IATA code
#       reassigned (eg. Ansett/AN), will incorrectly show as "Y".

class Airlines:
    def __init__(self, name, alias,
                 iata_code, icao_code, callsign,
                 country, active):
        self.active = active
        self.country = country
        self.callsign = callsign
        self.icao_code = icao_code
        self.iata_code = iata_code
        self.alias = alias
        self.name = name

    def __str__(self):
        return "name: {0}, " \
               "alias: {1}, " \
               "iata_code: {2}, " \
               "icao_code: {3}, " \
               "callsign: {4}, " \
               "country: {5}, " \
               "active: {6}".format(
            self.name,
            self.alias,
            self.iata_code,
            self.icao_code,
            self.callsign,
            self.country,
            self.active
        )


def parse_airlines():
    airlines = {}
    with open("data/airlines.dat") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            line_count += 1
            airline = Airlines(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            if airline.iata_code != '\\N':
                airlines[row[2]] = airline

        print(f'Processed {line_count} lines.')
    #print(*airlines, sep='\n')
    return airlines
