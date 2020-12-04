from settings import *
import math


class Bullet:
    def __init__(self, bullet_pos, bullet_angle):
        self.x, self.y = bullet_pos
        self.angle = bullet_angle
        self.radius = 5

    @property
    def pos(self):
        return (self.x, self.y)

    def movement(self):
        self.x += bullet_speed * math.cos(self.angle)
        self.y += bullet_speed * math.sin(self.angle)
