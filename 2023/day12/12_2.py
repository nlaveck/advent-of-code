from functools import cache
import sys, re

def current(springs: str):
    x = [len(x) for x in re.split('\\.|\\?',springs) if x]
    return x

@cache
def solve(springs: str, expected_idx):
    
    expected_slice = expected[expected_idx:]
    #print(springs, expected)
    actual = current(springs)

    if actual == expected_slice:
        return 1
    if  sum(actual) > sum(expected_slice):
        return 0

    if '?' in springs:
        idx = springs.index('?')

        first_half = springs[:idx]
        second_half = springs[idx+1:]

        operational = '.' + second_half
        damaged = '#' + second_half

        solved = current(first_half)
        prefix = ''

        #if first half ends with '#'
        if first_half and first_half[-1] == '#':
            prefix = '#' * solved[-1]
            solved = solved[:-1]
            
        if any(solved[i] != expected_slice[i] for i in range(len(solved))):
            return 0
        return solve(prefix + operational, expected_idx+len(solved)) + solve(prefix + damaged, expected_idx+len(solved))
    else:
        return 0

with open(sys.argv[1]) as in_file:
    points = 0
    while line := in_file.readline().strip():
        springs, expected = line.split()
        expected = [int(x) for x in expected.split(',')] * 5
        springs = '?'.join([springs]*5)

        combo = solve(springs, 0)
        #print(combo)
        points += combo

    print(points)
