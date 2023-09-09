import pygame
import numpy as np
class Entity():
    def __init__(self, x, y, w, h):
        self.position = pygame.Rect(x,y,w,h)
        self.acceleration = np.array([0,0])
    def get_width(self):
        return self.collider.width
    def get_height(self):
        return self.collider.height
    def get_position(self):
        return np.array((self.position.center[0],self.position.center[1]))