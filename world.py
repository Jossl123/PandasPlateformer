import pygame
import numpy as np
from player import Player
class World:
    def __init__(self, surface):
        self.surface = surface
        self.player = Player()
        self.screen_offset = np.array((self.surface.get_width()/2, self.surface.get_height()/2))
        
    def update(self):
        self.manage_input()
        pygame.draw.rect(self.surface, (255,0,0), self.to_screen_coord(self.player.collide_box))

    def manage_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_q]:
            self.player.move(np.array((-1,0)))
        if keys[pygame.K_RIGHT]or keys[pygame.K_d]:
            self.player.move(np.array((1,0)))
        if keys[pygame.K_DOWN]or keys[pygame.K_s]:
            pass
        if keys[pygame.K_UP]or keys[pygame.K_z]:
            pass
    
    def to_screen_coord(self, coord):
        match type(coord):
            case pygame.Rect:
                return pygame.Rect(coord.x + self.screen_offset[0],coord.y + self.screen_offset[1], coord.width, coord.height)
            case _:
                return 