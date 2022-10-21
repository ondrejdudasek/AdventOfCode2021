
from pathlib import Path
from numpy import array, full, bool_
from sys import argv, exit


def limitrange(range:list, limit: list) -> list:
    """Limit numeric range to limit, return False if both values are out of range"""
    
    # Check if range is in decreasing order and invert if needed
    if range[0] > range[1]:
        range[0],range[1] = range[1], range[0]
    
    # out of range checks
    if range[1] < limit[0]:
        return False
    
    if range[0] > limit[1]:
        return False
    
    if range[0] < limit[0]:
        range[0] = limit[0]
    
    if range[1] > limit[1]:
        range[0] = limit[0]
    
    return range

def parsecommand(line:str) -> list:
    """! Parse command with coordinate ranges
    @param line String with one line, stripped of surrounding whitespace
    @return List consisting of command, x, y and z ranges
    """
    [command, coordinates] = line.split(' ')
    [x,y,z] = coordinates.split(',')
    x = x.lstrip('x=').split('..')
    y = y.lstrip('y=').split('..')
    z = z.lstrip('z=').split('..')

    x = [int(x[0]), int(x[1])]
    y = [int(y[0]), int(y[1])]
    z = [int(z[0]), int(z[1])]

    return [command, x, y, z]
    

def set_blocks(reactor: array, ranges: list, on = True) -> list:
    """Set blocks in range on or off 
    
    Ranges have to be translated to array dimensions (starting with 0)
    """

    xrange = ranges[0]
    yrange = ranges[1]
    zrange = ranges[2]

    reactor[
        xrange[0]:xrange[1]+1,
        yrange[0]:yrange[1]+1, 
        zrange[0]:zrange[1]+1] = on


    return reactor



def day22(filename):
    
    current_line = 0

    xlim = [-50, 50]
    ylim = [-50, 50]
    zlim = [-50, 50]

    # Create reactor of size between limits
    reactor = full((
            (xlim[1] - xlim[0] + 1),
            (ylim[1] - ylim[0] + 1),
            (zlim[1] - zlim[0] + 1)),
        False, bool_)


    try:
        # Open file
        file = Path(filename)
        fd = file.open('r')

        # Parse lines
        for line in fd.readlines():
            current_line = current_line + 1

            # Parse input line and eliminate useless input
            line = line.strip()
            if(line) == '': # Line is empty
                continue
            command, x, y, z = parsecommand(line)
            x = limitrange(x, xlim)
            y = limitrange(y, ylim)
            z = limitrange(z, zlim)
            if x == False or y == False or z == False:
                continue

            # offset values to array indexes
            x = x[0] - xlim[0], x[1] - xlim[0]
            y = y[0] - ylim[0], y[1] - ylim[0]
            z = z[0] - zlim[0], z[1] - zlim[0]

            if command == 'on':
                set_blocks(reactor, [x, y, z], True)
            
            if command == 'off':
                set_blocks(reactor, [x, y, z], False)
                print(reactor[x[0]:x[1]][y[0]:y[1]][z[0]:z[1]])

            print("Reactor sum is %d"%reactor.sum())

        print(reactor.sum())

    except FileNotFoundError:
        print("File not found")
        return False
    
    except PermissionError:
        print('Insufficient permissions for file')
        return False
    
    except ValueError:
        print('Invalid number on line:' + str(current_line))

if argv[1] != None:
    if not day22(argv[1]) == False:
        exit(0)
    exit(1)

