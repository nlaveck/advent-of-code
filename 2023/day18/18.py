import sys

class Solution:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.data = []
        self.trench = set()
        
        self.min_x = sys.maxsize
        self.min_y = sys.maxsize
        self.max_x = -sys.maxsize - 1
        self.max_y = -sys.maxsize - 1
        
    def __get_input(self):
        with open(self.filename) as in_file:
          return [line.rstrip() for line in in_file.readlines()]
      
    def __parse(self, input: [str]):
        for line in input:
            self.data.append(line.split())
    
    def move(self, cursor, direction):
        vector = None
        if direction == 'D':
            vector = (1,0)
        elif direction == 'U':
            vector = (-1,0)
        elif direction == 'L':
            vector = (0,-1)
        else: #direction == 'R'
            vector = (0,1)
        return (cursor[0] + vector[0], cursor[1] + vector[1])
    
    def dig(self):
        
        cursor = (0,0)
        self.trench.add(cursor)
        
        for line in self.data:
            direction = line[0]
            distance = int(line[1])
            
            for _ in range(distance):
                cursor = self.move(cursor, direction)
                self.trench.add(cursor)
    
    def get_bounds(self):
        for y,x in self.trench:
            self.max_y = max(self.max_y, y)
            self.max_x = max(self.max_x, x)
            self.min_y = min(self.min_y, y)
            self.min_x = min(self.min_x, x)
    
    def get_area(self):
        
        def in_bounds(node):
            return self.min_y <= node[0] <= self.max_y and self.min_x <= node[1] <= self.max_x
            
            
        toVisit = set()
        
        #get edges nodes
        for x in range(self.min_x, self.max_x+1):
            toVisit.add((self.min_y, x))
            toVisit.add((self.max_y, x))
        for y in range(self.min_y, self.max_y+1):
            toVisit.add((y, self.min_x))
            toVisit.add((y, self.max_x))
        
        outside_nodes = 0
        rect_area = (self.max_x + 1 - self.min_x) * (self.max_y + 1 - self.min_y)
        
        visited = set()
        while toVisit:
            node = toVisit.pop()
            if node not in self.trench:
                outside_nodes += 1
                visited.add(node)
                siblings = [self.move(node, direction) for direction in 'UDLR']
                for s in siblings:
                    if in_bounds(s) and s not in visited and s not in self.trench:
                        toVisit.add(s)
        
        debug = False
        if debug:
            for y in range(self.min_y, self.max_y+1):
                for x in range(self.min_x, self.max_x+1):
                    if (y,x) in visited:
                        print('.', end='')
                    elif (y,x) in self.trench:
                        print('#', end='')
                    else:
                        print(' ', end='')
                print()   
        return rect_area - len(visited)
                
            
        
                
    def solve(self):
        self.dig()
        #print(self.trench)
        self.get_bounds()
        #print((self.min_x, self.min_y), (self.max_x, self.max_y))
        print(self.get_area())
        
    def run(self):
        input = self.__get_input()
        self.__parse(input)
        #print(self.data)
        self.solve()
        
Solution(sys.argv[1]).run()