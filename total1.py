import os
import threading
from firebase import firebase
import time

gasValue = '0'
maxValue = '0'
minValue = '0'
temp = '0'
humi = '0'

def gas() :
    os.system("sudo ./gas")

def cam() :
    os.system("sudo ./raspberrypi_video")

def temphumi() :
    os.system("sudo python discomfort.py")

def get() :
    global gasValue, maxValue, minValue, temp, humi
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

def upload_gas(f) :
    global gasValue
    while(True) :
        print("gasOK")
        upload_gas = f.patch('/gas', {'gas' : int(gasValue, base=10)});
        time.sleep(0.1)

def upload_max(f) :
    global maxValue
    while(True) :
        print("maxOK")
        upload_max = f.patch('/max', {'max' : int(maxValue, base=10)});
        time.sleep(0.1)

def upload_min(f) :
    global minValue
    while(True) :
        print("minOK")
        upload_min = f.patch('/min', {'min' : int(minValue, base=10)});
        time.sleep(0.1)

def upload_temp(f) :
    global temp
    while(True) :
        print("tempOK")
        upload_temp = f.patch('/temp', {'temp' : int(temp, base=10)});
        time.sleep(0.1)

def upload_humi(f) :
    global humi
    while(True) :
        print("humiOK")
        upload_humi = f.patch('/humi', {'humi' : int(humi)});
        time.sleep(0.1)

fire = firebase.FirebaseApplication('https://ohmybaby-60436.firebaseio.com', None)


t1 = threading.Thread(target=gas, )
t1.start()

t2 = threading.Thread(target=cam, )
t2.start()

t3 = threading.Thread(target=temphumi, )
t3.start()

t4 = threading.Thread(target=get, )
t4.start()

t5 = threading.Thread(target=upload_gas, args=(fire, ))
t5.start()

t6 = threading.Thread(target=upload_max, args=(fire, ))
t6.start()

t7 = threading.Thread(target=upload_min, args=(fire, ))
t7.start()

t8 = threading.Thread(target=upload_temp, args=(fire, ))
t8.start()

t9 = threading.Thread(target=upload_humi, args=(fire, ))
t9.start()
