import csv


# Read & Validate Airports
# Airport ID	Unique OpenFlights identifier for this airport.
# Name	Name of airport. May or may not contain the City name.
# City	Main city served by airport. May be spelled differently from Name. *** May be "Null" ****
# Country	Country or territory where airport is located. See countries.dat to cross-reference to ISO 3166-1 codes.
# IATA	3-letter IATA code. Null if not assigned/unknown. ***** \N
# ICAO	4-letter ICAO code. Null if not assigned. ***** \N
# Latitude	Decimal degrees, usually to six significant digits. Negative is South, positive is North.
# Longitude	Decimal degrees, usually to six significant digits. Negative is West, positive is East.
# Altitude	In feet.
# Timezone	Hours offset from UTC. Fractional hours are expressed as decimals, eg. India is 5.5.
# DST	Daylight savings time. One of E (Europe), A (US/Canada), S (South America), O (Australia), Z (New Zealand), N (None) or U (Unknown). See also: Help: Time
# Tz database time zone	Timezone in "tz" (Olson) format, eg. "America/Los_Angeles".
# Type	Type of the airport. Value "airport" for air terminals, "station" for train stations, "port" for ferry terminals and "unknown" if not known. In airports.csv, only type=airport is included.
# Source	Source of this data. "OurAirports" for data sourced from OurAirports, "Legacy" for old data not matched to OurAirports (mostly DAFIF), "User" for unverified user contributions. In airports.csv, only source=OurAirports is included.

class Airports:
    def __init__(self, airport_id, name,
                 city, country, iata_code,
                 icao_code, latitude, longitude,
                 altitude, timezone, dst,
                 tz, type):
        self.type = type
        self.tz = tz
        self.dst = dst
        self.timezone = timezone
        self.altitude = altitude
        self.longitude = longitude
        self.latitude = latitude
        self.icao_code = icao_code
        self.iata_code = iata_code
        self.city = city
        self.country = country
        self.name = name
        self.airport_id = airport_id

    def __str__(self):
        return "type: {0}, " \
               "tz: {1}, " \
               "dst: {2}, " \
               "timezone: {3}, " \
               "altitude: {4}, " \
               "longitude: {5}, " \
               "latitude: {6}," \
               "icao_code: {7}," \
               "iata_code: {8}," \
               "city: {9}," \
               "country: {10}," \
               "name: {11}," \
               "airport_id: {12}".format(
            self.type,
            self.tz,
            self.dst,
            self.timezone,
            self.altitude,
            self.longitude,
            self.latitude,
            self.icao_code,
            self.iata_code,
            self.city,
            self.country,
            self.name,
            self.airport_id)


def parse_airports():
    airports_by_iata_code = {}
    with open("data/airports.dat") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            line_count += 1
            airport_detail = Airports(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                                      row[10],
                                      row[11], row[12])
            if airport_detail.iata_code != '\\N':
                airports_by_iata_code[row[4]] = airport_detail
    print(f'Processed {line_count} lines.')
    return airports_by_iata_code
