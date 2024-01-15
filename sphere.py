from Hittable import Hittable
from Vector import *
import math
from Interval import interval, universe, empty

class sphere(Hittable):
    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material
        
    def hit(self, r, rayT, rec):
        oc = r.origin() - self.center
        a = dot(r.dir, r.dir)
        b = dot(oc, r.dir)
        c = dot(oc, oc) - self.radius ** 2
        
        discriminant = b ** 2 - a * c
        if discriminant > 0.0:
            
            temp = (-b - math.sqrt(discriminant)) / a
            if rayT.surrounds(temp):
                rec.t = temp
                rec.p = r.at(rec.t)
                rec.normal = (rec.p - self.center) / self.radius
                rec.material = self.material
                return True
            
            temp = (-b + math.sqrt(discriminant)) / a
            if rayT.surrounds(temp):
                rec.t = temp
                rec.p = r.at(rec.t)
                rec.normal = (rec.p - self.center) / self.radius
                rec.material = self.material
                return True
        else:
            return False