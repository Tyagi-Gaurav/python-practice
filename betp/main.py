import odds_parser
import football_parser
from odds_calculator import *
import sys
import time
import datetime


def start(min_wager, max_wager, wagers2, wagers3, url="", blacklisted=[], topx=1, risk=[]):
    print("Running with min_wager = %d, max_wager=%d, blacklisted=%s, topx=%d, risk=%s" %
          (min_wager, max_wager, blacklisted, topx, risk))
    try:
        # Parse URL
        # content = htmlparser.parse('http://www.oddschecker.com/football/english/fa-cup/winner')
        content = odds_parser.parse(url, blacklisted)
        # print(content)

        # Get combinations for each match and put them into a file.
        comb = CombinatorialExplosion()
        combinations = comb.find_matching_odds(content)

        print("Total combinations: ", len(combinations))
        if len(combinations) > 0:
            no_of_buckets = len(combinations[0])
            wagers = []
            if no_of_buckets == 2:
                wagers = wagers2
            else:
                wagers = wagers3

            output = analyze(combinations, wagers, no_of_buckets, max_wager, 10, risk)
            # print(len(output))
            # sorted_deals = sorted(output, key=lambda deal: sum(deal.roi_array) / len(deal.roi_array), reverse=True)
            return sorted(output, key=lambda deal: min(deal.roi_array), reverse=True)[:topx]
    except Exception as exc:
        print("Error Occurred: ", exc)


def main():
    # st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y_%M_%D_%H_%M_%S')
    # sys.stdout = open("/tmp/report_" + st, 'w')
    match_list = ["http://www.oddschecker.com/football/europa-league/az-alkmaar-v-antwerp/winner",
                  "http://www.oddschecker.com/football/english/premier-league/brighton-v-southampton/winner",
                  "http://www.oddschecker.com/football/english/premier-league/sheffield-utd-v-leicester/winner",
                  "http://www.oddschecker.com/football/english/championship/derby-v-west-brom/winner",
                  "http://www.oddschecker.com/football/english/championship/huddersfield-v-reading/winner",
                  "http://www.oddschecker.com/football/english/championship/preston-v-sheffield-wednesday/winner"]
    # match_list = football_parser.get_all_matches("/football")

    print("Number of matches", len(match_list))

    min_wager = 100
    max_wager = 200
    wagers2 = []  # get_wagers(min_wager, max_wager, 2)
    wagers3 = get_wagers(min_wager, max_wager, 3)

    for match in match_list:
        print("\nChecking match..." + match)
        print("Start Time: ", datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
        sorted_deals = start(min_wager, max_wager, wagers2,
                             wagers3,
                             url=match,
                             blacklisted=[],
                             topx=1,
                             risk=[0.0, 5.0, 0.0])

        if sorted_deals:
            print(*sorted_deals, sep="\n")
        else:
            print("No Odds Found")
        print("End Time: ", datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))


if __name__ == '__main__':
    main()
