from collections import Counter
import sys

card_values = {'2' : 2,
               '3': 3,
               '4': 4,
               '5': 5,
               '6': 6,
               '7': 7,
               '8': 8,
               '9': 9,
               'T': 10,
               'J': 1,
               'Q': 12,
               'K': 13,
               'A': 14}

def score(cards: str):
    bin_padding = len(bin(card_values['A']))-2

    pairs = Counter(cards)
    wildcards = pairs['J']
    del pairs['J']

    if pairs:
        max_pair = max(pairs.values()) + wildcards
    else:
        max_pair = 5

    hand_rank = 0
    if max_pair == 1:
        # high card
        hand_rank = 1
    elif max_pair == 2 and len(pairs) == 4:
        # one pair
        hand_rank = 2
    elif max_pair == 2 and len(pairs) == 3:
        # two pair
        hand_rank = 3
    elif max_pair == 3 and len(pairs) == 3:
        # three of a kind
        hand_rank = 4
    elif max_pair == 3 and len(pairs) == 2:
        # full house
        hand_rank = 5
    elif max_pair == 4:
        # four of a kind
        hand_rank = 6
    elif max_pair == 5:
        # five of a kind
        hand_rank = 7
    else:
        raise Exception('Unhandled hand rank') 

    score = hand_rank << bin_padding * 5

    nums = []
    for i,c in enumerate(cards[::-1]):
        nums.append(card_values[c])
        score += card_values[c] << (bin_padding * i)
    #print([hand_rank] + nums[::-1])
    return score
        

    


with open(sys.argv[1], "r") as inFile:
    hands = []
    winnings = 0
    while line := inFile.readline().strip():
        cards, bid = line.split()
        #print(cards)
        hands.append((score(cards), bid, hands))

    for i, v in enumerate(sorted(hands)):
        winnings += (i+1) * int(v[1])
    print(winnings)