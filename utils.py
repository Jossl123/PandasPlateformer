import numpy as np
import pygame
from math import *
from box import Box
BG = (0,100,0)
SCALE = 3
def closest_point_on_line(line_point1, line_point2, point_p):
    line_direction = (line_point2[0] - line_point1[0], line_point2[1] - line_point1[1])
    line_length_squared = line_direction[0] ** 2 + line_direction[1] ** 2

    if line_length_squared == 0:
        # If the line is just a point, return that point
        return line_point1

    point_to_line_start = (point_p[0] - line_point1[0], point_p[1] - line_point1[1])

    # Calculate the projection of point_to_line_start onto the line
    projection_scalar = (point_to_line_start[0] * line_direction[0] + point_to_line_start[1] * line_direction[1]) / line_length_squared

    # Check if the projection is beyond the endpoints of the line segment
    projection_scalar = max(0, min(1, projection_scalar))

    # Calculate the coordinates of the closest point on the line
    closest_point = (line_point1[0] + projection_scalar * line_direction[0],
                     line_point1[1] + projection_scalar * line_direction[1])

    return closest_point

def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       print("line do not intersect")
       return False

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return np.array([x, y])

def get_inside_dist_center_to_perimeter_rect(v, rect):
    v = np.array([abs(v[0]), abs(v[1])])
    maxDist = rect.get_width()*rect.get_height()
    l = (rect.center, (rect.center[0] + v[0] * (maxDist+1), rect.center[1] + v[1] * (maxDist+1)))
    l1 = ((0,rect.get_height()), (rect.get_width(),rect.get_height()))
    l2 = ((rect.get_width(),0), (rect.get_width(),rect.get_height()))
    i1 = line_intersection(l,l1)
    i2 = line_intersection(l,l2)
    if isinstance(i1, np.ndarray):
        return np.linalg.norm(np.array([i1[0] - rect.center[0], i1[1] - rect.center[1]]))
    if isinstance(i1, np.ndarray):
        return np.linalg.norm(np.array([i2[0] - rect.center[0], i2[1] - rect.center[1]])) 
    else:return maxDist

def check_box_collision_path(box1, box2, dir):
    points_nb = np.linalg.norm(dir)*100
    box1_pos = box1.get_position()
    i = 0
    a = 0
    new_box = box1
    prev_distance = new_box.distance(box2)
    while i < points_nb and prev_distance >= new_box.distance(box2):
        a = (i/points_nb)
        x = box1_pos[0] + dir[0] * a
        y = box1_pos[1] + dir[1] * a
        new_box = Box(x-box1.get_width()/2,y-box1.get_height()/2,box1.get_width(), box1.get_height())
        if new_box.collider.colliderect(box2.collider):
            return (max(i-1,0)/points_nb)
        i+=1
    return 1