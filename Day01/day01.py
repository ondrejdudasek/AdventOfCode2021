#!/usr/bin/python3

from sys import argv,exit
from pathlib import Path

"""! @brief Advent of Code 2021 Day 1 """


def day1(filename):
    
    samples = []
    increment_counter = 0
    previous_sum = None
    current_line = 0

    try:
        file = Path(filename)
        fd = file.open('r')

        for line in fd.readlines():
            current_line = current_line + 1

            line = line.strip()
            if(line) == '': # Line is empty
                continue

            samples.append(int(line))
            if len(samples) < 3: # not enough samples
                continue

            current_sum = sum(samples)
            #print(samples, end=' ')
            samples.pop(0) # Remove first

            
            if previous_sum == None:
                previous_sum = current_sum
                #print(current_sum, 'False')
                continue

            #print(current_sum, (current_sum > previous_sum))
            if previous_sum < current_sum:
                increment_counter = increment_counter + 1
            
            previous_sum = current_sum

            

    except FileNotFoundError:
        print("File not found")
        return False
    
    except PermissionError:
        print('Insufficient permissions for file')
        return False
    
    except ValueError:
        print('Invalid number on line:' + str(current_line))
    
    print('Sum has increased ' + str(increment_counter) + ' times.')    
    return increment_counter
        



if argv[1] != None:
    if not day1(argv[1]) == False:
        exit(0)
    exit(1)


