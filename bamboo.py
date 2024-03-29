from utils import *
from item import Item
class Bamboo(Item):
    def __init__(self,floor):
        super().__init__("./images/bamboo.png",(10,10), 2)
        self.height = 3
        self.collider = pygame.Rect(0,floor.collider.top-10*self.height,10,10*self.height)

    def draw(self, surface,to_screen_coord):
        x = self.collider.topleft[0]
        y = self.collider.topleft[1]
        for i in range(self.height):
            frame = 1 if i == 0 else 0
            print(to_screen_coord((x,y)))
            surface.blit(self.get_sprite(frame), to_screen_coord((x,y)))
            y += 10

