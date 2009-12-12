def area2(a,b,c):
    return (a.x - c.x) * (b.y - c.y) - (a.y - c.y) * (b.x - c.x)

def esquerdaEstrito(a,b,c):
    return area2(a,b,c) > 0

def esquerda(a,b,c):
    return area2(a,b,c) >= 0

def colinear(a,b,c):
    return area2(a,b,c) == 0

def entre(a,b,c):
    if colinear(a,b,c) == False: return False
    if a.x != b.x:
        return a.x <= c.x <= b.x or b.x <= c.x <= a.x
    else:
        return a.y <= c.y <= b.y or b.y <= c.y <= a.y

def intersectaprop(a,b,c,d):
    if colinear(a,b,c) or colinear(a,b,d) or colinear(c,d,a) or colinear(c,d,b): return False
    else: return (esquerdaEstrito(a,b,c) ^ esquerdaEstrito(a,b,d)) and (esquerdaEstrito(c,d,a) ^ esquerdaEstrito(c,d,b))

def inter(segmento1, segmento2): 
    if intersectaprop(segmento1.init, segmento1.to, segmento2.init, segmento2.to): return True
    elif entre(segmento1.init, segmento1.to, segmento2.init) or \
       entre(segmento1.init, segmento1.to, segmento2.to) or \
       entre(segmento2.init, segmento2.to, segmento1.init) or \
       entre(segmento2.init, segmento2.to, segmento1.to):
        return True
    else: return False
