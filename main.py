import pygame
from settings import *
from player import Player
from bullet import Bullet
import math

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
player = Player()
bullets = []

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

    pygame.display.flip()
    clock.tick(FPS)
