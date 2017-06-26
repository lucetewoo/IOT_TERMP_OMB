import os
import threading
from firebase import firebase
import time

def gas() :
    os.system("sudo ./gas")

def cam() :
    os.system("sudo ./raspberrypi_video")

def temphumi() :
    os.system("sudo python discomfort.py")

def upload(f) :
    
    while(True) :
        g = open("gasValue.txt", "r")
        gasValue = g.readline()

        maxV = open("maxValue.txt", "r")
        maxValue = maxV.readline()

        minV = open("minValue.txt", "r")
        minValue = minV.readline()

        t = open("temperature.txt", "r")
        temp = t.readline()

        h = open("humidity.txt", "r")
        humi = h.readline()

        print("*******************************")

        upload_gas = f.patch('/gas', {'gas' : int(gasValue)});
        upload_max = f.patch('/max', {'max' : int(maxValue)});
        upload_min = f.patch('/min', {'min' : int(minValue)});
        upload_temp = f.patch('/temp', {'temp' : int(temp)});
        upload_humi = f.patch('/humi', {'humi' : int(humi)});

        time.sleep(0.5)

fire = firebase.FirebaseApplication('https://ohmybaby-60436.firebaseio.com', None)

t1 = threading.Thread(target=gas, )
t1.start()

t2 = threading.Thread(target=cam, )
t2.start()

t3 = threading.Thread(target=temphumi, )
t3.start()

t4 = threading.Thread(target=upload, args=(fire, ))
t4.start()
