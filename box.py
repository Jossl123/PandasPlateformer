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
        x1_rect1, y1_rect1 = self.collider.topleft
        x2_rect1, y2_rect1 = self.collider.bottomright

        x1_rect2, y1_rect2 = box.collider.topleft
        x2_rect2, y2_rect2 = box.collider.bottomright

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
