import sys


def row(pattern):
    for i in range(1, len(pattern)):
        stop = False
        for offset in range(0, min(i, len(pattern)-i)):
            print((i-1-offset,i+offset))
            for j in range(len(pattern[0])):
                if pattern[i-1-offset][j] != pattern[i+offset][j]:
                    stop = True
                    break
            if stop:
                break
        if not stop:
            # done
            return i
    return -1

def column(pattern):
    for j in range(1,len(pattern[0])):
        stop = False
        for offset in range(0, min(j, len(pattern[0])-j)):
            for i in range(len(pattern)):
                if pattern[i][j-1-offset] != pattern[i][j+offset]:
                    stop = True
                    break
            if stop:
                break
        if not stop:
            # done
            print(j)
            return j 
    return -1


def solve(pattern):
    if (col := column(pattern)) > 0:
        return col
    else:
        return row(pattern) * 100




score = 0
with open(sys.argv[1], "r") as in_file:
    pattern = []
    while line := in_file.readline():
        #print(line)
        line = line.strip()
        if not line:
            score += solve(pattern)
            pattern = []
        else:
            pattern.append(line)
    score += solve(pattern)
    print(score)