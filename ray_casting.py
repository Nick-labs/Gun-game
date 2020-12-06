import pygame
from settings import *
from map import world_map
import math


def ray_casting(sc, player_pos, player_angle):
    cur_angle = player_angle - HALF_FOV
    xo, yo = player_pos
    for ray in range(NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)
        for depth in range(0, MAX_DEPTH, 10):
            x = xo + depth * cos_a
            y = yo + depth + sin_a
            pygame.draw.line(sc, DARKGRAY, player_pos, (x, y), 2)
        cur_angle += DELTA_ANGLE
