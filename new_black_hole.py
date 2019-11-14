'''
    It's a black hole!!
'''

'''
libraries
'''
from math import *
import pygame
import random


#display size || width: 320, height: 240
screen = pygame.display.set_mode((320,240))

#program doesn't stop
running = 1

#radius standard
radius = 70

#speed to create new circle
moveSpeed = 0.15

#constructor class
class Dot:

    def __init__(self, x, y, color, speed, surface):
        self.x = x
        self.y = y
        self.color = color
        self.speed = speed
        self.surface = surface

        self.originX = x
        self.originY = y
        self.angle = 0

    '''
    class that draw circle
    [-] gets the display size
    [-] color of the circle
    [-] coordinates x and y
    [-] circle size
    '''
    def drawing(self):
        pygame.draw.circle(self.surface, self.color, (self.x, self.y), 3)

    #class that update the data
    def updating(self):
        self.angle += self.speed
        self.x = self.originX + radius * sin(self.angle/360)
        self.y = self.originY + radius * cos(self.angle/360)

#class that creates the dot/points in the screen
def array(num):
    arr = []
    for i in range(0, num):
        d = Dot(120 + random.uniform(0,num), 100 + random.uniform(0,num), (255,125,0), random.uniform(0,5), screen)
        #append() method appends a passed obj into the existing list
        arr.append(d)

    return arr

#create how many circles have, in this case, between 50 and 70
dotQuantity = array(random.randrange(50))

#while program doesn't stop
while running:
    #gets a single event from the queue and it's going to appear in the terminal
    event =  pygame.event.poll()
    #if the user clicks 'x' on pygame screen
    if event.type == pygame.QUIT:
        running = 0

    #RGB
    screen.fill((0, 0, 0))

    for i in dotQuantity:
        i.updating()
        i.drawing()

    #Optimized function version of pygame.display.flip() for software displays
    pygame.display.update()
