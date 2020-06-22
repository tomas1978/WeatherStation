# Measuring temperature by TMP36
import time
import machine


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

temperatures=[] #Create an empty list for storing the temperatures

#Create a Pin object for the blue LED
from machine import Pin
blueLED = Pin('P9', mode = Pin.OUT)

adc = machine.ADC()             #Create an ADC object
apin = adc.channel(pin='P16');  #Create an analog pin on P16 & connect TMP36

for i in range(1,20):
    print("")
    print("Reading TMP36 sensor...")
    value = apin()
    print("ADC count = %d" %(value))

    #LoPy has 1.1 V input range for adc
    temp = ((value * 1100 ) / 4096 - 500) / 10
    temp -= 2.3  #Testing to calibrate temperature
    temperatures.append(temp)
    print("Temperature = %5.1f C" % (temp))

    averageTemp = calcAverageTemp(temperatures)

    print("Average temp = %5.1f C" % (averageTemp))

    pybytes.send_signal(1,round(temp,1))
    pybytes.send_signal(2,round(averageTemp,1))

    blinkLED(blueLED,0.5)
    #blueLED.value(1)
    #time.sleep(0.5)
    #blueLED.value(0)
    #time.sleep(0.5)

    time.sleep(10)
