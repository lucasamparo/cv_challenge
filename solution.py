test_cases = int(input())

def sum_coords(a, b):
    return [a.x + b.x, a.y + b.y]

def sub_coords(a, b):
    return [b.x - a.x, b.y - a.y]

def mul_coords(a, ld):
    return [ld * a.x, ld * a.y]

def div_coords(a, ld):
    return [a.x / ld, a.y / ld]

def cross(pt_a, pt_b):
    return ((pt_a.x*pt_b.y) - (pt_a.y*pt_b.x))

def inverse(pt):
    return [-pt.y, pt.x]

def find_intersect(l1, l2):
    d = cross(l1.pos, l2.pos)
    pt1 = Star(mul_coords(l1.pos, l2.loc))
    pt2 = Star(mul_coords(l2.pos, l1.loc))
    subt = Star(sub_coords(pt1, pt2))
    ret = Star(div_coords(subt, d))
    return ret

class Star(object):
    def __init__(self, coord):
        self.x = coord[0]
        self.y = coord[1]

    def split(self):
        self.x = self.x/2
        self.y = self.y/2

class Line(object):
    def __init__(self, p, q):
        self.pos = Star([p.x - q.x,p.y - q.y])
        self.loc = cross(self.pos, p)
        
    def perp(self, p):
        _cross = Star(inverse(self.pos))
        return Line(p, Star(sum_coords(p, _cross)))


for i in range(test_cases):
    st_old = Star([float(x) for x in input().split(" ")])
    nd_old = Star([float(x) for x in input().split(" ")])

    st_new = Star([float(x) for x in input().split(" ")])
    nd_new = Star([float(x) for x in input().split(" ")])

    mtx_a = Star(sum_coords(st_old, st_new))
    mtx_b = Star(sum_coords(nd_old, nd_new))

    mtx_a.split()
    mtx_b.split()

    l1 = Line(st_old, st_new)
    l2 = Line(nd_old, nd_new)

    l1 = l1.perp(mtx_a)
    l2 = l2.perp(mtx_b)

    out = find_intersect(l1, l2)

    print("Caso #%d: %.2f %.2f" %(i+1, out.x, out.y))
