import datetime
import glob
import os
import pickle
import time
from odds_analyzer import *


class CombinatorialExplosion:
    def __init__(self, path='/tmp', file_record_limit=10000):
        self.__total = 0
        self.__file_counter = 0
        self.__file_prefix = path + "/output_odds_"
        self.__file_record_limit = file_record_limit
        self.__data = []

    def __append_to_file(self):
        file_name = self.__file_prefix + str(self.__file_counter)
        file_handler = open(file_name, 'wb')
        pickle.dump(self.__data, file_handler)
        self.__reset_counters()

    def __reset_counters(self):
        self.__file_counter = self.__file_counter + 1
        self.__data = []

    def __find_combinations_internal(self, counter, index, data, index_bit):
        i = 0

        if counter >= len(index):
            # print(index)
            s = []
            for i in range(len(index)):
                s.append(data[i].odds[index[i]])
            # print(s)
            self.__data.append(s)
            self.__total = self.__total + 1
            if self.__total % self.__file_record_limit == 0:
                st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
                print(st + " : " + str(self.__total))
                self.__append_to_file()
            return

        while i < len(data[counter].odds):
            x = ((index_bit & (1 << i)) >> i)  # Is the bit at position i set
            if x == 0 and data[counter].odds[i].f_odd != '0.0':
                index[counter] = i
                self.__find_combinations_internal(counter + 1, index, data, index_bit | (1 << i))
            i = i + 1

    def __clear_directory(self):
        pattern = self.__file_prefix + "*"
        # print ("Looking for files to delete with pattern: ", pattern)
        fileList = glob.glob(pattern)
        # print("Found files to delete: ", fileList)
        for filePath in fileList:
            try:
                # print("Removing file ", filePath)
                os.remove(filePath)
            except Exception as e:
                print("Error while deleting file : ", filePath, str(e))

    def find_matching_odds(self, data):
        self.__clear_directory()
        # print("Start Time: ", datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
        index = [0] * len(data.events)  # Initialized index array
        index_bit = 0
        self.__find_combinations_internal(0, index, data.events, index_bit)
        # print("End Time: ", datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
        # self.__find_potential_deals()
        # self.__determine_odds()
        return self.__data

    def __determine_odds(self):
        for i in range(self.__file_counter):
            file_name = self.__file_prefix + str(i)
            print("Reading file name", file_name)
            file = open(file_name, 'rb')
            events = pickle.load(file)
            print(events)
            print("Number of events", len(events))

    def __find_potential_deals(self):
        for event in self.__data:
            print("Analyzing data: ", event)
            analyze(event)


def main():
    i = 1 | (1 << 0)
    print("Mark position 1", i)
    i = i | (1 << 2)
    print("Mark position 3", i)
    x = ((i & (1 << 2)) >> 2)
    print("Is position 3 set", x)
    x = ((i & (1 << 1)) >> 1)
    print("Is position 2 set", x)
    pass


if __name__ == '__main__':
    main()
