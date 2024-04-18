"""les pengouins."""
import requests
import pygame as pg
import variables as var
import fonctions as func


'''Connect to the phone by wifi'''
requests.get(var.starturl)
p1=0
p2=0
p3=0


pg.init()
pg.font.init()


runningf = True

func.init()

while runningf:
    # PARTIE EVENTS
    for event in pg.event.get():
        if event.type == pg.QUIT:
            runningf = False
        
    #Boucle pour le mouvement
 
    for pingind in range(len(var.liste_pingouins)):
        if not var.liste_pingouins[pingind].cache:
            var.liste_pingouins[pingind].vitesse = func.acc2speed(var.acc, var.liste_pingouins[pingind].vitesse)  
            var.liste_pingouins[pingind].vitesse = func.position(var.liste_pingouins[pingind], var.liste_pingouins[pingind].vitesse)
            if abs(var.liste_pingouins[pingind].vitesse[0] < abs(var.liste_pingouins[pingind].vitesse[1])):
                if var.liste_pingouins[pingind].vitesse[1] > 0:
                    var.liste_pingouins[pingind].tourne('bas')
                elif var.liste_pingouins[pingind].vitesse[1] < 0:
                    var.liste_pingouins[pingind].tourne('haut')
            else:
                if var.liste_pingouins[pingind].vitesse[0] < 0:
                    var.liste_pingouins[pingind].tourne('gauche')
                elif var.liste_pingouins[pingind].vitesse[0] > 0:
                    var.liste_pingouins[pingind].tourne('droite')                   
            print("position ", "indice ",pingind)
    for ciblind in range(len(var.liste_cibles)):
        if not var.liste_cibles[ciblind].cache:
            for ping in range(len(var.liste_pingouins)):
                if var.liste_cibles[ciblind].touche_cible(var.liste_pingouins[ping]):
                    func.animcible(var.liste_cibles[ciblind])            

    # PARTIE DESSIN
    var.screen.blit(var.wallpaper, (0, 0))
    func.dessine(var.dict_obj)
    if var.cibles_touchees == var.pingcibles:
        var.fini = True
        text_fin = var.font.render("Bravo !!", 10, (0, 100, 255))
        txt = var.font.render("Recommencer ?", 10, (0, 100, 255))
        t = var.font.render("monter : oui, descendre : non", 10, (0, 100, 255))
        var.screen.blit(text_fin, (var.fen_l/2-35, var.fen_h/2-5))
        var.screen.blit(txt, (var.fen_l/2 - 70, var.fen_h/2 + 15))
        var.screen.blit(t, (var.fen_l/2-120, var.fen_h/2 + 35))
        var.screen.blit(var.font.render(var.tmps[1], 1, (0, 100, 255)), (950, 0))
        var.screen.blit(var.font.render(var.tmps[0], 1, (0, 100, 255)), (895, 0))
    else:
        var.screen.blit(var.font.render(var.tmps[1], 1, (0, 100, 255)), (950, 0))
        var.screen.blit(var.font.render(var.tmps[0], 1, (0, 100, 255)), (895, 0))
        var.tmps = func.compteur_temps()
    pg.display.flip()
pg.quit()