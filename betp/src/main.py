import datetime
import time
import traceback

import normal_match_parser
import odds_parser
from odds_calculator import *
from analyze_with_wagers import *
from analyze_with_odds import *


def start(max_wager, wagers2, wagers3, url="", hat_list=[], hat_list_flag=0, topx=1, risk=[]):
    try:
        # Parse URL
        content = odds_parser.parse(url, hat_list, hat_list_flag)
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


def start2(min_expected_return,
           max_expected_return,
           combinations=[],
           topx=1,
           risk=[],
           min_profit_percentage=2):
    try:
        print("Total combinations: %d" % len(combinations))
        output = analyze_with_odds(min_expected_return,
                                   max_expected_return,
                                   combinations,
                                   10,
                                   risk,
                                   min_profit_percentage)
        # print(len(output))
        # return sorted(output, key=lambda deal: min(deal.roi_array), reverse=True)[:topx]
        return list(filter(lambda x: len(x.roi_array) > 0, output))[:topx]
    except Exception as exc:
        print("Error Occurred: ", exc)
        traceback.print_exc()


def main():
    # match_list = [
    #     "http://www.oddschecker.com/american-football/cfl/edmonton-eskimos-at-calgary-stampeders/winner"]
    # match_list = normal_match_parser.get_all_matches("/football")
    match_list = normal_match_parser.get_all_matches("/football/english/premier-league")
    # match_list = normal_match_parser.get_all_matches("/american-football")
    # match_list = normal_match_parser.get_all_matches("/basketball")
    # match_list = normal_match_parser.get_all_matches("/baseball")
    # match_list = normal_match_parser.get_all_matches("/cricket")
    # match_list = normal_match_parser.get_all_matches("/badminton")

    print("Number of matches", len(match_list))

    min_wager = 1
    max_wager = 10
    # hat_list = ["Man City", "Liverpool", "Tottenham", "Chelsea", "Man Utd", "Arsenal", "Wolves", "Everton", "Westham",
    #             "Leicester", "Watford", "Crystal Palace"]
    hat_list = []
    hat_list_flag = 0  # 1 - Whitelist, 0 - blacklist
    topx = 1
    risk = [0.0, 5.0, 0.0]
    wagers2 = get_wagers(min_wager, max_wager, 2)
    wagers3 = get_wagers(min_wager, max_wager, 3)

    print("Start Time: ", datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
    print("Running with min_wager = %d, max_wager=%d, hat_list=%s, hat_list_flag=%d, topx=%d, risk=%s" %
          (min_wager, max_wager, hat_list, hat_list_flag, topx, risk))

    matched_deals = []

    for match in match_list:
        print("\nChecking match..." + match)

        # Parse URL
        content = odds_parser.parse(match, hat_list, hat_list_flag)
        # Get combinations for each match and put them into a file.
        comb = CombinatorialExplosion()
        combinations = comb.find_matching_odds(content)

        sorted_deals = start(max_wager,
                             wagers2,
                             wagers3,
                             url=match,
                             hat_list=hat_list,
                             hat_list_flag=0,
                             topx=topx,
                             risk=risk)

        if sorted_deals:
            matched_deals += sorted_deals

    print("End Time: ", datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
    print("###############################################################################")
    print("######################### Final Output ########################################")
    print("###############################################################################")
    print(*matched_deals, sep="\n\n")


def log(message, deals):
    print(message)
    print(*deals, sep="\n\n")


if __name__ == '__main__':
    main()
