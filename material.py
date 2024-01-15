from abc import ABC, abstractmethod
from Vector import *
from Ray import ray

class Material(ABC):

    @abstractmethod
    def scatter(self, ray_in, hit_record, scattered):
        pass

class Lambertian(Material):
    def __init__(self, colour):
        self.albedo = colour
    
    def scatter (self, r, rec, attenuation, scattered):
        scatterDir = rec.normal + randomUnitVector()

        if scatterDir.nearZero():
            scatterDir = rec.normal

        self.scattered = ray(rec.p, scatterDir)
        self.attenuation = self.albedo

        return True
    
class Metal (Material):
    def __init__(self, colour, f):
        self.albedo = colour
        if f < 1: self.fuzz = f
        else: self.fuzz = 1

    def scatter(self, r, rec, attenuation, scattered):
        reflected = reflect(unit_vector(r.dir), rec.normal)
        scattered.orig = rec.p
        scattered.dir = reflected + randomUnitVector() * self.fuzz
        self.scattered = scattered
        self.attenuation = self.albedo
        return dot(scattered.dir, rec.normal) > 0
        