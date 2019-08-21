import odd_checker_parser
from odds_calculator import *


def start(min_wager=1, max_wager=500, url="", blacklisted=[], topx=1, risk=[]):
    try:
        # Parse URL
        # content = htmlparser.parse('http://www.oddschecker.com/football/english/fa-cup/winner')
        content = odd_checker_parser.parse(url, blacklisted)
        # print(content)

        # Get combinations for each match and put them into a file.
        comb = CombinatorialExplosion()
        combinations = comb.find_matching_odds(content)

        print("Total combinations: ", len(combinations))
        if len(combinations) > 0:
            no_of_buckets = len(combinations[0])
            wagers = get_wagers(min_wager, max_wager, no_of_buckets)
            output = analyze(combinations, wagers, no_of_buckets, max_wager, 10, risk)
            # print(len(output))
            # sorted_deals = sorted(output, key=lambda deal: sum(deal.roi_array) / len(deal.roi_array), reverse=True)
            return sorted(output, key=lambda deal: min(deal.roi_array), reverse=True)[:topx]
    except Exception as exc:
        print("Error Occurred: ", exc)


def main():
    sorted_deals = start(max_wager=50,
                         url='https://www.oddschecker.com/football/europa-league/fc-astana-v-bate-borisov/winner',
                         blacklisted=[],
                         topx=1,
                         risk=[0.0, 0.0, 0.0])

    if sorted_deals:
        print(*sorted_deals, sep="\n")


if __name__ == '__main__':
    main()
