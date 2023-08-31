from utils import *
from sprite import Sprite
class Item(Sprite):
    def __init__(self, filename, frame_nb, floor):
        super().__init__(filename, (10,10), frame_nb)
        self.collider = pygame.Rect(0,floor.top-10,10,10)

    def update(self):
        pass
