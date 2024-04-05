import pygame as pg

fen_l = 1000
fen_h = 700
screen = pg.display.set_mode((fen_l, fen_h))

pin = pg.image.load("dessins/ping.png").convert_alpha()
ci = pg.image.load("dessins/water.png").convert_alpha()
ice = pg.image.load("dessins/iceberg.png").convert_alpha()
wallpaper = pg.image.load("dessins/wallpapers_neige.png").convert_alpha()
cache = pg.image.load("dessins/snow.png").convert_alpha()
ci1 = pg.image.load("dessins/t1.png").convert_alpha()
ci2 = pg.image.load("dessins/t2.png").convert_alpha()
ci3 = pg.image.load("dessins/t3.png").convert_alpha()
ci4 = pg.image.load("dessins/t4.png").convert_alpha()