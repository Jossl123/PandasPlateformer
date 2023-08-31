from box import Box
from sprite import Sprite
from utils import *
import pygame
class Player(Box, Sprite):
    def __init__(self):
        Box.__init__(self,-10,-20,20,20)
        Sprite.__init__(self,"images/idle.png",(20,20),2)
        self.speed = 5
        self.acceleration = np.array([0,0.981*0.4])
        self.touching_floor = False
        self.idle_sprite_sheet = pygame.image.load("images/idle.png").convert_alpha()

    def move(self, dir):
        self.acceleration[0] = dir[0]
    
    def get_sprite(self):
        frame = int(pygame.time.get_ticks()/500)%2
        return Sprite.get_sprite(self,frame)
    
    def update(self, box):
        self.velocity = self.velocity + self.acceleration
        self.velocity[0] = min(self.speed,max(-self.speed, self.velocity[0]))
        collision = self.check_box_collision_path(box, self.velocity)
        self.touching_floor = self.distance(box) == 0
        self.velocity*=collision
        self.collider.center+=self.velocity
        self.velocity*=0.99