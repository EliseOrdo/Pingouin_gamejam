import pygame as pg
import variables as var
import fonctions as func

class Pingouin:
    """definie un pingouin."""

    def __init__(self, x, y):
        self.taille = (18, 17)
        # (width = horizontal = axe x, height = vertical = axe y)
        self.x = x
        self.y = y
        self.image = pg.image.load("dessins/ping.png").convert_alpha()
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
        bas = y1[1] > var.fen_h
        gauche = x1[0] < 0
        droite = x2[0] > var.fen_l
        return haut_gauche or bas_gauche or haut_droit or bas_droit or haut or bas or gauche or droite

    def touche_qui_ou(self):
        """Renvoie le mur touché par le pingouin"""
        print("self x : {}, y : {}".format(self.x,self.y))
        for mur in var.liste_murs:
            if self.touche_truc(mur):
                return True
        return False

    def move(self, touche):
        """Fait bouger le pingouin."""
        vit = 22
        if self.touche_qui_ou() is False:
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

    def tourne(self, dir):
        """UNIQUEMENT AVEC LES TOUCHES"""
        #Rotation
        match self.orientation:
            case 'haut':
                match dir :
                    case 'droite':
                        self.orientation = 'droite'
                        self.image = pg.transform.rotate(self.image, -90)
                        var.screen.blit(self.image, (self.x, self.y))
                    case 'bas':
                        self.orientation = 'bas'
                        self.image = pg.transform.rotate(self.image, 180)
                        var.screen.blit(self.image, (self.x, self.y))
                    case 'gauche':
                        self.orientation = 'gauche'
                        self.image = pg.transform.rotate(self.image, 90)
                        var.screen.blit(self.image, (self.x, self.y))
            
            case 'droite':
                match dir:
                    case 'haut':
                        self.orientation = 'haut'
                        self.image = pg.transform.rotate(self.image, 90)
                        var.screen.blit(self.image, (self.x, self.y))
                    case 'bas':
                        self.orientation = 'bas'
                        self.image = pg.transform.rotate(self.image, -90)
                        var.screen.blit(self.image, (self.x, self.y))
                    case 'gauche':
                        self.orientation = 'gauche'
                        self.image = pg.transform.rotate(self.image, 180)
                        var.screen.blit(self.image, (self.x, self.y))

            case 'gauche':
                match dir:
                    case 'haut':
                        self.orientation = 'haut'
                        self.image = pg.transform.rotate(self.image, -90)
                        var.screen.blit(self.image, (self.x, self.y))
                    case 'bas':
                        self.orientation = 'bas'
                        self.image = pg.transform.rotate(self.image, 90)
                        var.screen.blit(self.image, (self.x, self.y))
                    case 'droite':
                        self.orientation = 'droite'
                        self.image = pg.transform.rotate(self.image, 180)
                        var.screen.blit(self.image, (self.x, self.y))

            case 'bas':
                match dir :
                    case 'droite':
                        self.orientation = 'droite'
                        self.image = pg.transform.rotate(self.image, 90)
                        var.screen.blit(self.image, (self.x, self.y))
                    case 'haut':
                        self.orientation = 'haut'
                        self.image = pg.transform.rotate(self.image, 180)
                        var.screen.blit(self.image, (self.x, self.y))
                    case 'gauche':
                        self.orientation = 'gauche'
                        self.image = pg.transform.rotate(self.image, -90)
                        var.screen.blit(self.image, (self.x, self.y))


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

    def touche_cible(self, pingouin: Pingouin):
        """Renvoie vrai si le pingouin touche la cible + fait des choses"""
        if pingouin.touche_truc(self):
            self.cache = True
            if self in var.dict_obj['Cibles']:
                var.dict_obj['Cibles'].remove(self)
            var.cibles_touchees += 1
            pingouin.cache = True
            var.dict_obj['Pingouins'].remove(pingouin)
            self.anim = True
            match pingouin.orientation:
                case 'bas':
                    var.screen.blit(var.cache, (pingouin.x, pingouin.y - 22))
                    pg.display.update(pg.Rect(pingouin.x, pingouin.y - 22, 40, 40))
                case 'haut':
                    var.screen.blit(var.cache, (pingouin.x, pingouin.y + 22))
                    pg.display.update(pg.Rect(pingouin.x, pingouin.y + 22, 40, 40))
                case 'gauche':
                    var.screen.blit(var.cache, (pingouin.x + 22, pingouin.y))
                    pg.display.update(pg.Rect(pingouin.x + 22, pingouin.y, 40, 40))
                case 'droite':
                    var.screen.blit(var.cache, (pingouin.x - 22, pingouin.y))
                    pg.display.update(pg.Rect(pingouin.x - 22, pingouin.y, 40, 40))
            var.screen.blit(var.ci, (self.x, self.y))
            pg.display.update(pg.Rect(self.x, self.y, 40, 40))
            return True
        return False