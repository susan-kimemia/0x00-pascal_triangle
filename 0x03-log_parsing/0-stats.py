#!/usr/bin/python3
'''Log parsing mandatory
'''
import sys


def print_message(dict_sc, total_file_size):
    """
    Log parsing:
    script that reads stdin line by line and computes metrics
    """

    print("File size: {}".format(total_file_size))
    for key, val in sorted(dict_status.items()):
        if val != 0:
            print("{}: {}".format(key, val))


total_file_size = 0
code = 0
counter = 0
dict_status = {"200": 0,
               "301": 0,
               "400": 0,
               "401": 0,
               "403": 0,
               "404": 0,
               "405": 0,
               "500": 0}

try:
    for line in sys.stdin:
        parsed_line = line.split()  # ✄ trimming
        parsed_line = parsed_line[::-1]  # inverting

        if len(parsed_line) > 2:
            counter += 1

            if counter <= 10:
                total_file_size += int(parsed_line[0])  # file size
                code = parsed_line[1]  # status code

                if (code in dict_status.keys()):
                    dict_status[code] += 1

            if (counter == 10):
                print_message(dict_status, total_file_size)
                counter = 0

finally:
    print_message(dict_status, total_file_size)
