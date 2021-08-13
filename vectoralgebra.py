from math import sqrt
class VectorsAlg:


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
        sum = 0
        for i in mag:
            sum += i
        return round(sqrt(sum), 3)




v = VectorsAlg([2,3])
w = VectorsAlg([9,2])
print(v.magnitude())
print(v.scalar(4))
print(v.add(w))
