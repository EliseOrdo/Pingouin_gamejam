"""les pengouins."""
import pygame as pg
import variables as var
import fonctions as func
import classes as clas


pg.init()
pg.font.init()

runningf = True

func.init()

while runningf:
    # PARTIE EVENTS
    for event in pg.event.get():
        if event.type == pg.QUIT:
            runningf = False
        if event.type == pg.KEYDOWN:
            if var.fini:
                match event.key:
                    case pg.K_o:
                        func.init()
                    case pg.K_n:
                        pg.quit()
            var.liste_pingouins[0].tourne(event.key)
            for pingind in range(len(var.liste_pingouins)):
                if not var.liste_pingouins[pingind].cache:
                    var.liste_pingouins[pingind].move(event.key)
            for ciblind in range(len(var.liste_cibles)):
                if not var.liste_cibles[ciblind].cache:
                    for ping in range(len(var.liste_pingouins)):
                        if var.liste_cibles[ciblind].touche_cible(var.liste_pingouins[ping], event.key):
                            func.animcible(var.liste_cibles[ciblind])
    # PARTIE DESSIN
    var.screen.blit(var.wallpaper, (0, 0))
    func.dessine(var.dict_obj)
    if var.cibles_touchees == var.pingcibles:
        var.fini = True
        text_fin = var.font.render("Bravo !!", 10, (0, 100, 255))
        var.screen.blit(text_fin, (var.fen_l/2-35, var.fen_h/2-5))
        txt = var.font.render("Recommencer ? (o , n)", 10, (0, 100, 255))
        var.screen.blit(txt, (var.fen_l/2 - 85, var.fen_h/2 + 15))
        #screen.blit(font.render(t, 10, (0,100,255)), (fen_l/2-145, fen_h/2 + 15))
        var.screen.blit(var.font.render(var.tmps[1], 1, (0, 100, 255)), (950, 0))
        var.screen.blit(var.font.render(var.tmps[0], 1, (0, 100, 255)), (895, 0))
    else:
        var.screen.blit(var.font.render(var.tmps[1], 1, (0, 100, 255)), (950, 0))
        var.screen.blit(var.font.render(var.tmps[0], 1, (0, 100, 255)), (895, 0))
        var.tmps = func.compteur_temps()
    pg.display.flip()
pg.quit()