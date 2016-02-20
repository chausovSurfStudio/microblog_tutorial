from flask import Flask
from flask.ext.login import LoginManager

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'very_hard_key_092758'
app.config.from_object('config')

from app.model import db
db.init_app(app)  

from app import views

login_manager.init_app(app)
	
