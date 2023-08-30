from box import Box
from utils import *
import pygame
class Player(Box):
    def __init__(self):
        super().__init__(-10,-20,20,20)
        self.image_bounds = (20,20)
        self.speed = 5
        self.acceleration = np.array([0,0.981*0.4])
        self.touching_floor = False
        self.idle_sprite_sheet = pygame.image.load("images/idle.png").convert_alpha()

    def move(self, dir):
        self.acceleration[0] = dir[0]
    
    def get_sprite(self):
        frame = int(pygame.time.get_ticks()/500)%2
        image = pygame.Surface((self.image_bounds[0], self.image_bounds[1])).convert_alpha()
        image.blit(self.idle_sprite_sheet, (0,0), ((frame * self.image_bounds[0]), 0, self.image_bounds[0], self.image_bounds[1]))
        image = pygame.transform.scale(image, (self.image_bounds[0]*SCALE, self.image_bounds[1]*SCALE))
        image.set_colorkey((255,0,0))
        return image
    
    def update(self, box):
        self.velocity = self.velocity + self.acceleration
        self.velocity[0] = min(self.speed,max(-self.speed, self.velocity[0]))
        collision = check_box_collision_path(self, box, self.velocity)
        self.touching_floor = self.distance(box) == 0
        self.velocity*=collision
        self.collider.center+=self.velocity