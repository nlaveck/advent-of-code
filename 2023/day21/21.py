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
        
    def get_starting_point():
        for i in range(Solution.M):
            for j in range(Solution.N):
                if Solution.GARDEN_MAP[i][j] == 'S':
                    return (i,j)

    def in_bounds(node):
        return 0 <= node[0] < Solution.M and 0 <= node[1] < Solution.N

    def solve():
        def get_steps(node):
            node_step = [(node[0] + d[0], node[1] + d[1]) for d in Direction.all]
            return set(n for n in node_step if Solution.in_bounds(n) and Solution.GARDEN_MAP[n[0]][n[1]] != '#' and n not in visited)
            
        
        start = Solution.get_starting_point()
        steps = int(sys.argv[2])
        visited = set()
        to_visit = [start]
        
        ans = 1 if steps % 2 == 0 else 0 
        
        for i in range(1, steps+1):
            #print(i)
            children = set()
            while to_visit:
                node = to_visit.pop()
                visited.add(node)
                children |= get_steps(node)
            if i % 2 == steps % 2:
                ans += len(children)
            to_visit = children

        return ans

print(Solution.solve())
    
    