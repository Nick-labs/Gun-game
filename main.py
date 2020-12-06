import pygame
from settings import *
from player import Player
# from bullet import Bullet
import math
from map import world_map
from ray_casting import ray_casting

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
player = Player()
# bullets = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        # if pygame.key.get_pressed()[pygame.K_SPACE]:
        #     bullets.append(Bullet(player.pos, player.angle))

    player.movement()
    sc.fill(BLACK)

    pygame.draw.rect(sc, BLUE, (0, 0, WIDTH, HALF_HEIGHT))
    pygame.draw.rect(sc, BROWN, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    ray_casting(sc, player.pos, player.angle)

    # pygame.draw.circle(sc, GREEN, (int(player.x), int(player.y)), 12)
    # pygame.draw.line(sc, GREEN, player.pos, (player.x + WIDTH * math.cos(player.angle),
    #                                          player.y + WIDTH * math.sin(player.angle)))
    # for bul in bullets:
    #     if -10 <= bul.x <= WIDTH + 10 and -10 <= bul.y <= HEIGHT + 10:
    #         pygame.draw.circle(sc, BLUE, bul.pos, bul.radius)
    #         bul.movement()
    #     else:
    #         bullets.remove(bul)
    # for x, y in world_map:
    #     #     pygame.draw.rect(sc, DARKGRAY, (x, y, TILE, TILE), 2)

    pygame.display.flip()
    clock.tick(FPS)
