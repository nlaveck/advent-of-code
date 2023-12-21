import sys

class Direction:
    RIGHT = '0'
    DOWN = '1'
    LEFT = '2'
    UP = '3'
    
    # RIGHT = 'R'
    # DOWN = 'D'
    # LEFT = 'L'
    # UP = 'U'
    
class Solution:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.data = []
        self.points = []
        self.circumfrence = 0
        
    def __get_input(self):
        with open(self.filename) as in_file:
          return [line.rstrip() for line in in_file.readlines()]
      
    def __parse(self, input: [str]):
        for line in input:
            self.data.append(line.split())
            
    def is_clockwise(self, last_dir, current_dir):
        #print(last_dir, current_dir)
        if (last_dir == Direction.RIGHT and current_dir == Direction.DOWN) \
        or (last_dir == Direction.DOWN and current_dir == Direction.LEFT) \
        or (last_dir == Direction.LEFT and current_dir == Direction.UP) \
        or (last_dir == Direction.UP and current_dir == Direction.RIGHT):
            return True
        return False
    
    def get_direction_vector(self, direction):
        vector = None
        if  direction == Direction.RIGHT:
            vector = (0,1)
        elif direction == Direction.DOWN:
            vector = (1,0)
        elif direction == Direction.LEFT:
            vector = (0,-1)
        else: #direction == Direction.UP:
            vector = (-1,0)
        return vector
    
    def get_next_point(self, cursor, prev_dir, dir, next_dir, distance):
        vector = self.get_direction_vector(dir)
        self.circumfrence += distance
        
        rotation = 0
        rotation += 1 if self.is_clockwise(prev_dir, dir) else -1
        rotation += 1 if self.is_clockwise(dir, next_dir) else -1
        
        distance += rotation//2
        return (cursor[0] + vector[0] * distance, 
                cursor[1] + vector[1] * distance)
    
    def get_coords(self):
        
        cursor = (0,0)
        last_direction = self.data[-1][2][-2]
        
        for i in range(len(self.data)):
            line = self.data[i]
            
            #direction = line[0]
            direction = line[2][-2]
            #distance = int(line[1]) 
            distance = int(line[2][2:-2],16)
            next_direction = self.data[(i+1) % len(self.data)][2][-2]
            
            cursor = self.get_next_point(cursor, last_direction, direction, next_direction, distance)
            self.points.append(cursor)
            last_direction = direction
            
    def get_area(self):
        #print(self.points)
        area = 0
        j = len(self.points) - 1
        for i in range(len(self.points)):
            area += (self.points[j][1] + self.points[i][1]) * (self.points[j][0] - self.points[i][0])
            j = i
        #print(self.circumfrence)
        return abs(area // 2)
                
    def solve(self):
        self.get_coords()
        print(self.get_area())
        
    def run(self):
        input = self.__get_input()
        self.__parse(input)
        #print(self.data)
        self.solve()
        
Solution(sys.argv[1]).run()