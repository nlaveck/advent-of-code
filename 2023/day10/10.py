import sys

visited = set()

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
    #print(neighbors)
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
        if nodes[0] == nodes[1] or nodes[0] == toVisit[1] or nodes[1] == toVisit[0]:
            print(steps)
            break
        last = toVisit
        toVisit = nodes
        steps += 1        

with open(sys.argv[1], "r") as inFile:
    input = [line.strip() for line in inFile.readlines()]
    start = None
    
    for i, line in enumerate(input):
        for j, c in enumerate(line):
            if c == 'S':
                start = (i, j)
    
    solve()