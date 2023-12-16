import sys, re

def current(springs: str):
    x = [len(x) for x in re.split('\.|\?',springs) if x]
    return x

def solve(springs: str, expected: list[int]):
    #print(springs)
    actual = current(springs)
    if actual == expected:
        return 1
    if actual and max(actual) > max(expected) or sum(actual) > sum(expected):
        return 0
    
    mutable = [c for c in springs]
    
    if '?' in mutable:
        idx = mutable.index('?')
        mutable[idx] = '.'
        operational = ''.join(mutable)
        mutable[idx] = '#'
        damaged = ''.join(mutable)
        return solve(operational, expected) + solve(damaged, expected)
    else:
        return 0


with open(sys.argv[1]) as in_file:
    points = 0
    while line := in_file.readline().strip():
        springs, expected = line.split()
        expected = [int(x) for x in expected.split(',')]
        combo = solve(springs, expected)
        #print(springs, expected, combo)
        points += combo
    print(points)
