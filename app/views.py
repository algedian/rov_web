# -*- coding: utf-8 -*-
from flask import render_template
from app import app

@app.route('/', methods=['POST', 'GET'])
def index():
	return render_template('index.html', title='ROV control')
	
def button_input():
	if request.method == 'POST':
		
