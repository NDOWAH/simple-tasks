from math import sqrt,acos
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
        mag = [x*x for x in self.coordinates]
        return round(sqrt(sum(mag)), 3)

    def direction(self):
        mag = self.magnitude()
        return self.scalar(1/mag)

    def inner_product(self,v):
        product = [x*y for x,y in zip(self.coordinates,v.coordinates)]
        return sum(product)
    
    def angle(self,v):
        dir1 = self.direction()
        dir2 = v.direction()
        product = dir1.inner_product(dir2)
        print(product)
        return None


v = VectorAlg([2,3])
w = VectorAlg([9,2])
print(v.angle(w))
# print(v.inner_product(w))
# print(v.direction())
# print(v.magnitude())
# print(v.scalar(4))
# print(v.add(w))
