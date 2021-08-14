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
        return product
    
    def angle(self,v):
        unit1 = self.direction()
        unit2 = v.direction()
        print(unit1,unit2)
        inn_prod = unit1.inner_product(unit2)
        return acos(inn_prod)






v = VectorAlg([2,3])
w = VectorAlg([9,2])
print(v.inner_product(w))
print(v.direction())
print(v.magnitude())
print(v.scalar(4))
print(v.add(w))
