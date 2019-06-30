import csv


# Read & Validate Planes
# Name	Full name of the aircraft.
# IATA code	Unique three-letter IATA identifier for the aircraft.
# ICAO code	Unique four-letter ICAO identifier for the aircraft

class Plane:
    def __init__(self, name, iata_code, icao_code):
        self.icao_code = icao_code
        self.iata_code = iata_code
        self.name = name

    def __str__(self):
        return "name: {0}, iata: {1}, icao: {2}".format(self.name, self.iata_code, self.icao_code)


def parse_planes():
    planes = []
    with open("data/planes.dat") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            line_count += 1
            planes.append(Plane(row[0], row[1], row[2]))
        print(f'Processed {line_count} lines.')
    print(*planes, sep='\n')
    return planes
