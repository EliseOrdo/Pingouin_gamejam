"""les pengouins."""
#import Phyphox2python as p2p
from variables import *
from classes import *


pg.init()

screen = pg.display.set_mode((fen_l, fen_h))
background = pg.Surface(screen.get_size())
background = background.convert()
background.fill((186, 235, 239))

font = pg.font.Font(None, 24)
text = font.render(str(mouvements), 1, (0, 100, 255))

runningf = True

init()

while runningf:
    # PARTIE EVENTS
    for event in pg.event.get():
        if event.type == pg.QUIT:
            runningf = False
        if event.type == pg.KEYDOWN:
            if fini:
                match event.key:
                    case pg.K_o:
                        init()
                    case pg.K_n:
                        pg.quit()
            liste_pingouins[0].tourne(event.key)
            for pingind in range(len(liste_pingouins)):
                if not liste_pingouins[pingind].cache:
                    liste_pingouins[pingind].move(event.key)
            for ciblind in range(len(liste_cibles)):
                if not liste_cibles[ciblind].cache:
                    for ping in range(len(liste_pingouins)):
                        liste_cibles[ciblind].touche_cible(liste_pingouins[ping], event.key)
    # PARTIE DESSIN
    screen.blit(wallpaper, (0, 0))
    dessine(dict_obj)
    if cibles_touchees == pingcibles:
        fini = True
        text_fin = font.render("Bravo !!", 10, (0, 100, 255))
        screen.blit(text_fin, (fen_l/2-35, fen_h/2-5))
        txt = font.render("Recommencer ? (o , n)", 10, (0, 100, 255))
        screen.blit(txt, (fen_l/2 - 85, fen_h/2 + 15))
        #screen.blit(font.render(t, 10, (0,100,255)), (fen_l/2-145, fen_h/2 + 15))
        screen.blit(font.render(tmps[1], 1, (0, 100, 255)), (950, 0))
        screen.blit(font.render(tmps[0], 1, (0, 100, 255)), (895, 0))
    else:
        screen.blit(font.render(tmps[1], 1, (0, 100, 255)), (950, 0))
        screen.blit(font.render(tmps[0], 1, (0, 100, 255)), (895, 0))
        tmps = compteur_temps()
    pg.display.flip()
pg.quit()