import math
from random import random, randrange

class vec3:
    def __init__(self, e0=0, e1=0, e2=0):
        self.e = [e0, e1, e2]
    
    def fill(self,v):
        self.e = [v,v,v]
    
    def x(self):
        return self.e[0]
    
    def y(self):
        return self.e[1]
    
    def z(self):
        return self.e[2]
    
    def __neg__(self):
        return vec3(-self.e[0], -self.e[1], -self.e[2])
    
    def __getitem__(self, i):
        return self.e[i]
    
    def __setitem__(self, i, value):
        self.e[i] = value
    
    def __iadd__(self, v):
        self.e[0] += v.e[0]
        self.e[1] += v.e[1]
        self.e[2] += v.e[2]
        return self
    
    def __imul__(self, t):
        self.e[0] *= t
        self.e[1] *= t
        self.e[2] *= t
        return self

    def __idiv__(self, t):
        return self.__imul__(1/t)
    
    def length(self):
        return math.sqrt(self.length_squared())
    
    def length_squared(self):
        return float(self.e[0]) ** 2 + float(self.e[1]) ** 2 + float(self.e[2]) ** 2

    def __str__(self):
        return f"{self.e[0]} {self.e[1]} {self.e[2]}"

    def __mul__(u,v):
        if type(u) == vec3 and type(v) == vec3:
            return vec3(u.e[0] * v.e[0], u.e[1] * v.e[1], u.e[2] * v.e[2])
        elif type(v) == vec3:
            return vec3(u*v.e[0], u*v.e[1], u*v.e[2])
        elif type(u) == vec3:
            return vec3(v*u.e[0], v*u.e[1], v*u.e[2])
        
    def __add__(u,v):
        return vec3(u.e[0] + v.e[0], u.e[1] + v.e[1], u.e[2] + v.e[2])

    def __sub__(u,v):
        return vec3(u.e[0]-v.e[0],u.e[1]-v.e[1],u.e[2]-v.e[2])
    
    def __truediv__(u, v):
        if type(u) == vec3 and type(v) == vec3:
            return vec3(u.e[0] / v.e[0], u.e[1] / v.e[1], u.e[2] * v.e[2])
        elif type(v) == vec3:
            return vec3(u/v.e[0], u/v.e[1], u/v.e[2])
        elif type(u) == vec3:
            return vec3(u.e[0]/v, u.e[1]/v, u.e[2]/v)
    
    def nearZero(self):
        s = 10**-8
        return abs(self.e[0] < s) and abs(self.e[1] < s) and abs(self.e[2] < s)
    
def dot(u, v):
    return float(u.e[0]) * float(v.e[0]) + float(u.e[1]) * float(v.e[1]) + float(u.e[2]) * float(v.e[2])

def cross(u, v):
    return vec3(u.e[1] * v.e[2] - u.e[2] * v.e[1], u.e[2] * v.e[0] - u.e[0] * v.e[2], u.e[0] * v.e[1] - u.e[1] * v.e[0])

def unit_vector(v):
    return v / v.length() 
    
def randomInUnitSphere():
    while True:
        p = randomVector()
        if p.length_squared() < 1:
            return p

def randomUnitVector():
    return unit_vector(randomInUnitSphere())

def randomOnHemisphere(normal):
    onUnitSphere = randomUnitVector()
    if dot(onUnitSphere, normal) > 0:
        return onUnitSphere
    else:
        return -onUnitSphere

def randomVector():
    return vec3(random(), random(), random())

def randomInRange(min, max):
    return(vec3(randrange(min, max), randrange(min, max), randrange(min, max)))


def reflect(v, n):
    return v - (n * 2) * dot(v, n)