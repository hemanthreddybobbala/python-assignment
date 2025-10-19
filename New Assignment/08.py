import math
def circle(r):
    area = math.pi * r**2
    perimeter = 2 * math.pi * r
    return area, perimeter
r = 2
area, perimeter = circle(r)
print('area =',area)
print('perimeter =',perimeter)