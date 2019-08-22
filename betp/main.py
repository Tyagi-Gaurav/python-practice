import datetime
import time
import traceback

import normal_match_parser
import odds_parser
from odds_calculator import *


def start(min_wager, max_wager, wagers2, wagers3, url="", blacklisted=[], topx=1, risk=[]):
    try:
        # Parse URL
        content = odds_parser.parse(url, blacklisted)
        # Get combinations for each match and put them into a file.
        comb = CombinatorialExplosion()
        combinations = comb.find_matching_odds(content)

        if len(combinations) > 0:
            no_of_buckets = len(combinations[0])
            wagers = [max_wager]
            if no_of_buckets == 1:
                risk = [0.0]
            elif no_of_buckets == 2:
                wagers = wagers2
                risk = [0.0, 0.0]
            else:
                wagers = wagers3
            print("Total combinations: %d, Using Wager type: %d" % (len(combinations), no_of_buckets))
            output = analyze(combinations, wagers, no_of_buckets, max_wager, 10, risk)
            # print(len(output))
            # sorted_deals = sorted(output, key=lambda deal: sum(deal.roi_array) / len(deal.roi_array), reverse=True)
            return sorted(output, key=lambda deal: min(deal.roi_array), reverse=True)[:topx]
    except Exception as exc:
        print("Error Occurred: ", exc)
        traceback.print_exc()


def main():
    # match_list = ["http://www.oddschecker.com/football/english/premier-league/aston-villa-v-everton/winner"]
    # match_list = normal_match_parser.get_all_matches("/football")
    # match_list = normal_match_parser.get_all_matches("/american-football")
    # match_list = normal_match_parser.get_all_matches("/basketball")
    # match_list = normal_match_parser.get_all_matches("/baseball")
    # match_list = normal_match_parser.get_all_matches("/cricket")
    # match_list = normal_match_parser.get_all_matches("/badminton")

    print("Number of matches", len(match_list))

    min_wager = 1
    max_wager = 10
    blacklisted = []
    topx = 1
    risk = [0.0, 5.0, 0.0]
    wagers2 = get_wagers(min_wager, max_wager, 2)
    wagers3 = get_wagers(min_wager, max_wager, 3)

    print("Start Time: ", datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
    print("Running with min_wager = %d, max_wager=%d, blacklisted=%s, topx=%d, risk=%s" %
          (min_wager, max_wager, blacklisted, topx, risk))

    matched_deals = []

    for match in match_list:
        print("\nChecking match..." + match)

        sorted_deals = start(min_wager,
                             max_wager,
                             wagers2,
                             wagers3,
                             url=match,
                             blacklisted=blacklisted,
                             topx=topx,
                             risk=risk)

        if sorted_deals:
            matched_deals += sorted_deals

    print("End Time: ", datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
    print("###############################################################################")
    print("######################### Final Output ########################################")
    print("###############################################################################")
    print(*matched_deals, sep="\n\n")


if __name__ == '__main__':
    main()
