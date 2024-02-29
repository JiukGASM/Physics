import pygame
import sys
import numpy as np
from numpy.linalg import *
from math import *

# take an angle and return two coordinates (x,y) shifted by the center of the screen
def point (angle) :
    x = scale * sin(angle) + x_center # from the center
    y = scale * cos(angle) + y_center # from the center
    return (x,y) # return as a pair, tuple

# rendering the object tin the screen
def render (xy) :
    screen.fill(white)
    pygame.draw.line(screen, black, (x_center, y_center), (xy[0], xy[1]), 2)
    pygame.draw.circle(screen, green, (xy[0], xy[1]), 10)

# Slope(G) function
def G (t, y) :
    F[0] = -g*sin(y[1]) # -g sin(theta)
    F[1] = y[0] # angular speed
    return inv_L.dot(F)

# RK4 method
def RK4 (t, y, delta_t):

    k1 = G(t, y)
    k2 = G(t + 0.5 * delta_t, y + 0.5 * delta_t * k1)
    k3 = G(t + 0.5 * delta_t, y + 0.5 * delta_t * k2)
    k4 = G(t + delta_t, y + 1.0 * delta_t * k3)

    return 1/6 * k1 + 2/6 * k2 + 2/6 * k3 + 1/6 * k4

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
scale = 200 #length in pixel

#location of origin
x_center = width*0.5
y_center = height*0.5



# block from RK4 simple pendulum
##########################################################################
g = 9.8 #gravity const
l = 1.0 # lenth
t = 0.0 # incresing time
delta_t = 0.01 # time gap, or time icrement

theta0 = 179 * pi / 180 # this is radian
thetadot0 = 0 # of course this is too

y = np.array( [ thetadot0, theta0] ) # vector [angular velocity, angle]
L = np.array( [ [ l, 0.0 ], [ 0.0, 1.0 ]])
F = np.array( [ 0.0, 0.0] ) # not a force

inv_L = inv(L)
###########################################################################

# count = 0 # counter for image saving

# update the display
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT :
            sys.exit()

    # updating the position
    xy = point(y[1]) # angle goes in and (x,y) comes out

    # count += 1

    # rendering
    render(xy)

    # block from RK4 simple pendulum
    ###################################################################
    t += delta_t
    y = y + delta_t*RK4(t, y, delta_t)
    ##################################################################

    clock.tick(100)
    pygame.display.update()
