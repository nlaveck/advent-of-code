from collections import defaultdict
from functools import cache, reduce
import sys, re, copy


workflows = dict()
accepted = 0

def run_step(step, parts):
    condition, action = step.split(':')
    category = condition[0]
    comparison = condition[1]
    value = int(condition[2:])
    
    if comparison == '>':
        process_action(action, parts, category, range(value+1, 4001), step) 
    else:
        process_action(action, parts, category, range(0, value), step)
    
    #print(step, [(c, sum(parts[c])) for c in 'xmas'])


def process_action(action, parts, category = None, range_value: range = None, step=None):
    global accepted
    parts_copy = copy.deepcopy(parts)
    
    num = 1
    if category:
        num = 0
        for x in range_value:
            if parts[category][x] == 1:
                parts[category][x] = 0
                num += 1
                
    if action == 'A':
        sums = [sum(parts[c]) for c in 'xmas' if c != category]
        multiplier = reduce(lambda x,y: x*y, sums)
        accepted += num * multiplier
        #print(accepted)
    elif action != 'R':
        if category:
            for i in range(len(parts_copy[category])):
                if i not in range_value: parts_copy[category][i] = 0
        
            #print(step, [(c, sum(parts_copy[c])) for c in 'xmas'])
        run_workflow(action, parts_copy)

def run_workflow(label, parts): 
    workflow = workflows[label]
    for step in workflow[:-1]:
        run_step(step, parts)
    process_action(workflow[-1], parts)


def solve():
    parts = {'x': [1] * 4001, 'm': [1] * 4001, 'a': [1] * 4001, 's': [1]*4001}

    parts['x'][0] = 0
    parts['m'][0] = 0
    parts['a'][0] = 0
    parts['s'][0] = 0
    run_workflow('in', parts)
    

with open(sys.argv[1]) as in_file:
    while line := in_file.readline().strip():
        arr = re.split('{|}|,', line)[:-1]
        workflows[arr[0]] = arr[1:]


    solve()
    print(accepted)