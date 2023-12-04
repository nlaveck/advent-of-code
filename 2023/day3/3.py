import sys

grid = []
def getScore(num, r, c):
    isSymbol = lambda x: x != '.' and not x.isdigit()
       
    val = int(num)
    # check top
    for x in grid[r-1][c:c+len(num)]:
        if isSymbol(x):
            return val
    # check bottom
    for x in grid[r+1][c:c+len(num)]:
        if isSymbol(x):
            return val
    # check left
    if isSymbol(grid[r][c-1]):
        return val
    # check right
    if isSymbol(grid[r][c+len(num)]):
        return val
    # check top-left
    if isSymbol(grid[r-1][c-1]):
        return val
    # check top-right
    if isSymbol(grid[r-1][c+len(num)]):
        return val
    # check bottom-left
    if isSymbol(grid[r+1][c-1]):
        return val
    # check bottom-right
    if isSymbol(grid[r+1][c+len(num)]):
        return val

    return 0

def processLine(r: int) -> int:
    """Takes a row from the input and calculates it's score

    Returns: sum of the score for the row
    """
    row: str = grid[r]
    #print(row)
    score = 0
    digitStart = -1
    for i, c in enumerate(row):
        if c.isdigit() and digitStart == -1:
            digitStart = i
        elif digitStart != -1 and not c.isdigit():
            num = row[digitStart:i]
            score += getScore(num, r, digitStart)
            digitStart = -1
    return score

with open(sys.argv[1], "r") as inFile:
    row = 0
    while line := inFile.readline().strip():
        if row == 0:
            grid.append('.' * (len(line) + 2))
        grid.append('.' + line + '.')
        row += 1

n = len(grid[0])
grid.append('.' * n)
m = len(grid)

score = 0
for i in range(m):
    #print(grid[i])
    score += processLine(i)
print(score)
