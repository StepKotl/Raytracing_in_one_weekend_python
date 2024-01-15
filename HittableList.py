from Hittable import *
from Vector import vec3
from sphere import sphere
from Interval import interval, universe, empty


class hittableList:
    def __init__(self):
        self.objects = []
        
    def clear(self):
        self.objects = []
    
    
    def add(self,obj):
        self.objects.append(obj)
        
    def hit(self, r, rayT, rec):
        temp_rec = HitRecord()
        hit_anything = False
        closestSoFar = rayT.max
        
        for obj in self.objects:
            if obj.hit(r, interval(rayT.min, closestSoFar), temp_rec):
                hit_anything = True
                closestSoFar = temp_rec.t
                rec = temp_rec
                
        return [hit_anything, rec]
            
    