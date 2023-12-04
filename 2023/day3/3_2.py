import sys


grid = []

def getDigitsRange(line, i):
    d_s = d_e = i
    while line[d_s].isdigit():
        d_s -= 1
    while line[d_e].isdigit():
        d_e += 1
    return d_s+1, d_e-1


def getGearRatio(r, c):
    digits = []
    
    e = c-1
    # check above
    while e <= c+1:
        if grid[r-1][e].isdigit():
            s, e = getDigitsRange(grid[r-1], e)
            digits.append(int(grid[r-1][s:e+1]))
        e += 1
    # check left
    if grid[r][c-1].isdigit():
        s, e = getDigitsRange(grid[r], c-1)
        digits.append(int(grid[r][s:e+1]))
    # check right
    if grid[r][c+1].isdigit():
        s, e = getDigitsRange(grid[r], c+1)
        digits.append(int(grid[r][s:e+1]))
    # check below
    e = c-1
    while e <= c+1:
        if grid[r+1][e].isdigit():
            s, e = getDigitsRange(grid[r+1], e)
            digits.append(int(grid[r+1][s:e+1]))
        e += 1
    if len(digits) == 2:
        return digits[0] * digits[1]
    return 0

def processLine(r: int) -> int:
    """Takes a row from the input and calculates it's score

    Returns: sum of the score for the row
    """
    row: str = grid[r]
    #print(row)
    score = 0

    # digitStart = -1
    for i, c in enumerate(row):
        if c == '*':
            score += getGearRatio(r, i)
    #     if c.isdigit() and digitStart == -1:
    #         digitStart = i
    #     elif digitStart != -1 and not c.isdigit():
    #         num = row[digitStart:i]
    #         score += getScore(num, r, digitStart)
    #         digitStart = -1
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
