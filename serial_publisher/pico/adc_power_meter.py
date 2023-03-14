from machine import Pin, ADC, UART
import time
import utime


endCounter = 10000000
arValues = []
valTotal = 0
adc = ADC(26)
pin_led = Pin(20, mode=Pin.OUT, value=1) 

utime.sleep(3)
while True:
  analogVal = adc.read_u16()
  #	print(analogVal)
  volt= (analogVal / 1024 * 3.3) * 0.185
  utime.sleep(0.02)
  valTotal += volt
  arValues.append(volt)
  val = "{:.2f}".format(volt)
  print( val)
  #uart.write(str(volt) + "\n")
  utime.sleep(0.15)
  arValues = []
  valTotal = 0
  time.sleep(2)


