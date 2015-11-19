# -*- coding: utf-8 -*-
#!/usr/bin/env python
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

