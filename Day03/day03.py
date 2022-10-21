#!/usr/bin/python3
from sys import argv,exit
from pathlib import Path


def day3(filename):
    
    current_line = 0
    processed_lines = 0
    processed_ones = []

    gamma = 0
    epsilon = 0


    try:
        file = Path(filename)
        fd = file.open('r')

        line = fd.readline()
        line = line.strip()
        bits = len(line)
        for i in range(0,bits):
            processed_ones.append(0)
        
        fd.seek(0)


        for line in fd.readlines():
            current_line = current_line + 1

            line = line.strip()
            if(line) == '': # Line is empty
                continue

            

            # conversion to int will cause ValueError for invalid data
            if len(line) != bits or int(line, 2) < 0: 
                print("Invalid data")
                return False

            processed_lines = processed_lines + 1
            
            # cycle through positions
            for position in range(0,bits):
                if line[position] == '1':
                    processed_ones[position] += 1

        # Find most used
        for position in range(0,bits):
            if processed_ones[position] > processed_lines // 2:
                gamma += 2**(bits - 1 - position)
            else:
                epsilon += 2**(bits - 1 - position)
        print("Gamma is " + str(gamma) + ", epsilon is " + str(epsilon))
        print("Power consumption is " + str(gamma*epsilon)) 

    except FileNotFoundError:
        print("File not found")
        return False
    
    except PermissionError:
        print('Insufficient permissions for file')
        return False
    
    except ValueError:
        print('Invalid number on line:' + str(current_line))
    


def line_filter(lines: list, position: int, value: str) -> list:
    """Filter out lines not containing value on position
    """
    lines_to_remove = list()
    for line in lines:
        if line[position] != value:
            lines_to_remove.append(line)

    for line in lines_to_remove:
        lines.remove(line)
    return lines

def get_most_common(lines: list, position: int) -> str:
    """Get most common value at the specified position of each line

    Simplified for values 0 or 1.
    """
    ones = 0
    for line in lines:
        if line[position] == '1':
            ones += 1
    
    if ones >= (len(lines)-ones):
        return '1'
    
    return '0'

def get_least_common(lines:list, position: int) -> str:
    """Alias for get_most_common with inverted outputs
    """
    if get_most_common(lines, position) == '1':
        return '0'
    else:
        return '1'



def day3_part2(filename):
    
    current_line = 0
    report = list()

    gamma = 0
    epsilon = 0


    try:
        file = Path(filename)
        fd = file.open('r')

        for line in fd.readlines():
            current_line = current_line + 1

            line = line.strip()
            if(line) == '': # Line is empty
                continue

            report.append(line)
        
        # Oxygen generator report
        oxygen_report = report.copy()
        i = 0
        while i < len(oxygen_report[0]) and len(oxygen_report) > 1:
            most_common = get_most_common(oxygen_report, i)
            #print(most_common, oxygen_report)
            oxygen_report = line_filter(oxygen_report, i, most_common)
            i += 1
        
        if len(oxygen_report) > 1:
            print("Too many results")
            return False

        oxygen_report = oxygen_report[0]            
        #print(oxygen_report, int(oxygen_report,base=2))

        # Co2 scrubber report
        co2_report = report.copy()
        #print(co2_report)

        i = 0
        while i < len(co2_report[0]) and len(co2_report) > 1:
            least_common = get_least_common(co2_report, i)
            #print(least_common, co2_report)
            co2_report = line_filter(co2_report, i, least_common)
            i += 1
        
        if len(co2_report) > 1:
            print("Too many results")
            return False

        co2_report = co2_report[0]            
        #print(co2_report, int(co2_report,base=2))
        print(int(co2_report, 2)*int(oxygen_report, 2))
            

            
    
    except FileNotFoundError:
        print("File not found")
        return False
    
    except PermissionError:
        print('Insufficient permissions for file')
        return False
    
    except ValueError:
        print('Invalid number on line:' + str(current_line))

                

                    






if argv[1] != None:
    print("[Part 1]")
    if not day3(argv[1]) == False:
        exit(1)

    print("[Part 2]")
    if not day3_part2(argv[1]) == False:
        exit(1)
    exit(0)


