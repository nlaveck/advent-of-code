import sys

def get_hash_string():
    return ''.join([''.join(x) for x in panel])

def output():
    print('\n******\n')
    for r in panel:
        print(''.join(r))

def score():
    score = 0
    for r in range(row_count):
        for c in range(col_count):
            if panel[r][c] == 'O':
                score += row_count - r
    return score

def north():
    for col in range(col_count):
        next_rock_idx = 0
        for row in range(row_count):
            cell = panel[row][col]
            if cell == 'O':
                panel[row][col] = '.'
                panel[next_rock_idx][col] = 'O'
                next_rock_idx += 1
            elif cell == '#':
                next_rock_idx = row + 1

def south():
    for col in range(col_count):
        next_rock_idx = col_count-1
        for row in range(row_count-1,-1,-1):
            cell = panel[row][col]
            if cell == 'O':
                panel[row][col] = '.'
                panel[next_rock_idx][col] = 'O'
                next_rock_idx -= 1
            elif cell == '#':
                next_rock_idx = row - 1
    
def west():
    for row in range(row_count):
        next_rock_idx = 0
        for col in range(col_count):
            cell = panel[row][col]
            if cell == 'O':
                panel[row][col] = '.'
                panel[row][next_rock_idx] = 'O'
                next_rock_idx += 1
            elif cell == '#':
                next_rock_idx = col + 1

def east():
    for row in range(row_count):
        next_rock_idx = col_count-1
        for col in range(col_count-1, -1, -1):
            cell = panel[row][col]
            if cell == 'O':
                panel[row][col] = '.'
                panel[row][next_rock_idx] = 'O'
                next_rock_idx -= 1
            elif cell == '#':
                next_rock_idx = col - 1

with open(sys.argv[1], "r") as inFile:
    panel = [[c for c in line.strip()] for line in inFile.readlines()]
    row_count = len(panel)
    col_count = len(panel[0])
    
    
    rotation = [north, west, south, east]
    
    cycle_hash = {}
    scores = []
    loop_start = -1
    
    for i in range(1000):
        for fn in rotation:
            fn()
            #output()
        key = get_hash_string()
        #print(i, score())
        scores.append(score())
        if key in cycle_hash:
            start = cycle_hash[key]
            loop = scores[start:-1]
            #print('loop detected', start, loop)
            
            loop_end_idx = (1000000000 - 1 - i) % len(loop)
            #print(loop, loop_idx)
            print(loop[loop_end_idx])
            break
        else:
            cycle_hash[key] = i
 