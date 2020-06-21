# Measuring temperature by TMP36
import time
import machine


def calcAverageTemp(values):
  average = 0
  for i in range(0,len(values)):
    average += values[i]
    print(values[i])
  return average/len(values);

temperatures=[] #Create an empty list for storing the temperatures

adc = machine.ADC()             #Create an ADC object
apin = adc.channel(pin='P16');  #Create an analog pin on P16 & connect TMP36
for i in range(1,2):
    from machine import Pin
    blueLED = Pin('P17', mode = Pin.OUT)
    blueLED.value(1);

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

    pybytes.send_signal(1,temp)
    pybytes.send_signal(2,averageTemp)
    blueLED.value(1)
    time.sleep(0.2)
    blueLED.value(0)
    time.sleep(60)
