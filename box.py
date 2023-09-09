from utils import *
from entity import Entity
class Box(Entity): #absract
    def __init__(self, x, y, w, h, x1=None, y1=None, w1=None, h1=None):
        if not hasattr(self, 'position'):
            Entity.__init__(self,x,y,w,h)
        if x1 is None:
            self.collider = pygame.Rect(0, 0, w, h)
        else:
            self.collider = pygame.Rect(x1, y1, w1, h1)
        self.velocity = np.array([0,0])
        self.acceleration = np.array([0,0])

    def get_velocity(self):
        return self.velocity
    
    def distance(self, box):
        x1_rect1, y1_rect1 = self.position.topleft[0] + self.collider.topleft[0],self.position.topleft[1] + self.collider.topleft[1]
        x2_rect1, y2_rect1 = x1_rect1 + self.collider.width, y1_rect1 + self.collider.height
        
        x1_rect2, y1_rect2 = box.position.topleft[0] + box.collider.topleft[0],box.position.topleft[1] + box.collider.topleft[1]
        x2_rect2, y2_rect2 = x1_rect2 + box.collider.width, y1_rect2 + box.collider.height

        if x2_rect1 < x1_rect2:  # rect1 is to the left of rect2
            x_dist = x1_rect2 - x2_rect1
        elif x1_rect1 > x2_rect2:  # rect1 is to the right of rect2
            x_dist = x1_rect1 - x2_rect2
        else:  # rect1 and rect2 overlap in x-axis
            x_dist = 0

        if y2_rect1 < y1_rect2:  # rect1 is above rect2
            y_dist = y1_rect2 - y2_rect1
        elif y1_rect1 > y2_rect2:  # rect1 is below rect2
            y_dist = y1_rect1 - y2_rect2
        else:  # rect1 and rect2 overlap in y-axis
            y_dist = 0

        return (x_dist ** 2 + y_dist ** 2) ** 0.5  # Euclidean distance

    def collide(self, box):
        x1_rect1, y1_rect1 = self.position.topleft[0] + self.collider.topleft[0],self.position.topleft[1] + self.collider.topleft[1]
        x1_rect2, y1_rect2 = box.position.topleft[0] + box.collider.topleft[0],box.position.topleft[1] + box.collider.topleft[1]

        new_self = Box(x1_rect1,y1_rect1,self.collider.width, self.collider.height)
        new_box = Box(x1_rect2,y1_rect2,box.collider.width, box.collider.height)
        return new_self.collider.colliderect(new_box.collider)

    def check_box_collision_path(self, box2, dir):
        points_nb = np.linalg.norm(dir)*10
        box1 = self
        box1_pos = self.get_position()
        i = 0
        a = 0
        new_box = box1
        prev_distance = box2.distance(new_box)
        while i < points_nb and prev_distance >= box2.distance(new_box):
            a = (i/points_nb)
            x = box1_pos[0] + dir[0] * a
            y = box1_pos[1] + dir[1] * a
            new_box = Box(x-box1.get_width()/2,y-box1.get_height()/2,box1.get_width(), box1.get_height())
            if new_box.collide(box2):
                return (max(i-1,0)/points_nb)
            i+=1
        return 1