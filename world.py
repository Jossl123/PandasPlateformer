import pygame
from utils import *
from player import Player
from box import Box
from item import Item
from sprite import Sprite
from entity import Entity
class World:
    def __init__(self, surface):
        self.surface = surface
        self.player = Player()
        self.screen_offset = np.array((self.surface.get_width()/2, self.surface.get_height()/2))
        self.scale = 2
        self.background = Sprite("images/background.png", (600,600), -2.9)
        self.floor = Entity("images/floor.png", -200, 50, 600, 100)
        self.bamboo = Item("images/bamboo.png", self.floor.collider)

    def draw(self):
        self.surface.blit(self.background.get_sprite(),self.to_screen_coord((-300,-300), self.background.z_index))
        self.surface.blit(self.floor.get_sprite(),self.to_screen_coord(self.floor.collider.topleft))
        self.surface.blit(self.player.get_sprite(), self.to_screen_coord(self.player.collider.topleft))
        self.surface.blit(self.bamboo.get_sprite(), self.to_screen_coord(self.bamboo.collider.topleft))

    def update(self):
        self.manage_input()
        self.bamboo.update()
        self.player.update(self.floor)
        
        self.draw()

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
    
    def to_screen_coord(self, coord, z_index = 0):
        scale = SCALE * (1 + z_index/10)
        match type(coord):
            case pygame.Rect:
                res = coord.copy() 
                res.width*=scale
                res.height*=scale
                res.center = coord.center - self.player.get_position()
                res.center=(res.center[0]*scale+self.screen_offset[0],res.center[1]*scale+self.screen_offset[1])
                return res
            case _:
                return (coord - self.player.get_position()) * np.array((scale,scale)) + self.screen_offset 