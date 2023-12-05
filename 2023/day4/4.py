import sys

def points(line):
    # remove "Card #: "
    line = line[line.index(':')+2:]

    # parse winners and card to lists
    winners, card = [x.split() for x in line.split('|')]
    
    # count matches in set of winners
    matches = len([n for n in card if n in set(winners)])

    return 2**matches // 2
            



with open(sys.argv[1], "r") as inFile:
    score = 0
    while line := inFile.readline().strip():
        score += points(line)
    print(score)
    