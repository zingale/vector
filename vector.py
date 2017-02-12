# a simple class for 2 or 3 dimensional vectors in space

import math

class Vector(object):
    """a general 2- or 3-dimensional vector.  Operations involving a 2-d
    and 3-d vector will, in general, promote the 2-d vector to live in the
    x-y plane in 3-d space"""
    
    def __init__(self, x, y, z=None):
        self.x = x
        self.y = y
        self.z = z
        
        if z is not None:
            self.dim = 3
        else:
            self.dim = 2
            self.z = 0
        
    def __str__(self):
        if self.dim == 2:
            return "({}, {})".format(self.x, self.y)
        else:
            return "({}, {}, {})".format(self.x, self.y, self.z)

    def __repr__(self):
        if self.dim == 2:
            return "Vector({}, {})".format(self.x, self.y)
        else:
            return "Vector({}, {}, {})".format(self.x, self.y, self.z)

    def __add__(self, other):
        if isinstance(other, Vector):
            if self.dim == 2 and other.dim == 2:
                return Vector(self.x + other.x, self.y + other.y)
            else:
                return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            # it doesn't make sense to add anything but two vectors
            print("we don't know how to add a {} to a Vector".format(type(other)))
            raise NotImplementedError

    def __sub__(self, other):
        if isinstance(other, Vector):
            if self.dim == 2 and other.dim == 2:
                return Vector(self.x - other.x, self.y - other.y)
            else:
                return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            # it doesn't make sense to add anything but two vectors
            print("we don't know how to add a {} to a Vector".format(type(other)))
            raise NotImplementedError

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            # scalar multiplication changes the magnitude
            if self.dim == 2:
                return Vector(other*self.x, other*self.y)
            else:
                return Vector(other*self.x, other*self.y, other*self.z)
        else:
            print("we don't know how to multiply two Vectors")
            raise NotImplementedError

    def __matmul__(self, other):
        # a dot product
        if isinstance(other, Vector):
            return self.x*other.x + self.y*other.y + self.z*other.z
        else:
            print("matrix multiplication not defined")
            raise NotImplementedError

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        # we only know how to multiply by a scalar
        if isinstance(other, int) or isinstance(other, float):
            if self.dim == 2:
                return Vector(self.x/other, self.y/other)
            else:
                return Vector(self.x/other, self.y/other, self.z/other)

    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __neg__(self):
        if self.dim == 2:
            return Vector(-self.x, -self.y)
        else:
            return Vector(-self.x, -self.y, -self.z)

    def cross(self, other):
        # a vector cross product -- the result will always be a 3-d vector,
        # since the cross product in 2-d is in the z direction
        return Vector(self.y*other.z - self.z*other.y,
                      self.z*other.x - self.x*other.z,
                      self.x*other.y - self.y*other.x)

        
if __name__ == "__main__":

    # test it out

    u = Vector(1, 2)
    v = Vector(3, 5, 9)

    print(v)

    print("{} + {} = {}".format(u, v, u + v))
    print("{} - {} = {}".format(u, v, u - v))
    print(" ")

    print("{} * {} = {}".format(2.0, u, 2.0*u))
    print("{} * {} = {}".format(u, 2.0, u*2.0))
    print(" ")

    print("{} / {} = {}".format(u, 5.0, u/5.0))
    print(" ")

    print("dot product: {} @ {} = {}".format(u, v, u@v))
    print("cross product magnitude: {} x {} = {}".format(u, v, u.cross(v)))
    print(" ")

    print("magnitude: abs({}) = {}".format(u, abs(u)))



