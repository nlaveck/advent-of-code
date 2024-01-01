import sys, re

MIN = int(sys.argv[2])
MAX = int(sys.argv[3])

def line_intersection(line1, line2):
    #print(line1, line2)
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])
    
    # line1_positive = ydiff[0]/xdiff[0] > 0
    # line2_positive = xdiff[1]/ydiff[1] > 0

    def det(x, y):
        return x[0] * y[1] - x[1] * y[0]

    div = det(xdiff, ydiff)
    if div == 0:
       return False

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    
    
    in_range = MIN <= x <= MAX and MIN <= y <= MAX
    in_future = (line1[0][0] < line1[1][0]) == (line1[0][0] < x) \
    and (line2[0][0] < line2[1][0]) == (line2[0][0] < x) \
    and (line1[0][1] < line1[1][1]) == (line1[0][1] < y) \
    and (line2[0][1] < line2[1][1]) == (line2[0][1] < y)
    
    return 1 if in_range and in_future else 0

points = []

with open(sys.argv[1]) as in_file:
    while line := in_file.readline().strip():
        coords, velocity = line.split(' @ ')
        x, y, z = (int(x) for x in coords.split(', '))
        vx, vy, vz = (int(x) for x in velocity.split(', '))
        #print(vx,vy,vz)
        
        points.append(((x,y),(x+vx, y+vy)))
        
#print(points)
        
total = 0

for i in range(len(points)):
    #print(points[i])
    for j in range(i+1,len(points)):    
        total += line_intersection(points[i], points[j])
print(total)