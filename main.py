import pygame
from settings import *
from player import Player
# from bullet import Bullet
import math
from map import world_map
from ray_casting import ray_casting
from drawing import Drawing

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
sc_map = pygame.Surface((WIDTH // MAP_SCALE, HEIGHT // MAP_SCALE))
clock = pygame.time.Clock()
player = Player()
drawing = Drawing(sc, sc_map)
# bullets = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        # if pygame.key.get_pressed()[pygame.K_SPACE]:
        #     bullets.append(Bullet(player.pos, player.angle))

    player.movement()

    drawing.background(player.angle)
    drawing.world(player.pos, player.angle)
    drawing.fps(clock)
    drawing.mini_map(player)

    # pygame.draw.circle(sc, GREEN, (int(player.x), int(player.y)), 12)
    # pygame.draw.line(sc, GREEN, player.pos, (player.x + WIDTH * math.cos(player.angle),
    #                                          player.y + WIDTH * math.sin(player.angle)))
    # for bul in bullets:
    #     if -10 <= bul.x <= WIDTH + 10 and -10 <= bul.y <= HEIGHT + 10:
    #         pygame.draw.circle(sc, BLUE, bul.pos, bul.radius)
    #         bul.movement()
    #     else:
    #         bullets.remove(bul)


    pygame.display.flip()
    clock.tick()
