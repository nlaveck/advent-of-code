import re
import functools


# Checks if the round is possible based on the limits
def power(rounds: list[str], gameNum):
    maxVal = {'red': 0, 'green': 0, 'blue': 0}
    # enumerate through the rounds
    for round in rounds:
        colors = round.split(', ')
        vk = [c.split() for c in colors]

        # Check if value is over the limit
        for (v, k) in vk:
            if maxVal[k] < int(v):
                maxVal[k] = int(v)
    return functools.reduce(lambda a, b: a * b, maxVal.values())

def parseGame(input: str):
    input = input.strip()
    segments = re.split(': |; ', input)
    
    # Get the game number
    gameNum = int(segments[0][5:])
    
    rounds = segments[1:]
    return power(rounds, gameNum)

total = 0
with open("input.txt", "r") as inFile:
    while line := inFile.readline():
        total += parseGame(line)
print(total)
