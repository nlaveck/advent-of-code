from collections import defaultdict
from functools import cache
import sys

points = []
points_at_time = []
vectors = defaultdict(list)
point_pairs = defaultdict(set)

TIME_MAX = 1000

with open(sys.argv[1]) as in_file:
    while line := in_file.readline().strip():
        coords, velocity = line.split(' @ ')
        x, y, z = (int(x) for x in coords.split(', '))
        v, vy, vz = (int(x) for x in velocity.split(', '))
        points.append(((x,y,z),(v,vy,vz)))
        #print(vx,vy,vz)
    
    points_at_time = [[(p[0][0] + (t * p[1][0]), p[0][1] + (t * p[1][1]), p[0][2] + (t * p[1][2])) for t in range(0,TIME_MAX)] for p in points]
    
    
    totals = defaultdict(int)
    x_offsets: dict[defaultdict[set]] = [defaultdict(set)] * 2000
    y_offsets: dict[defaultdict[set]] = [defaultdict(set)] * 2000
    z_offsets: dict[defaultdict[set]] = [defaultdict(set)] * 2000
    
    vt = [[v*t for v in range(-1000,1000)] for t in range(1, TIME_MAX)]
    print(len(vt))

    x = dict()
    x.values()
    for v in range(-1000,1000):
        print(v)
        for t in range(1,TIME_MAX):
            for i, p in enumerate(points_at_time):
                x_diff = p[t][0] - vt[v+1000][t]
                y_diff = p[t][1] - vt[v+1000][t]
                z_diff = p[t][2] - vt[v+1000][t]
                if i not in x_offsets[v+1000][x_diff]:
                    x_offsets[v+1000][x_diff].add(i)
                if i not in y_offsets[v+1000][y_diff]:
                    y_offsets[v+1000][y_diff].add(i)
                if i not in z_offsets[v][z_diff]:
                    z_offsets[v+1000][z_diff].add(i)
                    
    #print([(k, len(v)) for k,v in x_offsets[0].items()])
    #print(x_offsets[0])
    
    def get_values(offsets):     
        x = [(k,v) for k,v in sorted(offsets.items(), key=lambda x: max(x[1].values(), key=lambda y: len(y)), reverse=True)][0]
        #print(x)
        #print(x[1])
        max_set = max(x[1].items(), key=lambda xx: len(xx[1]))
        return (x[0], max_set[0], len(max_set[1]))
    
    print(get_values(x_offsets))
    print(get_values(y_offsets))
    print(get_values(z_offsets))

def calculate_diff(p1,p2,delta_t):
    return ((p2[0] - p1[0])/delta_t, (p2[1] - p1[1])/delta_t, (p2[2] - p1[2])/delta_t)
x