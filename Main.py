"""
This project was made with a cool website called "Ray Tracing in One Weekend"
https://raytracing.github.io/books/RayTracingInOneWeekend.html#citingthisbook/basicdata

The original project was written in C++, but as someone else had made the same raytracer in python,
I decided to give it a try. 

https://github.com/shiva-kannan/RayTracingInOneWeekend-Python


This raytracer uses a PPM file to generate images, which is formatted (in binary) like the following which is eventually read by 
the computer to create the actual image:

Filetype (P3)
diplayWidth displayHeight
maxColourVal (225)
R G B | R G B | R G B

The ppm Format defines each pixel in the image by it's RGB Value, so the last line shows an example of what 3 pixels look like
"""
from Vector import vec3
from sphere import sphere
from Camera import camera
from HittableList import hittableList
from material import *
import math

def run():
    
    world = hittableList()
    
    material_ground = Lambertian(vec3(0.8, 0.8, 0.0))
    material_center = Lambertian(vec3(0.1, 0.2, 0.5))
    material_left   = Metal(vec3(0.7, 0.3, 0.3), 0.0)
    material_right  = Metal(vec3(0.8, 0.6, 0.2), 0.0)

    world.add(sphere(vec3( 0.0, -100.5, -1.0), 100.0, material_ground))
    world.add(sphere(vec3( 0.0,    0.0, -1.0),   0.5, material_center))
    world.add(sphere(vec3(-1.0,    0.0, -1.0),   0.5, material_left))
    world.add(sphere(vec3(-1.0,    0.0, -1.0),  -0.4, material_left))
    world.add(sphere(vec3( 1.0,    0.0, -1.0),   0.5, material_right))
    
    cam = camera(16/9, 400, 100, 50, 100, vec3(-2, 2, 1), vec3(0, 0, -1), vec3(0, 1, 0))
    cam.render(world)

from playsound import playsound
run()

playsound(r'C:\Users\stepi\Desktop\Python Projects\School\School-Projects\Math_Project\YourRenderIsDone.mp3')