import sys
from collections import defaultdict

card_counts = defaultdict(lambda: 1)

def solve(i, line):
    # remove "Card #: "
    line = line[line.index(':')+2:]

    # parse winners and card to lists
    winners, card = [x.split() for x in line.split('|')]
    
    # count matches in set of winners
    matches = len([n for n in card if n in set(winners)])

    for x in range(i+1,i+matches+1):
        card_counts[x] += card_counts[i]
    
    # reference to assign default value for cases with no matches
    card_counts[i]





with open(sys.argv[1], "r") as inFile:
    score = 0
    i = 1
    while line := inFile.readline().strip():
        solve(i, line)
        i += 1
    #print(card_counts)
    print(sum(card_counts.values()))

    