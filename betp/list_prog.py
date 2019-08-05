def comb(data):
    index = [0] * len(data)
    do_work(0, index, data)


def do_work(counter, index, data):
    i = 0

    if counter >= len(index):
        #print(index)
        s = []
        for i in range(len(index)):
            s.append(data[i][index[i]])
        print(s)
        return

    while i < len(index) and i < len(data[counter]):
        index[counter] = i
        do_work(counter + 1, index, data)
        i = i + 1


def main():
    l = [[1, 2, 3], [4, 6], [7, 8, 9], [10, 11], [12]]
    comb(l)


if __name__ == '__main__':
    main()
