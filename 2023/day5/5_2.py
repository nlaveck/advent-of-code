import sys
# current is a list of tuples representing start and end points
current = set()
next = set()

def convert(dest: int, source: int, length: int):
    global next, current

    #print('converting map: ', dest, source, length)
    toRemove = []
    toAdd = []
    sourceEnd = source + length - 1

    delta = dest-source

    for c in current:
        # if both points overlap
        if source <= c[0] <= c[1] <= sourceEnd:   
            next.add((c[0]+delta, c[1]+delta))
            toRemove.append(c)
            #print('\tBoth overlap: mapped range', c, 'to range', ((c[0]+delta, c[1]+delta)))

        # if the start overlaps
        elif source <= c[0] <= sourceEnd:
            next.add((c[0]+delta, sourceEnd+delta))
            #print('\tStart overlap: mapped range', (c[0],sourceEnd), 'to range', (c[0]+delta, sourceEnd+delta))
            toRemove.append(c)
            toAdd.append((sourceEnd+1, c[1]))
            

        # if the end overlaps
        elif source <= c[1] <= sourceEnd:
            next.add((source+delta, c[1]+delta))
            #print('\tEnd overlap: mapped range', (source,c[1]), 'to range', (c[0]+delta, sourceEnd+delta))
            toRemove.append(c)
            toAdd.append((c[0], source-1))
            

    
    current -= set(toRemove)
    current |= set(toAdd)    

def finishMapping():
    global next, current
    # add unmapped items from current
    next |= current

    # reassign current
    current = next

    #print('Finished mapping. New set:', current)

    # clear next
    next = set()

def getSeedPairs(input):
    for i in range(0, len(input), 2):
        yield (input[i], input[i+1])

def parse():
    with open(sys.argv[1], "r") as inFile:
        global current, next
        seedInput = [int(x) for x in inFile.readline().split(':')[1].split()]
        for i in range(0, len(seedInput), 2):
            current.add((seedInput[i], seedInput[i]+seedInput[i+1]-1))

        # jump to first set of maps

        #print(current)
        inFile.readline()
        inFile.readline()

        while line := inFile.readline():
            line = line.strip()

            # end of a map set
            if not line:
                finishMapping()
                
                #skip map label
                inFile.readline()
                continue

            else:
                dest, source, length = [int(x) for x in line.split()]
                convert(dest, source, length)
        finishMapping()

parse()
print(min(list(current), key=lambda x: x[0])[0])