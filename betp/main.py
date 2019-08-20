import odd_checker_parser
from odds_calculator import *


def main():
    min_wager = 50
    max_wager = 100

    # Parse URL
    # content = htmlparser.parse('http://www.oddschecker.com/football/english/fa-cup/winner')
    content = odd_checker_parser.parse(
        'https://www.oddschecker.com/football/english/championship/birmingham-v-barnsley/winner')
    # print(content)

    # Get combinations for each match and put them into a file.
    comb = CombinatorialExplosion()
    combinations = comb.find_matching_odds(content)

    print("Total combinations: ", len(combinations))
    if len(combinations) > 0:
        no_of_buckets = len(combinations[0])
        wagers = get_odd_values(min_wager, max_wager, no_of_buckets)
        output = analyze(combinations, wagers, no_of_buckets, max_wager)
        # print(len(output))
        # sorted_deals = sorted(output, key=lambda deal: sum(deal.roi_array) / len(deal.roi_array), reverse=True)
        sorted_deals = sorted(output, key=lambda deal: min(deal.roi_array), reverse=True)
        if sorted_deals:
            for i in range(1, 10):
                print(sorted_deals[i])


if __name__ == '__main__':
    main()
