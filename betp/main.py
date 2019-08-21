import odds_parser
import football_parser
from odds_calculator import *
import sys
import time
import datetime


def start(min_wager=1, max_wager=500, url="", blacklisted=[], topx=1, risk=[]):
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
            wagers = get_wagers(min_wager, max_wager, no_of_buckets)
            output = analyze(combinations, wagers, no_of_buckets, max_wager, 10, risk)
            # print(len(output))
            # sorted_deals = sorted(output, key=lambda deal: sum(deal.roi_array) / len(deal.roi_array), reverse=True)
            return sorted(output, key=lambda deal: min(deal.roi_array), reverse=True)[:topx]
    except Exception as exc:
        print("Error Occurred: ", exc)


def main():
    # st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y_%M_%D_%H_%M_%S')
    # sys.stdout = open("/tmp/report_" + st, 'w')
    match_list = []
    match_list = football_parser.get_all_matches("/football")

    for match in match_list:
        print("\nChecking match..." + match)
        print("Start Time: ", datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
        sorted_deals = start(max_wager=50,
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
