import sys
 
class Direction:
    left = (0,-1)
    right = (0,1)
    up = (-1,0)
    down = (1,0)
    
    all = [left, right, up, down]
    
class Solution:
    with open(sys.argv[1]) as in_file:
        GARDEN_MAP = [line.strip() for line in in_file.readlines()]
        M = len(GARDEN_MAP)
        N = len(GARDEN_MAP[0])
        memo = dict()
        
    def get_starting_point():
        for i in range(Solution.M):
            for j in range(Solution.N):
                if Solution.GARDEN_MAP[i][j] == 'S':
                    return (i,j)

    def in_bounds(node):
        return 0 <= node[0] < Solution.M and 0 <= node[1] < Solution.N

    def solve(steps, start=None):
        def get_steps(node, step_count):
            steps = set()
            outside_steps = set()
            grid, coords = node
            for d in Direction.all:
                new_coords = (coords[0] + d[0], coords[1] + d[1])
                new_grid = grid
                if not Solution.in_bounds(new_coords):
                    new_grid = (grid[0] + d[0], grid[1] + d[1])
                    new_coords = (new_coords[0] % Solution.M, new_coords[1] % Solution.N)
                    step = (new_grid, new_coords)
                    if step not in visited:
                        outside_steps.add(step, step_count+1)
                elif Solution.GARDEN_MAP[new_coords[0]][new_coords[1]] != '#':
                    step = (new_grid, new_coords)
                    if step not in visited:
                        steps.add(step)
                    
            return steps, outside_steps
        
        if not start:
            start = ((0,0), Solution.get_starting_point())
        visited = set()
        to_visit = [start]
        
        ans = 1 if steps % 2 == 0 else 0 
        
        for i in range(1, steps+1):
            #print(i)
            children = set()
            while to_visit:
                node = to_visit.pop()
                visited.add(node)
                children |= get_steps(node, i)
            if i % 2 == steps % 2:
                ans += len(children)
            to_visit = children

        return ans

print(Solution.solve(int(sys.argv[2])))
    
    