import sys

with open(sys.argv[1], "r") as inFile:
    time = [int(x) for x in inFile.readline().strip().split()[1:]]
    distance = [int(x) for x in inFile.readline().strip().split()[1:]]

total = 1
for t, d in zip(time, distance):
    score = 0
    for i in range(1,t):
        if i*(t-i) > d:
            score += 1
    total *= score
print(total)