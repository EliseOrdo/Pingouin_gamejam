'''Control Phyphox from computer. Go to Setting on the phone and share connection. 
Connect the computer wifi to the phone
You can access to the PP_Adress directly from phyphox in ...
Control the experience monitored with the appropriate PP_CHANNELS names'''


import matplotlib.pyplot as plt
import numpy as np
import requests
import time


# A changer à chaques fois
PP_ADDRESS = "http://192.168.201.140:8080" 

fig, (ax1, ax2,ax3) = plt.subplots(ncols=3)

def Monitor(PP_ADDRESS):
     """PP_CHANNELS = ["magX","magY","magZ"] # Name should be changed depending on the parameter
     PP_CHANNELS = ["pressure"]
     PP_CHANNELS = ["pCal","tempCal"] #For the sensor tag (also a version with Raw instead of 
     cal but the unites are weird)
     PP_CHANNELS = ["accX","accY","accZ"] #pour l'accélération"""
     PP_CHANNELS = ["gyrX","gyrY","gyrZ"] #pour le gyroscope
     
     starturl = PP_ADDRESS + "/control?cmd=start"
     
     '''Connect to the phone by wifi'''
     requests.get(starturl)
     p1=0
     p2=0
     p3=0
     
     """ initialisation du tableau de données"""
     coo_gyr = np.array([[0],[0],[0]]) #x,y,z
     while True: # une fois dans le main, à enlever et à mettre dans la boucle principale
         #PP_ADRESS/get?&
         url = PP_ADDRESS + "/get?" + ("&".join(PP_CHANNELS))
         data = requests.get(url=url).json()
         for i, channel in enumerate(PP_CHANNELS):
             value = data["buffer"][channel]["buffer"][0]
             if i ==0 : 
                 ax1.plot(p1,value,'ro')
                 plt.pause(0.005)
                 p1+=1
             if i ==1 : 
                 ax2.plot(p2,value,'go')
                 plt.pause(0.005)
                 p2+=1
             if i ==2 : 
                 ax3.plot(p3,value,'bo')
                 plt.pause(0.005)
                 p3+=1
              ('Channel is : {}, value is : {} ,index is : {}'.format(channel,value,i) )
             coo_gyr[i][0] = value
             (coo_gyr[i][0])
             ()
            #time.sleep(0.05)
Monitor(PP_ADDRESS)
