import pygame
import sys
import numpy as np
from numpy.linalg import *
from math import *

# take an angle and return two coordinates (x,y) shifted by the center of the screen
def point (angle1, angle2) :
    x1 = scale*l1 * sin(angle1) + x_center # from the center
    y1 = scale*l1 * cos(angle1) + y_center # from the center

    x2 = x1 + scale*l2 * sin(angle2)
    y2 = y1 + scale*l2 * cos(angle2)
    return (x1,y1), (x2,y2) # return as a pair, tuple

# rendering the object tin the screen
def render (pxy1, pxy2) :
    screen.fill(white)
    pygame.draw.line(screen, black, (x_center, y_center), (pxy1[0], pxy1[1]), 2)
    pygame.draw.circle(screen, green, (pxy1[0], pxy1[1]), 10)

    pygame.draw.line(screen, black, (pxy1[0], pxy1[1]), (pxy2[0], pxy2[1]), 2)
    pygame.draw.circle(screen, green, (pxy2[0], pxy2[1]), 10)

    return (pxy2[0], pxy2[1])

# Slope(G) function
def G (t, y) :
    F[0] = -1 * m2 * l2 * y[1]*y[1] * sin(y[2] - y[3]) - (m1 + m2)*g*sin(y[2])
    F[1] = l1 * y[0] * y[0] * sin(y[2] - y[3]) - g * sin(y[3])
    F[2] = y[0]
    F[3] = y[1]

    L = np.array([
        [(m1 + m2) * l1, m2 * cos(y[2] - y[3]), 0.0, 0.0],
        [l1 * cos(y[2] - y[3]), l2, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0]
    ])

    return inv(L).dot(F)

# RK4 method
def RK4 (t, y, delta_t):

    k1 = G(t, y)
    k2 = G(t + 0.5 * delta_t, y + 0.5 * delta_t * k1)
    k3 = G(t + 0.5 * delta_t, y + 0.5 * delta_t * k2)
    k4 = G(t + delta_t, y + 1.0 * delta_t * k3)

    return k1/6.0 + 2.0 * k2/6.0 + 2.0 * k3/6.0 + k4/6.0

# canvas size
width = 1080
height = 600
s = 10 # scale
# making the canvas
screen = pygame.display.set_mode((width,height))

# predefined colors
white = pygame.Color('white')
black = pygame.Color('black')
green = pygame.Color('green')
star = (191,241,251)

# fill the screen with white color
screen.fill(white)
trace = screen.copy()
# update the display
pygame.display.update()

#clock for frames
clock = pygame.time.Clock()
scale = 100 #length in pixel

#location of origin
x_center = width*0.5
y_center = height*0.5



# block from RK4 simple pendulum
##########################################################################
g = 9.8 #gravity const
l1 = 1.0 # lenth
l2 = 1.0
m1 = 100000000000
m2 = 1.0
t = 0.0 # incresing time
delta_t = 0.01 # time gap, or time icrement

y = np.array( [0.0, 0.0, 0.0, 1.0 ] ) # 4 x 1 vector [d-theta 1, d-theta 2, theta1, theta2]
F = np.array( [ 0.0, 0.0, 0.0, 0.0] ) # not a force
###########################################################################

# count = 0 # counter for image saving

# update the display
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT :
            sys.exit()

    # updating the position
    xy1,xy2 = point(y[2], y[3])

    # count += 1
    prev_point = render(xy1, xy2)

    # rendering
    render(xy1,xy2)

    # block from RK4 simple pendulum
    ###################################################################
    t += delta_t
    y = y + delta_t*RK4(t, y, delta_t)
    ##################################################################

    clock.tick(60)
    pygame.display.update()
