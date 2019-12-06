'''
    It's a black hole!!
'''

#libraries
from math import *
import pygame
import random

#display size || width: 320, height: 240
screen = pygame.display.set_mode((320, 240))

#program doesn't stop
running = 1

#radiu standard
RADIUS = 55

#speed to create new circle
MOVE_SPEED = 0.15

#constructor class
class Dot:

    def __init__(self, x, y, color, speed, surface):
        self.x = x
        self.y = y
        self.origin_x = x
        self.origin_y = y
        self.color = color
        self.surface = surface
        self.angle = 0
        self.speed = speed

    '''
    class that draw circle
    [-] gets the display size
    [-] color of the circle
    [-] coordinates x and y
    [-] circle size
    '''
    def draw(self):
        pygame.draw.circle(self.surface, self.color, (self.x, self.y), 3)

    #class that update the data
    def update(self):
        #print ("[-] angle: {0}".format(self.angle))

        self.angle += self.speed

        # update the position x and y
        self.x = self.origin_x + RADIUS * sin(self.angle/360)
        self.y = self.origin_y + RADIUS * cos(self.angle/360)

#class that saves the values on an array
def create_space(num):
    l = []
    for i in range(0, num):
        d = Dot(120 + random.uniform(0,num), 100 + random.uniform(0,num), (255,125,0), random.uniform(0,5), screen)
        #append() method appends a passed obj into the existing list
        l.append(d)

    return l

#create how many circles have, in this case, between 50 and 70
dot_list = create_space(random.randrange(50,70))

#while program doesn't stop
while running:
     #gets a single event from the queue and it's going to appear in the terminal
     event = pygame.event.poll()
     if event.type == pygame.QUIT:
         running = 0

     #RGB
     screen.fill((0, 0, 0))


     for i in dot_list:
        i.update()
        i.draw()

     #Optimized function version of pygame.display.flip() for software displays
     pygame.display.update()
