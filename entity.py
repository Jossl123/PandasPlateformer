from sprite import Sprite
from box import Box
class Entity(Box, Sprite):
    def __init__(self, filename, frame_nb,x, y, w, h):
        Box.__init__(self, x, y, w, h)
        Sprite.__init__(self, filename, (w, h), frame_nb)