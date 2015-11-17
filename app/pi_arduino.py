import serial
import time
import sys

ser = serial.Serial('/dev/ttyACM0', 9600)
i = 0
while True:
    number = raw_input("input :")
    if(number == '0'):
        break
    ser.write(number)
    #time.sleep(1);
    #i = i+1
