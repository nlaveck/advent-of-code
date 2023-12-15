import sys

with open(sys.argv[1], 'r') as inFile:
    input = inFile.readline().strip().split(',')
score = 0
for step in input:
    current_value = 0
    for c in step:
        #print(ord(c))
        current_value += ord(c)
        current_value *= 17
        current_value %= 256
    score += current_value
print(score)