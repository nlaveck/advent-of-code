import sys

class Direction:
    LEFT = (0,-1)
    RIGHT = (0,1)
    UP = (-1,0)
    DOWN = (1,0)

class Node:
    def __init__(self, position: tuple[int, int], direction: tuple[int, int]):
        self.position = position
        self.direction = direction

    def move(self):
        newPos = (self.position[0] + self.direction[0], self.position[1] + self.direction[1])
        #print(newPos)
        if self.__in_bounds(newPos):
            #print('hit')
            return Node(newPos, self.direction)
        else:
            return None
    
    def heading(self, dir):
        return Node(self.position, dir)
    
    def reflect(self):
        cell = grid[self.position[0]][self.position[1]]
        if cell == '.' \
                or (self.direction in {Direction.UP,Direction.DOWN} and cell == '|') \
                or (self.direction in {Direction.LEFT, Direction.RIGHT} and cell == '-'):
            return [self]
        if cell == '|':
            return [self.heading(Direction.UP), self.heading(Direction.DOWN)]
        if cell == '-':
            return [self.heading(Direction.LEFT), self.heading(Direction.RIGHT)]
        if cell == '/':
            if self.direction == Direction.LEFT:
                return [self.heading(Direction.DOWN)]
            if self.direction == Direction.RIGHT:
                return [self.heading(Direction.UP)]
            if self.direction == Direction.UP:
                return [self.heading(Direction.RIGHT)]
            if self.direction == Direction.DOWN:
                return [self.heading(Direction.LEFT)]
        if cell == '\\':
            if self.direction == Direction.LEFT:
                return [self.heading(Direction.UP)]
            if self.direction == Direction.RIGHT:
                return [self.heading(Direction.DOWN)]
            if self.direction == Direction.UP:
                return [self.heading(Direction.LEFT)]
            if self.direction == Direction.DOWN:
                return [self.heading(Direction.RIGHT)]


    def visit(self):
        d = self.to_dict()
        if d in visited:
            return []
        visited.add(d)

        # move
        newPos = self.move()
        if not newPos:
            return []
        
        # hit mirrors
        return newPos.reflect()
 
        
    def to_dict(self):
        return (self.position, self.direction)
        
    def __in_bounds(self, pos: tuple[int,int]):
        return 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0])


def solve(start: Node):
    toVisit = start.reflect()
    while toVisit:
        newNodes = toVisit.pop().visit()
        toVisit += newNodes

def print_grids(positions):
    for g in grid:
        print(g)
    print('\n**********************************************************\n')
    cell_grid = [[c for c in row] for row in grid]
    #print(cell_grid)
    for p in positions:
        if grid[p[0]][p[1]] == '.':
            cell_grid[p[0]][p[1]] = '#'
    
    for row in cell_grid:
        for cell in row:
            print(cell, end='')
        print()



with open(sys.argv[1], 'r') as in_file:
    grid = [line.strip() for line in in_file.readlines()]
    #print(grid)

    max_score = 0

    for i in range(len(grid)):
        visited = set()
        start = Node((i,0), Direction.RIGHT)
        solve(start)
        positions = {v[0] for v in visited}
        max_score = max(len(positions), max_score)

    for i in range(len(grid)):
        visited = set()
        start = Node((i,len(grid[0])-1), Direction.LEFT)
        solve(start)
        positions = {v[0] for v in visited}
        max_score = max(len(positions), max_score)

    for i in range(len(grid[0])):
        visited = set()
        start = Node((0,i), Direction.DOWN)
        solve(start)
        positions = {v[0] for v in visited}
        max_score = max(len(positions), max_score)

    for i in range(len(grid[0])):
        visited = set()
        start = Node((len(grid)-1,i), Direction.UP)
        solve(start)
        positions = {v[0] for v in visited}
        max_score = max(len(positions), max_score)
    print(max_score)

