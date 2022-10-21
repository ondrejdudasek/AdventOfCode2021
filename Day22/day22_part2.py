
from code import interact
from pathlib import Path
from numpy import array, full, bool_
from sys import argv, exit



class Block:
    x = [0, 0]
    y = [0, 0]
    z = [0, 0]

    def __init__(self, x:list, y:list, z:list) -> None:
        #print(x,y,z)
        if x[0] > x[1]:
            x = x[1],x[0]
        if y[0] > y[1]:
            y = y[1],y[0]
        if z[0] > z[1]:
            z = z[1],z[0]
        self.x = x
        self.y = y
        self.z = z

    def get_dimensions(self) -> list:
        return self.x, self.y, self.z

    def overlaps(self, block) -> bool:
        """Return True if blocks overlap"""
        if self.x[0] > block.x[1] or self.x[1] < block.x[0]:
            return False
        
        if self.y[0] > block.y[1] or self.y[1] < block.y[0]:
            return False
        
        if self.z[0] > block.z[1] or self.z[1] < block.z[0]:
            return False
        
        # All dimensions overlap, so the blocks overlap
        return True

    def difference(self, block) -> list:
        """ Remove block area from self. 

        If block intersects with this, return smaller blocks.
        If blocks do not intersect, return self.
        @return [intersection, list of cubes]
        """
        if not self.overlaps(block):
            return [False, [self]]

        # Blocks which will no further be modified
        replacement_blocks = []
        # Block to be splitted further
        intersecting_block = None

        # Axis X
        if self.x[0] < block.x[0]:
            if self.x[1] > block.x[1]:
                # block lies within self's x range
                replacement_blocks.append(
                    Block(
                        [self.x[0], block.x[0]-1], 
                        self.y, 
                        self.z),
                )
                replacement_blocks.append(
                    Block(
                        [block.x[1]+1, self.x[1]], 
                        self.y, 
                        self.z)
                )
                intersecting_block = Block(
                    [block.x[0], block.x[1]], 
                    self.y, 
                    self.z)
            else:
                # block occupies part of the self's x range to its edge
                replacement_blocks.append(
                    Block(
                        [self.x[0], block.x[0]-1], 
                        self.y, 
                        self.z)
                )
                intersecting_block = Block(
                    [block.x[0],self.x[1]], 
                    self.y, 
                    self.z)
        else:
            if self.x[1] > block.x[1]:
                # block occupies part of the self's x range its to edge
                replacement_blocks.append(Block(
                    [block.x[1]+1,self.x[1]], 
                    self.y, 
                    self.z)
                )
                intersecting_block = Block(
                    [self.x[0], block.x[1]], 
                    self.y,
                    self.z)
            else:
                # block overlaps self's x range
                intersecting_block = self
        
        # Y axis
        if intersecting_block.y[0] < block.y[0]:
            if intersecting_block.y[1] > block.y[1]:
                # block lies within self's y range
                replacement_blocks.append(Block(
                    intersecting_block.x,
                    [intersecting_block.y[0], block.y[0] - 1], 
                    intersecting_block.z),
                )
                replacement_blocks.append(Block(
                    intersecting_block.x, 
                    [block.y[1] + 1, intersecting_block.y[1]], 
                    intersecting_block.z)
                )
                intersecting_block = Block(
                    intersecting_block.x,
                    [block.y[0], block.y[1]],
                    intersecting_block.z)
            else:
                # block occupies part of the self's y range to its edge
                replacement_blocks.append(Block(
                    intersecting_block.x, 
                    [intersecting_block.y[0], block.y[0] - 1], 
                    intersecting_block.z)
                )
                intersecting_block = Block(
                    intersecting_block.x, 
                    [block.y[0], intersecting_block.y[1]], 
                    intersecting_block.z)
        else:
            if intersecting_block.y[1] > block.y[1]:
                # block occupies part of the self's y range its to edge
                replacement_blocks.append(Block(
                        intersecting_block.x,
                        [block.y[1] + 1, intersecting_block.y[1]],
                        intersecting_block.z)
                )
                intersecting_block = Block(
                    intersecting_block.x, 
                    [intersecting_block.y[0], block.y[1]], 
                    intersecting_block.z)
            else:
                # block overlaps self's y range
                # intersecting block remains unchanged
                pass

        # Z axis
        if intersecting_block.z[0] < block.z[0]:
            if intersecting_block.z[1] > block.z[1]:
                # block lies within self's z range
                replacement_blocks.append(Block(
                    intersecting_block.x,
                    intersecting_block.y, 
                    [intersecting_block.z[0], block.z[0] - 1]),
                )
                replacement_blocks.append(Block(
                    intersecting_block.x, 
                    intersecting_block.y, 
                    [block.z[1] + 1, intersecting_block.z[1]])
                )
            else:
                # block occupies part of the self's z range to its edge
                replacement_blocks.append(Block(
                    intersecting_block.x, 
                    intersecting_block.y, 
                    [intersecting_block.z[0], block.z[0] - 1])
                )
        else:
            if intersecting_block.z[1] > block.z[1]:
                # block occupies part of the self's z range its to edge
                replacement_blocks.append(Block(
                        intersecting_block.x,
                        intersecting_block.y,
                        [block.z[1] + 1, intersecting_block.z[1]])
                )
            else:
                # block overlaps self's z range
                # intersecting block remains unchanged
                pass
        return True, replacement_blocks


                



    
    def sum(self) -> int:
        """Return block volume"""
        x_size = self.x[1] - self.x[0] + 1
        y_size = self.y[1] - self.y[0] + 1
        z_size = self.z[1] - self.z[0] + 1

        return x_size * y_size * z_size
    
    def __str__(self) -> str:
        return (
            "[" + 
            str(self.x[0]) + ".." +
            str(self.x[1]) + ", " +
            str(self.y[0]) + ".." +
            str(self.y[1]) + ", " +
            str(self.z[0]) + ".." +
            str(self.z[1]) + "]")
 

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
    
class Reactor(list):
    def remove_block(self, block: Block):
        for existing_block in self:
            overlapping, blocks = existing_block.difference(block)
            if overlapping:
                sum = existing_block.sum()
                self.remove(existing_block)
                for new_block in blocks:
                    sum = sum - new_block.sum()
                    print("New partial block: %s"%new_block)
                    self.append(new_block)
                print("Removed %d blocks"%sum)

    def add_block(self, block: Block):
        new_blocks = [block]
        sum = 0
        for existing_block in self:
            for new_block in new_blocks:
                overlaps, fractial_blocks = new_block.difference(existing_block)
                if overlaps:
                    for new_fractial_block in fractial_blocks:
                        #print(new_fractial_block)
                        new_blocks.append(new_fractial_block)
                    
                    new_blocks.remove(new_block)
        for new_block in new_blocks:
            sum += new_block.sum()
            self.append(new_block)
        
        #print("Added %d blocks"%sum)

        #self.remove_block(block)
        #self.append(block)
    
    def sum(self):
        sum = 0
        for block in self:
            #print(block)
            sum = sum + block.sum()

        return sum

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

def day22_part2(filename):
    """ My solution of Day 22, second part.

    The reactor is simplified as a list of turned on blocks. 
    """
    xlim = [-50, 50]
    ylim = [-50, 50]
    zlim = [-50, 50]
    current_line = 0

    try:
        file = Path(filename)
        fd = file.open('r')
        
        reactor = Reactor()

        
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

            #print(line)

            if x == False or y == False or z == False:
                continue
            
            print(line)
            if command == 'on':
                reactor.add_block(Block(x,y,z))
            
            if command == 'off':
                reactor.remove_block(Block(x,y,z))
                 

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
    if not day22_part2(argv[1]) == False:
        exit(0)
    exit(1)

