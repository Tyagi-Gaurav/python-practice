import csv
import htmlparser


class Match:
    def __init__(self, match, odds_list={}):
        self.match = match
        self.odds_list = odds_list

    def __str__(self):
        return "match: {0}, odds: {1}" \
            .format(self.match, self.odds_list)


class Odds:
    def __init__(self, company, home=0, draw=0, away=0, win=0):
        self.company = company
        self.home = home
        self.draw = draw
        self.away = away
        self.win = win

    def __str__(self):
        return "company: {0}, home: {1}, draw: {2}, away: {3}" \
            .format(self.company, self.home, self.draw, self.away)


def process_headers(headers):
    match_data = []
    for match_name in headers:
        match_data.append(Match(match_name))
    return match_data


def process_row(row, match_data):
    if len(row) == 0:
        return

    cell = row[0].split("/")
    company = cell[0]
    i = 1
    while i < len(row):
        if company in match_data[i - 1].odds_list:
            data = match_data[i - 1].odds_list[company]
        else:
            data = Odds(company)
            match_data[i - 1].odds_list[company] = data

        if cell[1] == 'H':
            data.home = row[i]
        elif cell[1] == 'D':
            data.draw = row[i]
        elif cell[1] == 'A':
            data.away = row[i]
        else:
            data.win = row[i]

        i = i + 1


def read_rows():
    with open("data.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        headers = next(csv_reader)
        match_data = process_headers(strip_empty(headers))
        for row in csv_reader:
            process_row(strip_empty(row), match_data)

    return match_data


def strip_empty(list_with_empty_strings):
    return list(filter(None, list_with_empty_strings))


def find_quote(home, draw, away, limit):
    h = d = a = 1
    minimum_stake = h + d + a
    while minimum_stake < limit:
        if home != 0 and home * h < minimum_stake:
            h = h + 1
        elif draw != 0 and draw * d < minimum_stake:
            d = d + 1
        elif away != 0 and away * a < minimum_stake:
            a = a + 1
        else:
            return h, d, a
        minimum_stake = h + d + a
    return -1, -1, -1


def main():
    limit = 100

    #Parse URL
    content = htmlparser.parse('http://www.oddschecker.com/football/english/fa-cup/winner')
    print(content)

    # Read Data
    #match_data = read_rows()

    # Get combinations for each match
    

    # For each combination calculate candidate quotes
    #print(find_quote(1.125, 8.5, 21, limit))

    # Sort candidate quotes by


if __name__ == '__main__':
    main()
