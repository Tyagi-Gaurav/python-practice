import concurrent.futures
from concurrent.futures import ThreadPoolExecutor
import multiprocessing


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


def is_eligible(arr, total, risk):
    for i in range(0, total):
        if arr[i] + risk[i] < 0:
            return False

    return True


def analyze(odds, wagers, no_of_buckets, total_wager, topx=10, risk=[]):
    output = []
    # print("Wagers: ", len(wagers))
    # print("Odds: ", len(odds))
    thread_group_size = multiprocessing.cpu_count()
    step_size = len(wagers) // thread_group_size

    if no_of_buckets != len(risk):
        raise Exception(
            "Length of risk indicators: %d should be same as no_of_buckets: %d" % (len(risk), no_of_buckets))

    with ThreadPoolExecutor() as executor:
        future_to_num = {
            executor.submit(zip_wagers_to_odds, odds, wagers, no_of_buckets, total_wager, j, j + step_size, risk): j for
            j in
            range(0, len(wagers), step_size)}
        #        print("Number of Jobs submitted: ", len(future_to_num))
        count = 0
        for future in concurrent.futures.as_completed(future_to_num):
            num = future_to_num[future]
            try:
                result = future.result()
                count = count + 1
                if len(result) > 0:
                    sorted_result = sorted(result, key=lambda deal: min(deal.roi_array), reverse=True)[:topx]
                    output += sorted_result
                    # print("Output Received: ", count, len(sorted_result))
                    # print("#", end="")
                # else:
                #     print(".", end="")
            except Exception as exc:
                print('%r generated an exception: %s' % (num, exc))
    print("")
    return output


def zip_wagers_to_odds(odds, wagers, no_of_buckets, total_wager, a, b, risk=[]):
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
                    roi_in_percentage = ((return_value - total_wager) / total_wager) * 100
                    prod += [roi_in_percentage]

                if is_eligible(prod, no_of_buckets, risk):
                    # print ((wager, prod)#)
                    output += [ROI(wager, odd, prod, returns)]
    return output


def get_wagers(min_wager, max_wager, no_of_buckets):
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
