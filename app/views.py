# -*- coding: utf-8 -*-
from flask import render_template
from app import app

@app.route('/')
<<<<<<< HEAD
@app.route('/index')
def index():
	return render_template('index.html', title='ROV control')
=======
def index():
	return render_template('index.html', title='ROV control')
		
>>>>>>> origin/master
