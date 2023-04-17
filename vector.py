import math



class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def dot(self, other):
        return self.x*other.x + self.y*other.y + self.z*other.z

    def cross(self, other):
        return (self.y*other.z - self.z*other.y) - (self.x*other.z - self.z*other.x) + (self.x*other.y - self.y*other.x)
    
    def __add__(self, other):
        return Vector(self.x+other.x, self.y+other.y, self.z+other.z)
    
    def __sub__(self, other):
        return Vector(self.x-other.x, self.y-other.y, self.z-other.z)
    
    def x_component(self):
        return Vector(self.x,0,0)
    
    def y_component(self):
        return Vector(0,self.y,0)
    
    def z_component(self):
        return Vector(0,0,self.z)
    
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def __mul__(self,scalar):
        return Vector(self.x*scalar, self.y*scalar, self.z*scalar)
    
    def duplicate(self):
        return Vector(self.x, self.y, self.z)
    
    def unit(self):
        return self*(1/self.magnitude())
    
  