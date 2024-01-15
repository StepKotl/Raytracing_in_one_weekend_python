from Hittable import Hittable, HitRecord
from Interval import interval, universe, empty
from math import floor, inf, pi, radians, tan
from Vector import *
from Ray import ray, write_colour
import random
from material import Material

class camera():
    def __init__(self, aspectRatio = 1, imgWidth = 100, samplesPerPixel = 10, maxDepth = 10, vfov = 90, lookFrom = vec3(0, 0, 0), lookAt = vec3(0, 1, 0), vup = vec3(0, 1, 0)):
        self.aspectRatio = aspectRatio
        self.imgWidth = imgWidth
        self.samples_per_pixel = samplesPerPixel
        self.maxDepth = maxDepth
        self.vfov = vfov
        self.lookFrom = lookFrom
        self.lookAt = lookAt
        self.vup = vup
    
    def render(self, world):
        self.initialize()
        with open("Math_Project/picture.ppm", "wb+") as activeFile:
            
            # Start with writing the settings
            activeFile.write((f"{self.settings}\n").encode("ascii"))
            for h in range(self.imgHeight):

                for w in range(self.imgWidth):
                    # Progress Bar
                    print(f"Scanlines Remaining: {self.imgHeight - h - 1} | % Finished: {round(h * 100 / self.imgHeight)}% | Pixels Remaining in Scanline: {self.imgWidth - w - 1} | Scanline % Finished: {round(w * 100 / self.imgWidth)}%                        ", end = "\r")
                    
                    pixel_colour = vec3(0, 0, 0)

                    for i in range(self.samples_per_pixel):
                        r = self.get_ray(w, h)
                        pixel_colour += self.rayColour(r, self.maxDepth, world)
                               
                    # Write it into the file
                    write_colour(activeFile, pixel_colour, self.samples_per_pixel)

            
    def get_ray(self, i, j):
        # Find the centre of the current pixel
        pixelcentre = self.pixel00_loc + self.pixel_delta_u * i + self.pixel_delta_v * j
        pixelSample = pixelcentre + self.pixelSampleSquared()

        rayOrigin = self.cameraCentre
        rayDirection = pixelSample - rayOrigin
        return ray(rayOrigin, rayDirection)
        

    def pixelSampleSquared(self):
        px = random.random() - 0.5
        py = random.random() - 0.5
        return (self.pixel_delta_u * px) + (self.pixel_delta_v * py)
    
    def initialize(self):
        # Calculate Image Height
        imgHeight = int(floor(self.imgWidth / self.aspectRatio))
        if imgHeight < 1:
            imgHeight = 1

        # Determine some Camera Variables
        focalLengths = 1
        focalLength = (self.lookFrom - self.lookAt).length()


        theta = radians(self.vfov)
        print(theta)

        viewportHeight = focalLengths * 2 * tan(theta / 2)
        viewportWidth = viewportHeight * self.imgWidth/imgHeight
        cameraCentre = self.lookFrom

        w = unit_vector(self.lookFrom - self.lookAt)
        u = unit_vector(cross(self.vup, w))
        v = cross(w, u)

        # Size of the Main Viewport
        viewport_u = u * viewportWidth 
        viewport_v = -v * viewportHeight 

        # Pixel Deltas
        pixel_delta_u = viewport_u / self.imgWidth
        pixel_delta_v = viewport_v /imgHeight

        # Find the upperleft of the viewport to properly generate the image 
        vieport_upperleft = cameraCentre - (w * focalLength) - (viewport_u / 2) - (viewport_v / 2)
        pixel00_loc = vieport_upperleft + (pixel_delta_u + pixel_delta_v) * 0.5

        settings = (f"P3\n{self.imgWidth} {imgHeight}\n225\n")

        # self.something
        self.settings = settings
        self.pixel00_loc = pixel00_loc
        self.vieport_upperleft = vieport_upperleft
        self.pixel_delta_u = pixel_delta_u
        self.pixel_delta_v = pixel_delta_v
        self.viewport_v = viewport_v
        self.viewport_u = viewport_u
        self.u, self.v, self.w = u, v, w
        self.cameraCentre = cameraCentre
        self.viewportHeight = viewportHeight
        self.viewportWidth = viewportWidth
        self.focalLengths = focalLengths
        self.imgHeight = imgHeight
        

    
    def rayColour(self, r, depth, world):
        rec = HitRecord()
        ret = world.hit(r, interval(0.001, inf), rec)
        rec = ret[1]

        if depth <= 0:
            return vec3(0, 0, 0)

        if ret[0]:
            scattered = ray(vec3(), vec3())
            attenuation = vec3()
            test = rec.material.scatter(r, rec, attenuation, scattered)
            scattered = rec.material.scattered
            attenuation = rec.material.attenuation
            if test:
                return attenuation * self.rayColour(scattered, depth - 1, world)
            return vec3()

        unit_direction = unit_vector(r.dir)
        a = (unit_direction.y() + 1) * 0.5
        colourVariance = vec3(1, 1, 1) * (1 - a) + vec3(0.5, 0.7, 1) * a
        return colourVariance