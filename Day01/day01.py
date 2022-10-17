#!/usr/bin/python3

from sys import argv,exit
from pathlib import Path

"""! @brief Advent of Code 2021 Day 1 """


def day1(filename):
    
    previous_number = None
    increment_counter = 0
    current_line = 1

    try:
        file = Path(filename)
        fd = file.open('r')
        line = fd.readline()
        previous_number = int(line)

        for line in fd.readlines():
            current_line = current_line + 1
            line = line.strip()
            if(line) == '':
                continue
            current_number = int(line)
            if previous_number < current_number:
                increment_counter = increment_counter + 1
            previous_number = current_number

    except FileNotFoundError:
        print("File not found")
        return False
    
    except PermissionError:
        print('Insufficient permissions for file')
        return False
    
    except ValueError:
        print('Invalid number on line:' + str(current_line))
    
    print('Number has increased ' + str(increment_counter) + ' times.')    
    return increment_counter
        







if argv[1] != None:
    if not day1(argv[1]) == False:
        exit(0)
    exit(1)


