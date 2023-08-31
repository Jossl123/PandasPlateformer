from utils import *
from sprite import Sprite
class Item(Sprite):
    def __init__(self, filename, bounds,frame_nb):
        super().__init__(filename, bounds, frame_nb)

    def update(self):
        pass
