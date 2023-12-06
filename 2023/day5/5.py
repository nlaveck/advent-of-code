import sys

current: set = set()
next: set = set()

def convert(dest: int, source: int, length: int):
    global next, current
    toRemove = []

    for c in current:
        # if the current item is in the range of the map
        if source <= c <= source + length - 1:
            print('mapping', c, 'to', c-source+dest)
            next.add(c-source+dest)
            toRemove.append(c)

    current -= set(toRemove)

def finishMapping():
    global next, current
    # add unmapped items from current
    next |= current

    # reassign current
    current = next

    print('Finished mapping. New set:', current)

    # clear next
    next = set()

def parse():
    with open(sys.argv[1], "r") as inFile:
        global current, next
        current = set(int(x) for x in inFile.readline().split(':')[1].split())
        next = set()

        # jump to first set of maps
        inFile.readline()
        inFile.readline()

        while line := inFile.readline():
            line = line.strip()

            # end of a map set
            if not line:
                finishMapping()
                
                #skip map label
                inFile.readline()
                continue;

            else:
                dest, source, length = [int(x) for x in line.split()]
                convert(dest, source, length)
        finishMapping()

parse()
print(min(list(current)))