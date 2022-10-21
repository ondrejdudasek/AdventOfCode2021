#!/usr/bin/python3

from sys import argv,exit
from pathlib import Path


def day1(filename):
    
    print("[Part 1]")
    increment_counter = 0
    previous_number = None
    current_line = 0

    try:
        file = Path(filename)
        fd = file.open('r')

        for line in fd.readlines():
            current_line = current_line + 1

            line = line.strip()
            if(line) == '': # Line is empty
                continue

            current_number = int(line)

            
            if previous_number == None:
                previous_number = current_number
                #print(current_sum, 'False')
                continue

            #print(current_sum, (current_sum > previous_sum))
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
        return False
    
    print('Number has increased ' + str(increment_counter) + ' times.')    
    return increment_counter

def day1_p2(filename):
    
    print("[Part 2]")

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
        return False
    
    print('Sum has increased ' + str(increment_counter) + ' times.')    
    return increment_counter
        



if argv[1] != None:
    if day1(argv[1]) == False:
        exit(1)

    if day1_p2(argv[1]) == False:
        exit(1)
    exit(0)


