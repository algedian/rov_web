# -*- coding: utf-8 -*-
#!/usr/bin/env python
import serial
import time
import sys
from flask import Flask, render_template, Response
from app import app
from camera_pi import Camera

@app.route('/', methods=['POST', 'GET'])
def index():
	return render_template('index.html', title='ROV control')
	
def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
               
@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/ledon')
def ledon():
	print("ledon")
	#ser = serial.Serial('/dev/ttyUSB0', 9600)
	ser = serial.Serial('/dev/ttyACM0', 9600) #arduino due
	ser.write("m117")
	ser.close()
	return "led on complete"

@app.route('/ledoff')
def ledoff():
	print("ledoff")
	#ser = serial.Serial('/dev/ttyUSB0', 9600)
	ser = serial.Serial('/dev/ttyACM0', 9600) #arduino due
	ser.write("m017")
	ser.close()
	return "led off complete"
	
@app.route('/gostraight')
def gostraight():
	print("go straight")
	#ser = serial.Serial('/dev/ttyUSB0', 9600)
	ser = serial.Serial('/dev/ttyACM0', 9600) #arduino due
	ser.write("m1256")
	ser.close()
	return "go straight complete"
	
@app.route('/goback')
def goback():
	print("go back")
	#ser = serial.Serial('/dev/ttyUSB0', 9600)
	ser = serial.Serial('/dev/ttyACM0', 9600) #arduino due
	ser.write("m2256")
	ser.close()
	return "go back complete"
	
@app.route('/goleft')
def goleft():
	print("go left")
	#ser = serial.Serial('/dev/ttyUSB0', 9600)
	ser = serial.Serial('/dev/ttyACM0', 9600) #arduino due
	ser.write("m115")
	ser.close()
	return "go left complete"
	
@app.route('/goright')
def goright():
	print("go right")
	#ser = serial.Serial('/dev/ttyUSB0', 9600)
	ser = serial.Serial('/dev/ttyACM0', 9600) #arduino due
	ser.write("m116")
	ser.close()
	return "go right complete"

@app.route('/goup')
def goup():	
	print("go up")
	#ser = serial.Serial('/dev/ttyUSB0', 9600)
	
	#ser = serial.Serial('/dev/ttyACM0, 9600)	
	#ser.write("m141234")	
	#ser.close()
	ser2 = serial.Serial('/dev/ttyACM1', 9600) #arduino uno
	ser2.write("m141234")
	ser2.close()
	return "go up return"

@app.route('/godown')
def godown():
	print("go down")
	#ser = serial.Serial('/dev/ttyUSB0', 9600)
	
	ser = serial.Serial('/dev/ttyACM1', 9600) #arduino uno
	ser.write("m241234")
	ser.close()
	#ser2 = serial.Serial('/dev/ttyACM0, 9600)
	#ser2.write("m0256")
	#ser2.close()
	return "go down return"
	
@app.route('/updownstop')
def updownstop():
	print("updown motor stop")
	#ser = serial.Serial('/dev/ttyUSB0', 9600)
	
	#ser = serial.Serial('/dev/ttyACM0, 9600)
	#ser.write("m041234")
	#ser.close()
	ser2 = serial.Serial('/dev/ttyACM1', 9600) #arduino uno
	ser2.write("m041234")
	ser2.close()
	return "updown motor stopped"

@app.route('/forbackstop')
def forbackstop():
	print("forback motor stop")
	#ser = serial.Serial('/dev/ttyUSB0', 9600)
	
	ser = serial.Serial('/dev/ttyACM0', 9600) #arduino due
	ser.write("m0256")
	ser.close()
	#ser2 = serial.Serial('/dev/ttyACM1', 9600) #arduino uno
	#ser2.write("m0256")
	#ser2.close()
	return "forback motor stopped"
