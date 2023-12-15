
import sys


galaxies = []
distance = 0
with open(sys.argv[1], "r") as inFile:
    i = 0
    input = [line.strip() for line in inFile.readlines()]
    row_totals = [0] * len(input)
    col_totals = [0] * len(input[0])
    
    for i, line in enumerate(input):
        for j, c in enumerate(line):
            if c == '#':
                for g in galaxies:
                    distance += abs(g[0] - i) + abs(g[1] - j)
                galaxies.append((i,j))
                row_totals[i] += 1
                col_totals[j] += 1
    
    totals = [row_totals, col_totals]
    
    for totals in [row_totals, col_totals]:
        for i,v in enumerate(totals):
            if v == 0:
                distance += sum(totals[:i]) * sum(totals[i+1:]) * 999999                    
    print(distance)