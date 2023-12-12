import sys, re

map = dict()
with open(sys.argv[1], "r") as inFile:
    directions = inFile.readline().strip()
    # consume blank line
    inFile.readline()

    while line := inFile.readline().strip():
        key, l, r = [x for x in re.split(' = |, |\(|\)', line) if x]
        map[key] = {'L': l, 'R':r}
    
    steps = 0
    lastStep = 'AAA'
    while(lastStep != 'ZZZ'):
        lastStep = map[lastStep][directions[steps%len(directions)]]
        steps += 1
    print(steps)

