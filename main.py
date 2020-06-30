# Measuring barometric pressure and temperature using av BMP180 sensor
import time
import machine
import pycom
from machine import I2C
from bmp085 import BMP180
from machine import Pin

def calcAverage(values):
  return sum(values)/len(values);

def blinkLED(myLED, blinktime):
    myLED.value(1)
    time.sleep(blinktime)
    myLED.value(0)
    time.sleep(blinktime)

def RGBTemperature(temp):
    if temp<20:
        pycom.rgbled(0x0000FF)  # Blue
    elif temp>25:
        pycom.rgbled(0xFF0000)  # Red
    else:
        pycom.rgbled(0x00FF00)  # Green

temperatures=[] #Create an empty list for storing the temperatures

#Create a Pin object for the blue LED
blueLED = Pin('P8', mode = Pin.OUT)

#Set up i2c protocol for the BMP180 sensor
i2c = I2C(0)                         # create on bus 0
i2c = I2C(0, I2C.MASTER)             # create and init as a master
i2c = I2C(0, pins=('P9','P10'))      # PIN assignments (P9=SDA, P10=SCL)
i2c.init(I2C.MASTER, baudrate=115200) # init as a master
bmp = BMP180(i2c)

pycom.heartbeat(False)

for i in range(1,1000):
    temp=bmp.temperature    #Read temperature from BMP180
    temperatures.append(temp)
    pressure=bmp.pressure   #Read pressure from BMP180

    #RGBTemperature(temp)    #Set color of RGB diode according to temperature

    print('Temperature = ', temp)
    print('Pressure = ', pressure)

    pybytes.send_signal(1,temp)
    pybytes.send_signal(2,round(pressure,2))
    if(i%24==0):
        pybytes.send_signal(3,round(min(temperatures),2))
        pybytes.send_signal(4,round(max(temperatures),2))
        pybytes.send_signal(5,round(calcAverage(temperatures),2))
        temperatures=[]     #Clear the temperature list
    blinkLED(blueLED,0.5)

    #The time until next iteration in the loop. For example, time.sleep(3600)
    #makes the Pycom read from the BMP180 and send data once every hour.
    time.sleep(3600)

pycom.rgbled(0x000000)  #Set RGB LED to black
