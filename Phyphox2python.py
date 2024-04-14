'''Control Phyphox from computer. Go to Setting on the phone and share connection. 
Connect the computer wifi to the phone
You can access to the PP_Adress directly from phyphox in ...
Control the experience monitored with the appropriate PP_CHANNELS names'''


import matplotlib.pyplot as plt
import numpy as np
import requests
import time
import classes as clas
import pygame as pg
import variables as var

# A changer à chaques fois
PP_ADDRESS = "http://192.168.198.133:8080"  # dans variables

#fig, (ax1, ax2,ax3) = plt.subplots(ncols=3)

PP_CHANNELS = ["accX","accY","accZ"] #pour l'accélération avec g

starturl = PP_ADDRESS + "/control?cmd=start"
     
'''Connect to the phone by wifi'''
requests.get(starturl)
p1=0
p2=0
p3=0
     
""" initialisation du tableau de données"""
m = 1 # masse des pingouins (en faire des plus lourd ?)
pos_p = [0,0] #self.x, self.y
vit_p = [0,0]
acc = [0,0,0] #(x,y,z)    liste car pas besoin d'une array
#x(phyphox)=y(écran)


def acc2speed(acc: list, vit_p : list):
    
    #PP_ADRESS/get?&
    url = PP_ADDRESS + "/get?" + ("&".join(PP_CHANNELS))
    data = requests.get(url=url).json()
    for i, channel in enumerate(PP_CHANNELS):
        saute = False
        value = data["buffer"][channel]["buffer"][0]
        if(value == None): value = 0  #si value==None, on ne peut pas la mettre dans notre array acc_p
        print ('Channel is : {}, value is : {} ,index is : {}'.format(channel,value,i) )
        if(value<=-2 or value>=2 ):
            if(acc[i] == m*value/2): saute = True
            else : acc[i] = m*value/2
        else:
            if(acc[i] == 0) : saute = True
            else: acc[i] = 0
        print(acc[i])
        print("pingouin : \nax : {}\nay : {}\n".format(acc[0],acc[1]))
        if not saute:
            #on n'oublie pas de séparer les cas i=0 ou 1 parce que sinon le truc fait deux fois les additions et évidemment ça part dans e130
            if i ==0 :
                if(vit_p[0] < 1 and vit_p[0]> -1): #0.5*0.5=0.25 on évite que ça tende vers 0 à l'infini
                    vit_p[0] = acc[1]  #on inverse x et y ici
                else :
                    if(vit_p[0] < 0 and acc[1]<0):
                        vit_p[0] *= -1*acc[1] #v = v*a~ --> - * - = + et on veut pas ça
                    else:
                        vit_p[0] *= acc[1]
            
            if i ==1 :
                if(vit_p[1] < 1 and vit_p[1]> -1): 
                    vit_p[1] = acc[0]
                else : 
                    if(vit_p[1] < 0 and acc[0]<0):
                        vit_p[1] *= -1*acc[0]
                    else:
                        vit_p[1] *= acc[0] 
            print("pingouin : \nvx : {}\nvy : {}\n".format(vit_p[0],vit_p[1]))
    return vit_p

def position(ping: clas.Pingouin , lvit_p: list):

    if(lvit_p[0] != 0):
        ping.x += lvit_p[0]  #x = x+v

        print("ping_x : ", ping.x)

    if(lvit_p[1] != 0):
        ping.y += lvit_p[1]   

        print("ping_y : ", ping.y)
    if(ping.x >= var.fen_l) : ping.x = var.fen_l -1
    elif(ping.x <= 0): ping.x = 1
    if(ping.y >= var.fen_h) : ping.y = var.fen_h -1
    elif(ping.y <= 0) : ping.y = 1
    #time.sleep(0.05)
    if(lvit_p[0] > 0): ping.orientation = 'droite'
    elif(lvit_p[0] < 0): ping.orientation = 'gauche'
    if(lvit_p[1] > 0): ping.orientation = 'bas'
    elif(lvit_p[1] < 0): ping.orientation = 'haut'
    while ping.touche_qui_ou() is True:
            print("collision")
            match ping.orientation :
                case 'haut':
                    ping.y += 1
                case 'bas':
                    ping.y -= 1
                case 'droite':
                    ping.x -= 1
                case 'gauche':
                    ping.x += 1
            print( "avant test x : ", ping.x, " y : ", ping.y)
            if(ping.x >= var.fen_l) : 
                ping.x = var.fen_l -1
                ping.orientation = 'droite' # même si on change d'orientation alors qu'on a dépasssé le cadre, on remet le bon
            elif(ping.x <= 0): 
                ping.x = 1
                ping.orientation = 'gauche'
            if(ping.y >= var.fen_h) : 
                ping.y = var.fen_h -1
                ping.orientation = 'bas'
            elif(ping.y <= 0) : 
                ping.y = 1
                ping.orientation = 'haut'

            ping.prect = pg.Rect((ping.x, ping.y), (20, 40))
    print( "x : ", ping.x, " y : ", ping.y)
    


"""graphique de la position"""
""""
pos = [0,0]
while True: 
    vit = acc2speed(acc, vit_p)
    pos = position(pos, vit)
    ax1.plot(p1,pos[0],'ro')
    plt.pause(0.005)
    p1+=1
    ax2.plot(p2,pos[1],'go')
    plt.pause(0.005)
    p2+=1
"""
#trucs à expliquer : vitesse angulaire, on veut pouvoir pencher lentement et que ça glisse quand même, donc on modélise le poids