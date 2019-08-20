import concurrent.futures
from concurrent.futures import ThreadPoolExecutor


class ROI:
    def __init__(self, wager, odd, roi_array, returns):
        self.wager = wager
        self.odd = odd
        self.roi_array = roi_array
        self.returns = returns

    def __str__(self):
        return "wager: {0}, \n" \
               "odd: {1}\n" \
               "returns: {2},\n" \
               "roi_array: {3}".format(
            self.wager, self.odd, self.returns, self.roi_array
        )

    def __repr__(self):
        return self.__str__()


def majority_positive(arr, total):
    neg_count = len(list(filter(lambda x: (x < 0), arr)))

    if neg_count == 0 or neg_count < total / 2:
        return True
    else:
        return False


def analyze(odds, wagers, no_of_buckets, total_wager):
    output = []
    print("Wagers: ", len(wagers))
    print("Odds: ", len(odds))
    step_size = 50
    with ThreadPoolExecutor() as executor:
        future_to_num = {
            executor.submit(zip_wagers_to_odds, odds, wagers, no_of_buckets, total_wager, j, j + step_size): j for j in
            range(0, len(wagers), step_size)}
        print("Number of Jobs submitted: ", len(future_to_num))
        count = 0
        for future in concurrent.futures.as_completed(future_to_num):
            num = future_to_num[future]
            try:
                result = future.result()
                count = count + 1
                if len(result) > 0:
                    sorted_result = sorted(result, key=lambda deal: min(deal.roi_array), reverse=True)[:10]
                    output += sorted_result
                    print("Output Received: ", count, len(sorted_result))
                else:
                    print(".")
            except Exception as exc:
                print('%r generated an exception: %s' % (num, exc))
            # else:
            # print('%r page is %d ' % (num, len(result)))
            # print(result)
    return output


def zip_wagers_to_odds(odds, wagers, no_of_buckets, total_wager, a, b):
    output = []
    for i in range(a, b):
        if i < len(wagers):
            wager = wagers[i]
            for odd in odds:
                prod = []
                returns = []
                for j in range(0, len(odd)):
                    return_value = float(wager[j] * float(odd[j].f_odd))
                    returns += [return_value]
                    prod += [((return_value - total_wager) / total_wager) * 100]

                if majority_positive(prod, no_of_buckets):
                    # print ((wager, prod)#)
                    output += [ROI(wager, odd, prod, returns)]
    return output


def get_odd_values(min_wager, max_wager, no_of_buckets):
    if no_of_buckets >= 2:
        return generate_wagers(min_wager, max_wager, no_of_buckets, [])
    else:
        return []


def generate_wagers(min_wager, max_wager, no_of_buckets, current):
    output = []
    for i in range(1, max_wager):
        if no_of_buckets == 1:
            current_sum = sum(current) + i
            if current_sum >= min_wager and current_sum == max_wager:
                output.append(current + [i])
        else:
            output += generate_wagers(min_wager, max_wager, no_of_buckets - 1, current + [i])

    return output


def some_action(num, a):
    output = []
    print(num, a)
    for j in range(0, num):
        output += [num * 2]
    return output


def check_parallel():
    output = []
    with ThreadPoolExecutor() as executor:
        future_to_num = {executor.submit(some_action, j, j + 4): j for j in range(1, 50, 5)}
        for future in concurrent.futures.as_completed(future_to_num):
            num = future_to_num[future]
            try:
                result = future.result()
                output += result
            except Exception as exc:
                print('%r generated an exception: %s' % (num, exc))
            else:
                print('%r page is %d ' % (num, len(result)))
                print(result)
    print(output)


def main():
    # print(get_odd_values(100, 3))
    check_parallel()


if __name__ == '__main__':
    main()
