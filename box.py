from utils import *
class Box:
    def __init__(self, x, y, w, h):
        self.collider = pygame.Rect(x, y, w, h)
        self.velocity = np.array([0,0])
    
    def get_position(self):
        return np.array((self.collider.center[0], self.collider.center[1]))

    def get_velocity(self):
        return self.velocity
    
    def get_width(self):
        return self.collider.width
    
    def get_height(self):
        return self.collider.height
    
    def distance(self, box):
        self_center = np.array(self.collider.center)
        box_center = np.array(box.collider.center)
        center_distance = np.linalg.norm(self_center - box_center)
        
        width_diff = self.collider.width + box.collider.width
        height_diff = self.collider.height + box.collider.height
        width_height_distance = max(0, center_distance - 0.5 * (width_diff + height_diff))
        
        return width_height_distance