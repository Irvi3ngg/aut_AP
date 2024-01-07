#File name: init_AP.py
#Author: Irving Juarez (extracted from  Adeept_RaspTank)
#Pendientes: El archivo no se ejecuta en el arranque de la raspberry
            #Implementar una rutina en donde si sigue conectado a la red no vuelva a ejecutar funcion sta_thread()
            #Cuando esta en modo AP e identifica la red conocida, se conecta a esta pero con la config incorrecta de /etc/dhcpcd.conf

#File name: init_AP.py
#Author: Irving Juarez (extracted from  Adeept_RaspTank)

import time
#import threading
import os

import wifi

def ap_thread():
    os.system("sudo cp /etc/dhcpcd.conf.ap /etc/dhcpcd.conf")
    os.system("sudo systemctl start dnsmasq")
    os.system("sudo systemctl restart hostapd")

def sta_thread():
    os.system("sudo cp /etc/dhcpcd.conf.sta /etc/dhcpcd.conf")
    os.system("sudo systemctl stop dnsmasq")
    os.system("sudo systemctl stop hostapd")
    os.system("sudo ifconfig wlan0 down")
    os.system("sudo ifconfig wlan0 up")

def wifi_check(ssid):
    try:
        cells = wifi.Cell.all("wlan0")
        for cell in cells:
            if cell.ssid == ssid:
                return True
        return False

    except:
        print("wlan0 ocupada")
        #ap_threading = threading.Thread(target=ap_thread)
        #ap_threading.setDaemon(True)
        #ap_threading.start()

if __name__ == "__main__":
    ssid = "INFINITUMAD76_2.4"
    time.sleep(3)
    sta_val, ap_val = False, False
    while True:
        test = wifi_check(ssid)
        if test:
            if not sta_val:
                sta_thread()
            print("Station Mode Active")
            sta_val, ap_val = True, False
        else:
            if not ap_val:
                ap_thread()
            print("Access Point Mode Active")
            ap_val, sta_val = True, False
        time.sleep(20)