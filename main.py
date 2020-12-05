import pygame
from settings import *
from player import Player
from bullet import Bullet
from map import game_map_init
import math

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
player = Player()
bullets = []
walls = game_map_init()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            bullets.append(Bullet(player.pos, player.angle))

    player.movement()
    sc.fill(BLACK)

    pygame.draw.circle(sc, GREEN, player.pos, 20)
    pygame.draw.line(sc, GREEN, player.pos, (player.x + WIDTH * math.cos(player.angle),
                                             player.y + WIDTH * math.sin(player.angle)))
    for bul in bullets:
        if -10 <= bul.x <= WIDTH + 10 and -10 <= bul.y <= HEIGHT + 10:
            pygame.draw.circle(sc, BLUE, bul.pos, bul.radius)
            bul.movement()
        else:
            bullets.remove(bul)
    for wall in walls:
        pygame.draw.rect(sc, WHITE, (wall[0], wall[1], WALL_WIDTH, WALL_WIDTH), 2)

    pygame.display.flip()
    clock.tick(FPS)
