from solidsprite import SolidSprite
from utils import *
import pygame
class Player(SolidSprite):#should be an entity
    def __init__(self):
        super().__init__(-10,-20,20,20,0,0,20,20,"images/idle.png",2)
        self.speed = 5
        self.acceleration = np.array([0,0.981*0.4])
        self.touching_floor = False
        self.idle_sprite_sheet = pygame.image.load("images/idle.png").convert_alpha()

    def move(self, dir):
        self.acceleration[0] = dir[0]
    
    def get_frame(self):return int(pygame.time.get_ticks()/500)%2
    
    def update(self, box):
        self.velocity = self.velocity + self.acceleration
        self.velocity[0] = min(self.speed,max(-self.speed, self.velocity[0]))
        collision = self.check_box_collision_path(box, self.velocity)
        self.touching_floor = self.distance(box) == 0
        self.velocity*=collision
        self.position.center+=self.velocity
        self.velocity*=0.99