from math import acos, sqrt, pi
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

    def angle(self, v, in_degree = False):
            dir1 = self.direction()
            dir2 = v.direction()
            d3 = dir1.dot(dir2)
            in_radian = acos(dir1.dot(dir2))
            if in_degree:
                degrees_per_radian = 180/pi

                return in_radian * in_radian
    def is_orthogonal_to(self, v, tolerance = 1e-10):
        return abs(self.dot(v)) < tolerance

    def is_parallel_to(self, v):
        return(self.is_zero()
        or v.is_zero()
        or self.angle_with(v)==0
        or self.angle_with(v) == pi)

    def is_zero(self,tolerance=1e-10):
        return self.magnitude < tolerance
    
    def projection(self,v):
        dir = self.direction
        proj = v.scalar((self.direction()))
        return proj

    def cross_prod(self, v):
        x_1,y_1, z_1 = self.coordinates()
        x_2,y_2,z_2 = self.coordinates()
        new_coordinates = [y_1*z_2 - z_1*y_2,
                           -(x_1*z_2 - x_2*z_1),
                           x_1*y_2 - y_1*x_1]
        return VectorAlg(new_coordinates)
    
    def area_of_parallel0gram(self,v):
        vector = self.cross_prod()
        return vector.magnitude()

    
    def area_of_triangle(self,v):
        return self.area_of_parallelogram(v)/ Decimal("2.0")


v = VectorAlg([9,3])
w = VectorAlg([9,2])
print(v.projection(w))
print("the angle is: ", v.dot(w))
# print(v.angle(w) 
# print(v.magnitude())
# print(v.scalar(4))
# print(v.add(w))
