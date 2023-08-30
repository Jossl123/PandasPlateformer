import pygame
from utils import *
from player import Player
from box import Box
class World:
    def __init__(self, surface):
        self.surface = surface
        self.player = Player()
        self.screen_offset = np.array((self.surface.get_width()/2, self.surface.get_height()/2))
        self.scale = 2
        self.floor_box = Box(-200, 50, 400, 200)
        
    def update(self):
        self.manage_input()
        self.player.update(self.floor_box)
        pygame.draw.rect(self.surface,(240,0,0), self.to_screen_coord(self.floor_box.collider))
        self.surface.blit(self.player.get_sprite(), self.to_screen_coord(self.player.collider.topleft))

    def manage_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_q]:
            self.player.move(np.array((-1,0)))
        elif keys[pygame.K_RIGHT]or keys[pygame.K_d]:
            self.player.move(np.array((1,0)))
        else:self.player.acceleration[0] = 0
        if keys[pygame.K_DOWN]or keys[pygame.K_s]:
            pass
        if keys[pygame.K_UP] or keys[pygame.K_z]:
            if self.player.touching_floor:self.player.velocity[1] = -5
    
    def to_screen_coord(self, coord):
        match type(coord):
            case pygame.Rect:
                res = coord.copy()
                res.width*=SCALE
                res.height*=SCALE
                res.center = coord.center
                res.center=(res.center[0]*SCALE+self.screen_offset[0],res.center[1]*SCALE+self.screen_offset[1])
                return res
            case _:
                return coord *np.array((SCALE,SCALE))+ self.screen_offset