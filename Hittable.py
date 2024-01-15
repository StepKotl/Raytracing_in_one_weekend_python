from Ray import ray
from Vector import *

# Taken from:
# https://github.com/shiva-kannan/RayTracingInOneWeekend-Python/blob/277bbe861ce0661442fb1dfecb4a42cf693a3409/src/hittable.py
from abc import ABC, abstractmethod
from material import Material

class Hittable(ABC):

    @abstractmethod
    def hit(self, ray, rayT, hit_record):
        pass


class HitRecord:
    def __init__(self, t=0.0, p=vec3(0.0, 0.0, 0.0), normal=vec3(0.0, 0.0, 0.0), frontFace = bool()):
        self.t = t
        self.p = p
        self.normal = normal
        self.material = None
        self.frontFace = frontFace

    
    def setFaceNormal(self, r, outwardNormal):
        self.frontFace = dot(r.direction(), outwardNormal) < 0
        self.normal = outwardNormal if self.frontFace else -outwardNormal
        