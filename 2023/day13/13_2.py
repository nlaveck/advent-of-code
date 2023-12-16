import sys


def print_row(pattern, reflection):
    for i in range(len(pattern)):
        print(pattern[i])
        if i == reflection:
            print('-' * len(pattern[0]))



def row(pattern, reflection=-1, has_smudge=False):
    for i in range(1, len(pattern)):
        smudge = has_smudge
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
    return 0

def column(pattern, reflection=-1, has_smudge=False):
    for j in range(1,len(pattern[0])):
        smudge = has_smudge
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
            return j 
    return 0

def solve(pattern):
    if c := column(pattern):
        return c2 if (c2 := column(pattern, c, True)) else row(pattern, has_smudge=True) * 100
    else:
        r = row(pattern)
        return r2 * 100 if (r2 := row(pattern, r, True)) else column(pattern, has_smudge=True)



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