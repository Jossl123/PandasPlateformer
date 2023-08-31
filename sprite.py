from utils import *
class Sprite:
    def __init__(self, filename, bounds,z_index = 0,transparent_color = (255,0,0)):
        self.sprite_sheet = pygame.image.load(filename).convert_alpha()
        self.image_bounds = bounds
        self.z_index = z_index
        self.transparent_color =transparent_color

    def get_sprite(self, frame=0):
        image = pygame.Surface((self.image_bounds[0], self.image_bounds[1])).convert_alpha()
        image.blit(self.sprite_sheet, (0,0), ((frame * self.image_bounds[0]), 0, self.image_bounds[0], self.image_bounds[1]))
        image = pygame.transform.scale(image, (self.image_bounds[0]*SCALE, self.image_bounds[1]*SCALE))
        image.set_colorkey(self.transparent_color)
        return image