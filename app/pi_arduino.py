import serial
import time
import sys

ser = serial.Serial('/dev/ttyACM0', 9600)
led_status = 0

def led_toggle():
	if led_status is 0:
		led_on()
	elif led_status is 1:
		led_off()
	return False

def led_on():
	ser.write("m117")
	led_status = 1
	
def led_off():
	ser.write("m017")
	led_status = 0
