from app import app
from flask import render_template
from flask.ext.bootstrap import Bootstrap

bootstrap = Bootstrap(app)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
	return render_template('user.html', name = name)
