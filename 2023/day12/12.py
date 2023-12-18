import sys, re

def current(springs: str):
    x = [len(x) for x in re.split('\\.|\\?',springs) if x]
    return x

def solve(springs: str, expected: list[int]):
    actual = current(springs)
    if len(actual) >= 4 and actual[:4] == [1,1,3,1]:
        print(springs, actual)
        return 0
    if actual == expected:
        return 1
    # if  sum(actual) > sum(expected):
    #     return 0
    
    mutable = [c for c in springs]
    
    if '?' in mutable:
        idx = mutable.index('?')
        mutable[idx] = '.'
        operational = ''.join(mutable)
        mutable[idx] = '#'
        damaged = ''.join(mutable)
        #print(operational)
        return solve(operational, expected) + solve(damaged, expected)
    else:
        return actual == expected


with open(sys.argv[1]) as in_file:
    points = 0
    while line := in_file.readline().strip():
        springs, expected = line.split()
        expected = [int(x) for x in expected.split(',')] * 5
        springs *= 5
        combo = solve(springs, expected)
        break
        #print(springs, expected, combo)
        points += combo
    print(points)
