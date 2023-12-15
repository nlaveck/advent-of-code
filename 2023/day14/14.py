import sys


with open(sys.argv[1], "r") as inFile:
    input = [line.strip() for line in inFile.readlines()]
    
    total = 0
    mx = len(input)
    for i in range(len(input[0])):
        top_score = mx
        for j in range(len(input)):
            if input[j][i] == 'O':
                total += top_score
                print(i, top_score)
                top_score -= 1
            elif input[j][i] == '#':
                top_score = mx - j - 1
    print(total)
    