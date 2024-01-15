from Vector import vec3
from Interval import interval

colour = point3 = vec3
def write_colour (file, pixel_colour, samples_per_pixel):
    rgb = [pixel_colour.x(), pixel_colour.y(), pixel_colour.z()]

    for i in range(len(rgb)):
        rgb[i-1] = rgb[i-1] * 1 / samples_per_pixel

    for i in range(len(rgb)):
        rgb[i-1] = linearToGamma(rgb[i-1])

    intensity = interval(0, 0.999)
    file.write((f"{intensity.clamp(rgb[0])*255.99} {intensity.clamp(rgb[1])*255.99} {intensity.clamp(rgb[2])*255.99}\n").encode("ascii"))

def linearToGamma(LinearCommponent):
    from math import sqrt
    return sqrt(LinearCommponent)

class ray:
    def __init__(self,origin,direction):
        self.orig = origin
        self.dir = direction

    def origin (self):
        return self.orig

    def direction (self):
        return self.dir
    
    def at(self,t):
        return self.orig + (self.dir * t)