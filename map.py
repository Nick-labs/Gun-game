from settings import *


def game_map_init():
    game_map = """WWWWWWWWWWWW
                  W..........W
                  W.WWW...WW.W
                  W...W...W..W
                  W.......W..W
                  W..WWW.....W
                  W..W.......W
                  WWWWWWWWWWWW"""

    walls = []

    for j, row in enumerate(game_map.split()):
        for i, letter in enumerate(row):
            if letter == 'W':

    return walls
