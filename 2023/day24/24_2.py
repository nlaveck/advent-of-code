from collections import defaultdict
from functools import cache
import sys

points = []
points_at_time = []
vectors = defaultdict(list)
point_pairs = defaultdict(set)

with open(sys.argv[1]) as in_file:
    while line := in_file.readline().strip():
        coords, velocity = line.split(' @ ')
        x, y, z = (int(x) for x in coords.split(', '))
        vx, vy, vz = (int(x) for x in velocity.split(', '))
        #print(vx,vy,vz)

        points.append(((x,y,z),(vx,vy,vz)))
        
        
#print(points)
        
@cache
def position_at_time(p, t):
    pt = points[p]
    x = pt[0][0] + (t * pt[1][0])
    y = pt[0][1] + (t * pt[1][1])
    z = pt[0][2] + (t * pt[1][2])
    return (x,y,z)

def calculate_diff(p1,p2,delta_t):
    return ((p2[0] - p1[0])/delta_t, (p2[1] - p1[1])/delta_t, (p2[2] - p1[2])/delta_t) 

for t1 in range(1,1000):
    print(t1)
    for t2 in range(t1+1,1000):
        for p1 in range(len(points)):
            for p2 in range(p1+1,len(points)):
                
                pos1 = position_at_time(p1, t1)
                pos2 = position_at_time(p2, t2)
                diff = calculate_diff(pos1,pos2, t2-t1)
                #print(pos1,pos2)
                if (p1,p2) not in point_pairs[diff]:
                    vectors[diff] += [(pos1,t1), (pos2, t2)]
                    point_pairs[diff].add((p1,p2))
                
                
                pos1 = position_at_time(p2, t1)
                pos2 = position_at_time(p1, t2)
                diff = calculate_diff(pos1,pos2, t2-t1)
                if (p2,p1) not in point_pairs[diff]:
                    vectors[diff] += [(pos1,t1), (pos2,t2)]
                    point_pairs[diff].add((p2,p1))

key, items = [(k,v) for k, v in sorted(vectors.items(), key=lambda item: len(point_pairs[item[0]]))][-1]
print(point_pairs[key])
print(key,items, len(items))