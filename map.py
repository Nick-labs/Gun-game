from settings import *


text_map = """WWWWWWWWWWWW
              W.W...W....W
              W.W.W.W.WW.W
              W.W.WWW.W..W
              W.W.....W..W
              W.W..W..W.WW
              W....W.....W
              WWWWWWWWWWWW"""

world_map = set()

for j, row in enumerate(text_map.split()):
    for i, char in enumerate(row):
        if char == 'W':
            world_map.add((i * TILE, j * TILE))
