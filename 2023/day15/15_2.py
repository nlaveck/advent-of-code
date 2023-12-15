import sys

boxes = [dict() for i in range(256)]


def hash_value(label: str):
    current_value = 0
    for c in label:
        #print(ord(c))
        current_value += ord(c)
        current_value *= 17
        current_value %= 256
    return current_value
    
        

with open(sys.argv[1], 'r') as inFile:
    input = inFile.readline().strip().split(',')
    for step in input:
        
        label = operation = lens = None
        if step[-1] == '-':
            label = step[:-1]
            operation = '-'
            lens = -1
        else:
            label = step[:-2]
            operation = '='
            lens = int(step[-1])
    
    
        box_idx = hash_value(label)
        
        if operation == '-':
            if label in boxes[box_idx]:
                del boxes[box_idx][label]
        else:
            boxes[box_idx][label] = lens
    
    score = 0
    for i, box in enumerate(boxes):
        for j, lens in enumerate(box.values()):
            lens_value = (i+1) * lens * (j+1)
            print(lens_value)
            score += lens_value
    print(score)