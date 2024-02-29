#2. Create a (any) program  using pygame library and create a movie.

import pygame
import sys
import numpy as np


def point (x, y) :
    x = x
    y = y + delta_t*rain_speed_y # from the center
    return (x,y) # return as a pair, tuple

def render (x,y) :
    screen.fill(white)
    for i in range(10000):
        pygame.draw.line(screen, blue, (x[i], y[i]), (x[i], y[i]+10), 2)



# canvas size
width = 1080
height = 600

# making the canvas
screen = pygame.display.set_mode((width,height))

# predefined colors
white = pygame.Color('white')
blue = pygame.Color('blue')

# fill the screen with white color
screen.fill(white)

# update the display
pygame.display.update()

#FPS
clock = pygame.time.Clock()

#################################################
x = np.random.randint(low = 0, high = 1080, size = 10000)
y = np.random.randint(low = -6000, high = 0, size = 10000)
rain_speed_y = 10

delta_t = 1 # time gap, or time icrement

# count = 0 # counter for image saving

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT :
            sys.exit()

    # updating the position
    x,y = point(x, y)

    # count += 1

    # filename = "/Users/leejiuk1/Documents/lectureincau/3rd/1semester/computationalphysics/rain/rain_%04d.png" % (
    #     count)  # 4자리 숫자 0001,0002,0003,0004 ...
    # pygame.image.save(screen, filename)

    # rendering
    render(x,y)

    clock.tick(60)
    pygame.display.update()

