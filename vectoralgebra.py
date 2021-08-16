from math import acos, sqrt
class VectorAlg:


    def __init__(self,coordinates):
        self.coordinates = coordinates

    def add(self,v):
        sum = [x+y for x,y in zip(self.coordinates,v.coordinates)]
        return sum

    def sub(self,v):
        difference = [x-y for x,y in zip(self.coordinates,v.coordinates)]
        return difference

    def scalar(self,c):
        scale = [c*x for x in self.coordinates]
        return scale

    def __str__(self):
        return "Vector: {}".format(self.coordinates)

    def magnitude(self):
            squares = [ x*x for x in self.coordinates]
            return sqrt(sum(squares))

    def direction(self):
            mag = self.magnitude()
            return self.scalar(1/mag)
            
    def dot(self, v):
        prod = [x*y for x,y in zip(self.coordinates, v.coordinates)]
        return sum(prod)

    def angle(self,v):
        dir1 = self.direction()
        dir2 = v.direction()
        d3 = dir1.dot(dir2)
        in_radian = acos(dir1.dot(dir2))
        return in_radian



v = VectorAlg([2,3])
w = VectorAlg([9,2])
print(v.dot(w))
# print(v.angle(w) 
# print(v.magnitude())
# print(v.scalar(4))
# print(v.add(w))
