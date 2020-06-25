# Measuring barometric pressure and temperature using av BMP180 sensor
import time
import machine
import pycom
from machine import I2C
from bmp085 import BMP180
from machine import Pin

def calcAverageTemp(values):
  average = 0
  for i in range(0,len(values)):
    average += values[i]
    print(values[i])
  return average/len(values);

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

for i in range(1,10):
    temp=bmp.temperature    #Read temperature from BMP180
    temperatures.append(temp)
    pressure=bmp.pressure   #Read pressure from BMP180
    averageTemp = calcAverageTemp(temperatures)

    RGBTemperature(temp)    #Set color of RGB diode according to temperature

    print('Temperature = ', temp)
    print('Pressure = ', bmp.pressure)
    print("Average temp = %5.1f C" % (averageTemp))

    #pybytes.send_signal(1,int(temp))
    pybytes.send_signal(1,temp)
    pybytes.send_signal(2,pressure)
    blinkLED(blueLED,0.5)
    time.sleep(60)

pycom.rgbled(0x000000)  #Set RGB LED to black
