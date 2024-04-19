import pygame as pg

#phy
# A changer à chaques fois
PP_ADDRESS = "http://192.168.172.40"
PP_CHANNELS = ["accX","accY","accZ"] #pour l'accélération avec g

starturl = PP_ADDRESS + "/control?cmd=start"

""" initialisation du tableau de données"""
m = 1 # masse des pingouins (en faire des plus lourd ?)
pos_p = [0,0] #self.x, self.y
vit_p = [0,0]
acc = [0,0,0] #(x,y,z)    liste car pas besoin d'une array
#x(phyphox)=y(écran)


fen_l : int= 1000
fen_h : int= 700

screen = pg.display.set_mode((fen_l, fen_h))
background = pg.Surface(screen.get_size())
background = background.convert()
background.fill((186, 235, 239))

pg.font.init()
font = pg.font.Font(None, 24)


ci = pg.image.load("dessins/water.png").convert_alpha()
ice = pg.image.load("dessins/iceberg.png").convert_alpha()
wallpaper = pg.image.load("dessins/wallpapers_neige.png").convert_alpha()
cache = pg.image.load("dessins/snow.png").convert_alpha()
ci1 = pg.image.load("dessins/t1.png").convert_alpha()
ci2 = pg.image.load("dessins/t2.png").convert_alpha()
ci3 = pg.image.load("dessins/t3.png").convert_alpha()
ci4 = pg.image.load("dessins/t4.png").convert_alpha()

#Variables qui vont etre def dans func.init
dict_obj : dict = {}
liste_murs : list = []
liste_cibles : list = []
liste_pingouins : list = []
pingcibles : int = None
start : int = None
tmps : tuple = None
fini : bool = False