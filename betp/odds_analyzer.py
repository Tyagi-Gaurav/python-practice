class ROI:
    def __init__(self, wager, odd, roi_array):
        self.wager = wager
        self.__roi_value = 0.0
        self.odd = odd
        self.roi_array = roi_array

    def __str__(self):
        return "wager: {0}, " \
               "roi_array: {1}," \
               "odd: {2}".format(
            self.wager, self.roi_array, self.odd
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
    for wager in wagers:
        for odd in odds:
            prod = []
            for j in range(0, len(odd)):
                return_value = float(wager[j] * float(odd[j].f_odd))
                prod += [((return_value - total_wager)/total_wager) * 100]

            if majority_positive(prod, no_of_buckets):
                # print ((wager, prod)#)
                output += [ROI(wager, odd, prod)]
    return output


def get_odd_values(num, no_of_buckets):
    if no_of_buckets >= 2:
        return generate_wagers(num, no_of_buckets, [])
    else:
        return []


def generate_wagers(num, no_of_buckets, current):
    output = []
    for i in range(1, num):
        if no_of_buckets == 1:
            if sum(current) + i == num:
                output.append(current + [i])
        else:
            output += generate_wagers(num, no_of_buckets - 1, current + [i])

    return output


def main():
    print(get_odd_values(100, 3))


if __name__ == '__main__':
    main()
