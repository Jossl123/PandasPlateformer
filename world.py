import pygame
from utils import *
from player import Player
from box import Box
from item import Item
from sprite import Sprite
from entity import Entity
from solidsprite import SolidSprite
from bamboo import Bamboo
class World:
    def __init__(self, surface):
        self.surface = surface
        self.player = Player()
        self.screen_offset = np.array((self.surface.get_width()/2, self.surface.get_height()/2))
        self.sprites = [
            Sprite(-300,-300,600,600,"images/background.png",1, -2.9),
            SolidSprite(-200, 50, 600, 100,0, 0, 600, 100,"images/floor.png", 1,),
            self.player
        ]
        # self.sprites.append(
        #     Bamboo(self.sprites[-1]))

    def draw(self):
        offset = self.player.get_position() * SCALE - self.screen_offset
        for sprite in self.sprites:
            sprite.draw_sprite(self.surface, offset)

    def update(self):
        self.manage_input()
        self.player.update(self.sprites[1])
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
    