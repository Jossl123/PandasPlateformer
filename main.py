import pygame,sys
from utils import *
from world import World
from pygame.locals import *

flags =  DOUBLEBUF 
pygame.init()
surface = pygame.display.set_mode((16*100,9*100),flags,32)
pygame.display.set_caption('Game')
clock = pygame.time.Clock()
world = World(surface)
while True:
    surface.fill(BG)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    world.update()

    pygame.display.update()
    clock.tick(60)
