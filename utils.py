import numpy as np
import pygame
from math import *
BG = (0,100,0)
SCALE = 10
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
