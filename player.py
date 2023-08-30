import numpy as np
import pygame
class Player:
    def __init__(self):
        self.collide_box = pygame.Rect(-30,-60,60,60)
        self.speed = 5

    def move(self, dir):
        self.collide_box.center+=dir*self.speed