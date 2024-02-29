import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import *
from math import *

# Slope(G) function
def G (t, y) :
    F[0] = -g*sin(y[1]) # -g sin(theta)
    # approximation : F[0] = - g * y[1]
    F[1] = y[0] # angular speed
    return inv_L.dot(F)

# RK4 method
def RK4 (t, y, delta_t):

    k1 = G(t, y)
    k2 = G(t + 0.5 * delta_t, y + 0.5 * delta_t * k1)
    k3 = G(t + 0.5 * delta_t, y + 0.5 * delta_t * k2)
    k4 = G(t + delta_t, y + 1.0 * delta_t * k3)

    return 1/6 * k1 + 2/6 * k2 + 2/6 * k3 + 1/6 * k4

g = 9.8 #gravity const
l = 1.0 # lenth

omega = sqrt(g/l)

delta_t = 0.01
time = np.arange(0, 5, delta_t) # zero to 5 sec by 0.01 imcrement

theta0 = 50.0 * pi / 180 # this is radian
thetadot0 = 0 # of course this is too

y = np.array( [ thetadot0, theta0] ) # vector [angular velocity, angle]

L = np.array( [ [ l, 0.0 ], [ 0.0, 1.0 ]])
F = np.array( [ 0.0, 0.0] ) # not a force

# result
Angle = [] # angle
AS = [] # anlgular speed

inv_L = inv(L)

for t in time :
    y = y + delta_t * RK4 (t, y, delta_t)
    AS.append(y[0])
    Angle.append(y[1])




import pygame
import sys
from math import *

pygame.init()

background = pygame.mixer.Sound("1-02 Castle on the Hill.mp3")
background.play(-1) #계속 재생

# button = pygame.mixer

def point (angle) :
    x = l * sin(angle) + x_center
    y = l * cos(angle) + y_center
    return (x,y)

def render (xy) :
    screen.fill(white)
    pygame.draw.line(screen, black, (x_center, y_center), (xy[0], xy[1]), 2)
    pygame.draw.circle(screen, green, (xy[0], xy[1]), 10)

    clock.tick(100)  # runs one frame per 1sec
    pygame.display.update()


# angle
angle = 0.0 # initial angle

# canvas size
width = 1080
height = 600

# making the canvas
screen = pygame.display.set_mode((width,height))

# predefined colors
white = pygame.Color('white')
black = pygame.Color('black')
green = pygame.Color('green')

# fill the screen with white color
screen.fill(white)

# update the display
pygame.display.update()

#clock for frames
clock = pygame.time.Clock()

l = 200 #length
a = 0.0 #initial angle

#location of origin
x_center = width*0.5
y_center = height*0.5

count = 0

# update the display
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT :
            sys.exit()

    # updating the position
    xy = point(angle)
    angle = Angle[count]
    # a += 1  # circular motion
    count += 1




    # rendering
    render(xy)


    # filename = "/Users/leejiuk1/Documents/lecture in cau/3학년/1학기/전산물리학/pendulum/pendulum_%04d.png" % (count) #4자리 숫자 0001,0002,0003,0004 ...
    # pygame.image.save(screen,filename)


    # rendering
    # screen.fill(white)
    # pygame.draw.line(screen, black, (300,200),(300,300),2)
    # pygame.draw.circle(screen, black, (300,300), 10)
    # pygame.display.update()

