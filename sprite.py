from entity import Entity
from utils import *
class Sprite(Entity):
    def __init__(self,x,y,w,h,filename,frame_nb,z_index=0,transparent_color=(255,0,0)):
        super().__init__(x,y,w,h)
        self.z_index = z_index
        self.sprite_sheet = pygame.image.load(filename).convert_alpha()
        self.transparent_color = transparent_color
        self.frames = []
        for i in range(frame_nb):
            image = pygame.Surface((self.position.width, self.position.height)).convert_alpha()
            image.blit(self.sprite_sheet, (0,0), ((i * self.position.width), 0, self.position.height, self.position.height))
            image = pygame.transform.scale(image, (self.position.width*SCALE, self.position.height*SCALE))
            image.set_colorkey(self.transparent_color)
            self.frames.append(image)

    def draw_sprite(self, surface, offset):
        if hasattr(self, "collider"):
            surface.blit(self.frames[self.get_frame()], self.to_screen_coord(self.collider.topleft, offset))
        else:
            surface.blit(self.frames[self.get_frame()], self.to_screen_coord(self.position.topleft, offset))

    def get_frame(self):return 0
    
    def to_screen_coord(self, coord, offset):
        scale = SCALE * (1 + self.z_index/10)
        match type(coord):
            case pygame.Rect:
                res = coord.copy() 
                res.width*=scale
                res.height*=scale
                res.center = coord.center
                res.center=(res.center[0]*scale-offset[0],res.center[1]*scale-offset[1])
                return res
            case _:
                return coord * np.array((scale,scale)) - offset