hello_string ="hello tower project"
print(hello_string)

def distance(p1,p2):
    x1,y1 = p1
    x2,y2 = p2
    d = ( (x2-x1)**2 + (y2-y1)**2   )**0.5
    return d
print(
distance((3,6),(-6,7))
)