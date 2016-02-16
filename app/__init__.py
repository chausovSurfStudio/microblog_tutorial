from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'very_hard_key_092758'
app.config.from_object('config')

from app.model import db
db.init_app(app)  

from app import views
	
