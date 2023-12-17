import sys
from time import sleep

visited = set()

class Direction:
    LEFT = (0,-1)
    RIGHT = (0,1)
    UP = (-1,0)
    DOWN = (1,0)
    
    def opposite(direction):
        if direction == Direction.LEFT:
            return Direction.RIGHT
        if direction == Direction.RIGHT:
            return Direction.LEFT
        if direction == Direction.UP:
            return Direction.DOWN
        if direction == Direction.DOWN:
            return Direction.UP
    
    def rotate(direction, clockwise):
        if direction == Direction.UP:
            return Direction.RIGHT if clockwise else Direction.LEFT 
        if direction == Direction.RIGHT:
            return Direction.DOWN if clockwise else Direction.UP
        if direction == Direction.DOWN:
            return Direction.LEFT if clockwise else Direction.RIGHT
        if direction == Direction.LEFT:
            return Direction.UP if clockwise else Direction.DOWN

def is_clockwise(heading, pipe):
    if pipe == 'F':
        return True if heading == Direction.UP else False
    if pipe == '7':
        return True if heading == Direction.RIGHT else False
    if pipe == 'J':
        return True if heading == Direction.DOWN else False
    if pipe == 'L':
        return True if heading == Direction.LEFT else False
         
    
def pipe_directions(pipe):
    if pipe == '|':
        return [Direction.UP, Direction.DOWN]
    if pipe == '-':
        return [Direction.LEFT, Direction.RIGHT]
    if pipe == 'L':
        return [Direction.UP, Direction.RIGHT]
    if pipe == 'J':
        return [Direction.UP, Direction.LEFT]
    if pipe == '7':
        return [Direction.LEFT, Direction.DOWN]
    if pipe == 'F':
        return [Direction.RIGHT, Direction.DOWN]
    
def move(position, direction):
    return (position[0] + direction[0], position[1] + direction[1])
    
def in_bounds(c: tuple):
    return 0 <= c[0] < len(input) and 0 <= c[1] < len(input[0])

def get_connecting_pipes(c: tuple):
    if not in_bounds(c):
        raise Exception('out of bounds!', c)
    neighbors = set()
    pipe = input[c[0]][c[1]]
    if pipe == '|':
        neighbors = {(c[0]+1,c[1]),(c[0]-1,c[1])}
    elif pipe == '-':
        neighbors = {(c[0],c[1]+1),(c[0],c[1]-1)}
    elif pipe == 'L':
        neighbors = {(c[0]-1,c[1]),(c[0],c[1]+1)}
    elif pipe == 'J':
        neighbors = {(c[0]-1,c[1]),(c[0],c[1]-1)}
    elif pipe == '7':
        neighbors = {(c[0]+1,c[1]),(c[0],c[1]-1)}
    elif pipe == 'F':
        neighbors = {(c[0]+1,c[1]),(c[0],c[1]+1)}
    return {n for n in neighbors if in_bounds(c)}
    
def solve():
    global visited
    visited.add(start)
    
    left = (start[0], start[1]-1)
    right = (start[0], start[1]+1)
    up = (start[0]+1, start[1])
    down = (start[0]-1, start[1])
    
    toVisit = [dir for dir in [left, right, up, down] if in_bounds(dir) and start in get_connecting_pipes(dir)]
    last = [start, start]
    steps = 2
    
    
    while True:
        nodes = [(get_connecting_pipes(toVisit[i]) - {last[i]}).pop() for i in range(2)]
        visited |= set(toVisit) | set(nodes)
        if nodes[0] == nodes[1] or nodes[0] == toVisit[1] or nodes[1] == toVisit[0]:
            #print(steps)
            break
        last = toVisit
        toVisit = nodes
        steps += 1        

def print_pipes():
    for i in range(len(input)):
        for j in range(len(input[0])):
            if (i,j) in area:
                print('I', end='')
            elif (i,j) in outside_area:
                print('O', end='')
            elif (i,j) in visited:
                print(input[i][j], end='')
            else:
                print(' ', end='')
                
        print()
        
def top_left_loop_corner():
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == 'F' and (i,j) in visited:
                return (i,j)

def get_score(pos, dir):
    inside = move(pos, dir)
    ouside = move(pos, Direction.opposite(dir))
    
    score = 0
    toVisit=[inside]
    while toVisit:
        current = toVisit.pop()
        if current in visited or current in area or not in_bounds(current):
            continue
        else:
            area.add(current)
            toVisit += [move(current, d) for d in [Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT]]
            score += 1
    
    toVisit=[ouside]
    while toVisit:
        current = toVisit.pop()
        if current in visited or current in outside_area or not in_bounds(current):
            continue
        else:
            outside_area.add(current)
            toVisit += [move(current, d) for d in [Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT]]
    return score
            
        


with open(sys.argv[1], "r") as inFile:
    input = [line.strip() for line in inFile.readlines()]
    start = None
    
    for i, line in enumerate(input):
        for j, c in enumerate(line):
            if c == 'S':
                start = (i, j)
     
    solve()
    

    start = cursor = top_left_loop_corner()
    heading = Direction.RIGHT
    inside = Direction.DOWN
    area = set()
    outside_area = set()
    score = 0
    visited2 = set([start])
    
    while (cursor := move(cursor, heading)) != start:
        pipe = input[cursor[0]][cursor[1]]
        #print(cursor)
        if pipe == 'S': pipe = '-'  # Trick to fix pipe manually
        if pipe in {'7', 'J', 'L', 'F'}:
            clockwise = is_clockwise(heading, pipe)
            heading = Direction.rotate(heading, clockwise)
            
            # corners need to be calculated twice since they can have more than 1 inside edge
            score += get_score(cursor, inside)
            inside = Direction.rotate(inside, clockwise)
        visited2.add(cursor)
        score += get_score(cursor, inside)
        
    print(score)
    #print_pipes()
    
    

                

