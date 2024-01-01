import sys

map_data = []



with open(sys.argv[1]) as in_file:
    while line := in_file.readline().strip():
        map_data.append(line)
        
M = len(map_data)
N = len(map_data[0])

start = (1, 0)
end = (N-2, M-1)

to_visit = set([start])
while to_visit:
    node = to_visit.pop()