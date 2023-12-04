import re

limits = {'red': 12, 'green': 13, 'blue': 14}

# Checks if the round is possible based on the limits
def isPossible(rounds: list[str], gameNum):
    # enumerate through the rounds
    for round in rounds:
        colors = round.split(', ')
        vk = [c.split() for c in colors]

        # Check if value is over the limit
        for (v, k) in vk:
            if limits[k] < int(v):
                print(gameNum, False)
                return False
        print(gameNum, True)
    return True

def parseGame(input: str):
    input = input.strip()
    segments = re.split(': |; ', input)
    
    # Get the game number
    gameNum = int(segments[0][5:])
    
    rounds = segments[1:]
    return gameNum if isPossible(rounds, gameNum) else 0

sum = 0
with open("input.txt", "r") as inFile:
    while line := inFile.readline():
        sum += parseGame(line)
print(sum)
