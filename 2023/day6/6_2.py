import sys

with open(sys.argv[1], "r") as inFile:
    time = int(''.join(inFile.readline().strip().split()[1:]))
    distance = int(''.join(inFile.readline().strip().split()[1:]))

score = 0
for i in range(1,time):
    if i*(time-i) > distance:
        score += 1
print(score)