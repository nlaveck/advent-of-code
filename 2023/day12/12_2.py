from functools import cache
import sys, re

def current(springs: str):
    x = [len(x) for x in re.split('\.|\?',springs) if x]
    return x

def firstCount(springs: str):
    if '#' in springs:
        idx = springs.index('#')
        count = 1
        while idx + count < len(springs) and springs[idx+count] == '#':
            count += 1
        return count
    else:
        return 0


    


def solve(springs: str, expected: list[int]):

    # i = position in springs
    # j = position in expected
    @cache
    def dp(count, i, j):

        if i == len(springs):
            return 0
        
        new_springs = springs[i:]
        if j == len(expected):
            return 0 if '#' in new_springs else 1
        
        new_expected = expected[j:]

        if count == new_expected[0]:
            return dp(0, i, j+1) if springs[i] != '#' else 0


        for i2, v in enumerate(new_springs):
            if v == '?':
                return dp(count+1, i+i2+1, j) + dp(count, i+i2+1, j)
            if v == '#':
                return dp(count+1, i+i2+1, j)
        return 0

    return dp(0,0,0)




with open(sys.argv[1]) as in_file:
    points = 0
    while line := in_file.readline().strip():
        springs, expected = line.split()
        expected = [int(x) for x in expected.split(',')]
        springs *= 5
        expected *= 5
        combo = solve(springs, expected)
        print(springs, expected, combo)
        points += combo
    print(points)
