from collections import defaultdict
import sys, re


workflows = dict()
parts = []

def run_step(step, part):
    condition, action = step.split(':')
    category = condition[0]
    comparison = condition[1]
    value = int(condition[2:])
    
    succeeded = None
    
    if comparison == '>':
        succeeded = part[category] > value
    else:
        succeeded = part[category] < value
        
    if succeeded:
        return action

def run_workflow(label, part: dict):
    def process_action(action):
        if action == 'A':
            return sum(part.values())
        elif action == 'R':
            return 0
        else:
            return run_workflow(action, part)
    
        
    
    workflow = workflows[label]
    for step in workflow[:-1]:
        action = run_step(step, part)
        if action: return process_action(action)
    return process_action(workflow[-1])


def solve(part):
    return run_workflow('in', part)
    

with open(sys.argv[1]) as in_file:
    while line := in_file.readline().strip():
        arr = re.split('{|}|,', line)[:-1]
        workflows[arr[0]] = arr[1:]
    
    while line := in_file.readline().strip():
        arr = re.split('{|}|,',line)[1:-1]
        parts.append(dict((x[0],int(x[1])) for x in [val.split('=') for val in arr]))
        
    print(sum(solve(p) for p in parts))