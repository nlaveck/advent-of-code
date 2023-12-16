import sys


def print_row(pattern, reflection):
    for i in range(len(pattern)):
        print(pattern[i])
        if i == reflection:
            print('-' * len(pattern[0]))



def row(pattern, reflection=-1, smudge=False):
    for i in range(1, len(pattern)):
        if i == reflection: continue
        stop = False
        for offset in range(0, min(i, len(pattern)-i)):
            #print((i-1-offset,i+offset))
            for j in range(len(pattern[0])):
                if pattern[i-1-offset][j] != pattern[i+offset][j]:
                    stop = True
                    if smudge:
                        stop = smudge = False
                    else:
                        break
            if stop:
                break
        if not stop:
            # done
            return i
    return -1

def column(pattern, reflection=-1, smudge=False):
    for j in range(1,len(pattern[0])):
        if j == reflection: continue
        stop = False
        for offset in range(0, min(j, len(pattern[0])-j)):
            for i in range(len(pattern)):
                if pattern[i][j-1-offset] != pattern[i][j+offset]:
                    stop = True
                    if smudge:
                        stop = smudge = False
                    else:
                        break
            if stop:
                break
        if not stop:
            # done
            #print(j)
            return j 
    return -1

def solve(pattern):
    score = None
    c = column(pattern)
    r = row(pattern)
    c2 = column(pattern, c, True)
    c3 = column(pattern, smudge=True)
    r2 = row(pattern, r, True)
    r3 = row(pattern, smudge=True)
    print(c2, r2, c3, r3)
    return 0

def solve2(pattern):
    if (col := column(pattern)) > 0:
        print(col)
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