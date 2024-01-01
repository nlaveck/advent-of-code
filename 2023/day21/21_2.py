import sys
 
class Direction:
    LEFT = (0,-1)
    RIGHT = (0,1)
    UP = (-1,0)
    DOWN = (1,0)
    
    ALL = [LEFT, RIGHT, UP, DOWN]
    
class Solution:
    with open(sys.argv[1]) as in_file:
        GARDEN_MAP = [line.strip() for line in in_file.readlines()]
        M = len(GARDEN_MAP)
        N = len(GARDEN_MAP[0])
        memo = dict()
        grid_memo = dict()
        
    def get_starting_point():
        for i in range(Solution.M):
            for j in range(Solution.N):
                if Solution.GARDEN_MAP[i][j] == 'S':
                    return (i,j)

    def in_bounds(node):
        return 0 <= node[0] < Solution.M and 0 <= node[1] < Solution.N
        
    
    def solve(steps, start=None, grid=(0,0)):
        if steps < 0: return 0
        if steps == 0:
            return 1
        
        def get_steps(node):
            node_step = [(node[0] + d[0], node[1] + d[1], d) for d in Direction.ALL]
            out_of_bounds = set((n[0] % Solution.N, n[1] % Solution.M, n[2]) for n in node_step if not Solution.in_bounds(n) and n not in outside_nodes) 
            in_bounds = set((n[0], n[1]) for n in node_step if Solution.in_bounds(n) and Solution.GARDEN_MAP[n[0]][n[1]] != '#' and n not in visited)
            return in_bounds, out_of_bounds
        
        
        if not start:
            start = Solution.get_starting_point()

        
        if start not in Solution.memo:
            totals = [0]
            outside_nodes = dict()
            visited = set()

            to_visit = [start]
            step = 0
            
            while True:
                children = set()
                while to_visit:
                    node = to_visit.pop()
                    visited.add(node)
                    in_bounds, out_of_bounds = get_steps(node)
                    for oob in out_of_bounds:
                        outside_nodes[oob] = step + 1               
                    children |= in_bounds
                

                if len(totals) > 2:
                    totals[-1] += totals[-3]
                if not children:
                    break
                totals.append(0)
                step += 1
                to_visit = children
            
            Solution.memo[start] = {'totals': totals, 'outside_nodes': outside_nodes}
    
        totals = Solution.memo[start]['totals']      
        outside_nodes: dict = Solution.memo[start]['outside_nodes']
          
        if steps < len(totals):
            result = totals[steps]
        else:
            if len(totals)%2 == steps%2:
                result = totals[-2]
            else:
                result = totals[-1]
                
        if grid in Solution.grid_memo:
            result = max(Solution.grid_memo[grid] - result, 0)
        else:    
            Solution.grid_memo[grid] = result
            
        
            
        
        print(start, steps, result)
        for node, steps_taken in outside_nodes.items():
            result += Solution.solve(steps-steps_taken, (node[0], node[1]), (grid[0] + node[2][0], grid[1] + node[2][1]))
        return result
        

print(Solution.solve(int(sys.argv[2])))
    
    