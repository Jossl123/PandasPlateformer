from utils import *
class Sprite:
    def __init__(self,filename, bounds):
        self.sprite_sheet = pygame.image.load(filename).convert_alpha()
        self.image_bounds = bounds
    def get_sprite(self, frame=0):
        image = pygame.Surface((self.image_bounds[0], self.image_bounds[1])).convert_alpha()
        image.blit(self.sprite_sheet, (0,0), ((frame * self.image_bounds[0]), 0, self.image_bounds[0], self.image_bounds[1]))
        image = pygame.transform.scale(image, (self.image_bounds[0]*SCALE, self.image_bounds[1]*SCALE))
        image.set_colorkey((255,0,0))
        return image
    