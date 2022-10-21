#!/usr/bin/python3
from sys import argv,exit
from pathlib import Path


"""! @brief Advent of Code 2021 Day 2 """


def day2(filename):
    current_line = 0

    depth = 0
    position = 0

    try:
        file = Path(filename)
        fd = file.open('r')

        for line in fd.readlines():
            current_line = current_line + 1

            line = line.strip()
            if(line) == '': # Line is empty
                continue
    

            [command, distance] = line.split(' ')
            distance = int(distance)

            if command == "forward":
                position = position + distance
                continue

            if command == "down":
                depth = depth + distance
                continue

            if command == "up":
                depth = depth - distance
                continue

            print("Unknown command")
            return False
            

    except FileNotFoundError:
        print("File not found")
        return False
    
    except PermissionError:
        print('Insufficient permissions for file')
        return False
    
    except ValueError:
        print('Invalid number on line:' + str(current_line))
    
    print('Forward position is ' + str(position) + ' and depth is ' + str(depth) + '.')  
    print('Multiply of position and depth is ' + str(position*depth))  
    return position * depth

def day2_part2(filename):
    current_line = 0

    depth = 0
    position = 0
    aim = 0

    try:
        file = Path(filename)
        fd = file.open('r')

        for line in fd.readlines():
            current_line = current_line + 1

            line = line.strip()
            if(line) == '': # Line is empty
                continue
    

            [command, x] = line.split(' ')
            x = int(x)

            if command == "forward":
                position = position + x
                depth = depth + aim * x
                continue

            if command == "down":
                aim = aim + x
                continue

            if command == "up":
                aim = aim - x
                continue

            print("Unknown command")
            return False
            

    except FileNotFoundError:
        print("File not found")
        return False
    
    except PermissionError:
        print('Insufficient permissions for file')
        return False
    
    except ValueError:
        print('Invalid number on line:' + str(current_line))
    
    print('Forward position is ' + str(position) + ' and depth is ' + str(depth) + '.')  
    print('Multiply of position and depth is ' + str(position*depth))  
    return position * depth
        



if argv[1] != None:
    print("[Part 1]")
    if day2(argv[1]) == False:
        exit(1)

    print("[Part 2]")
    if day2_part2(argv[1]) == False:
        exit(1)
    exit(0)


