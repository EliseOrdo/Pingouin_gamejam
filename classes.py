from fonctions import *
from variables import *

class Pingouin:
    """definie un pingouin."""

    def __init__(self, x, y):
        self.taille = (18, 17)
        # (width = horizontal = axe x, height = vertical = axe y)
        self.x = x
        self.y = y
        # Le point (x,y) est le point en haut a gauche de rectangle.
        self.prect = pg.Rect((self.x, self.y), self.taille)
        self.cache = False
        self.orientation = 'haut'

    def touche_truc(self, truc):
        """Verifie si le pingouin touche le truc (le truc doit avoir x et y en parametre).
            x1 : haut gauche de self, x2 : haut droit de self y1 bas gauche de self et y2 bas droit de self
            x3, x4, y3, y4 : meme chose pour truc"""
        x1, x2 = (self.x, self.y), (self.x + self.taille[0], self.y)
        y1, y2 = (self.x, self.y + self.taille[1]), (self.x + self.taille[0], self.y + self.taille[1])
        x3, x4 = (truc.x, truc.y), (truc.x + truc.taille[0], truc.y)
        y3, y4 = (truc.x, truc.y + truc.taille[1]), (truc.x + truc.taille[0], truc.y + truc.taille[1])
        haut_gauche = x3[0] < x1[0] < x4[0] and x3[1] < x1[1] < y3[1]
        haut_droit = x3[0] < x2[0] < x4[0] and x3[1] < x2[1] < y3[1]
        bas_gauche = x3[0] < y1[0] < x4[0] and x3[1] < y1[1] < y3[1]
        bas_droit = x3[0] < y2[0] < x4[0] and x3[1] < y2[1] < y3[1]
        haut = x1[1] < 0
        bas = y1[1] > fen_h
        gauche = x1[0] < 0
        droite = x2[0] > fen_l
        return haut_gauche or bas_gauche or haut_droit or bas_droit or haut or bas or gauche or droite

    def touche_qui_ou(self):
        """Renvoie le mur touché par le pingouin"""
        for mur in liste_murs:
            if self.touche_truc(mur):
                return True
        return False

    def move(self, touche):
        """Fait bouger le pingouin."""
        global mouvements
        vit = 22
        if self.touche_qui_ou() is False:
            #Mouvement

            match touche:
                case pg.K_UP:
                    self.y -= vit
                case pg.K_DOWN:
                    self.y += vit
                case pg.K_RIGHT:
                    self.x += vit
                case pg.K_LEFT:
                    self.x -= vit
                
        while self.touche_qui_ou() is True:
            match touche :
                case pg.K_UP:
                    self.y += 1
                case pg.K_DOWN:
                    self.y -= 1
                case pg.K_RIGHT:
                    self.x -= 1
                case pg.K_LEFT:
                    self.x += 1
            self.prect = pg.Rect((self.x, self.y), (20, 40))

    def tourne(self, touche):
        global pin
        #Rotation
        match self.orientation:
            case 'haut':
                match touche :
                    case pg.K_RIGHT:
                        self.orientation = 'droite'
                        pin = pg.transform.rotate(pin, -90)
                        screen.blit(pin, (self.x, self.y))
                    case pg.K_DOWN:
                        self.orientation = 'bas'
                        pin = pg.transform.rotate(pin, 180)
                        screen.blit(pin, (self.x, self.y))
                    case pg.K_LEFT:
                        self.orientation = 'gauche'
                        pin = pg.transform.rotate(pin, 90)
                        screen.blit(pin, (self.x, self.y))
            
            case 'droite':
                match touche:
                    case pg.K_UP:
                        self.orientation = 'haut'
                        pin = pg.transform.rotate(pin, 90)
                        screen.blit(pin, (self.x, self.y))
                    case pg.K_DOWN:
                        self.orientation = 'bas'
                        pin = pg.transform.rotate(pin, -90)
                        screen.blit(pin, (self.x, self.y))
                    case pg.K_LEFT:
                        self.orientation = 'gauche'
                        pin = pg.transform.rotate(pin, 180)
                        screen.blit(pin, (self.x, self.y))
                (self.orientation)

            case 'gauche':
                match touche:
                    case pg.K_UP:
                        self.orientation = 'haut'
                        pin = pg.transform.rotate(pin, -90)
                        screen.blit(pin, (self.x, self.y))
                    case pg.K_DOWN:
                        self.orientation = 'bas'
                        pin = pg.transform.rotate(pin, 90)
                        screen.blit(pin, (self.x, self.y))
                    case pg.K_RIGHT:
                        self.orientation = 'droite'
                        pin = pg.transform.rotate(pin, 180)
                        screen.blit(pin, (self.x, self.y))
                (self.orientation)

            case 'bas':
                match touche :
                    case pg.K_RIGHT:
                        self.orientation = 'droite'
                        pin = pg.transform.rotate(pin, 90)
                        screen.blit(pin, (self.x, self.y))
                    case pg.K_UP:
                        self.orientation = 'haut'
                        pin = pg.transform.rotate(pin, 180)
                        screen.blit(pin, (self.x, self.y))
                    case pg.K_LEFT:
                        self.orientation = 'gauche'
                        pin = pg.transform.rotate(pin, -90)
                        screen.blit(pin, (self.x, self.y))
                (self.orientation)


class Mur:
    """Un mur."""

    def __init__(self, x, y, taille):
        self.taille = taille
        self.x = x
        self.y = y
        self.couleur = (250, 250, 250)


class Cible:
    """Je propose que le but soit d'aller dans l'eau, genre pour chercher du poisson."""

    def __init__(self, x, y):
        self.taille = (40, 40)
        self.x = x
        self.y = y
        self.couleur = (140, 220, 250)
        self.cache = False
        self.anim = False

    def touche_cible(self, pingouin, key):
        """Renvoie vrai si le pingouin touche la cible."""
        global cibles_touchees
        global dict_obj
        if pingouin.touche_truc(self):
            self.cache = True
            if self in dict_obj['Cibles']:
                dict_obj['Cibles'].remove(self)
            cibles_touchees += 1
            pingouin.cache = True
            dict_obj['Pingouins'].remove(pingouin)
            self.anim = True
            match key:
                case pg.K_DOWN:
                    screen.blit(cache, (pingouin.x, pingouin.y - 22))
                    pg.display.update(pg.Rect(pingouin.x, pingouin.y - 22, 40, 40))
                case pg.K_UP:
                    screen.blit(cache, (pingouin.x, pingouin.y + 22))
                    pg.display.update(pg.Rect(pingouin.x, pingouin.y + 22, 40, 40))
                case pg.K_LEFT:
                    screen.blit(cache, (pingouin.x + 22, pingouin.y))
                    pg.display.update(pg.Rect(pingouin.x + 22, pingouin.y, 40, 40))
                case pg.K_RIGHT:
                    screen.blit(cache, (pingouin.x - 22, pingouin.y))
                    pg.display.update(pg.Rect(pingouin.x - 22, pingouin.y, 40, 40))
            screen.blit(ci, (self.x, self.y))
            pg.display.update(pg.Rect(self.x, self.y, 40, 40))
            animcible(self)