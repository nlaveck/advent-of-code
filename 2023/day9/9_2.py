import sys

def solve(input):
    diffs = [input[i] - input[i-1] for i in range(1,len(input))]
    # print(diffs)
    if diffs[0] == diffs[1] == diffs[2]:
        return input[0] - diffs[0]
    else:
        return input[0] - solve(diffs)

with open(sys.argv[1], "r") as inFile:
    total = 0
    while line := inFile.readline().strip(): 
        points = solve([int(x) for x in line.split()])
        # print('---')
        # print(points)
        total += points
        
    print(total)
    
