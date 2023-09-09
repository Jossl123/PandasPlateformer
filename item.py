from utils import *
from sprite import Sprite
class Item(Sprite):
    def __init__(self, collider, filename, bounds,frame_nb):
        self.collider = collider
        super().__init__(filename, self.collider, frame_nb)

    def update(self):
        pass
