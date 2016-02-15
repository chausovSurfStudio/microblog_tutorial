from flask import Flask


def create_app(config_filename):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'very_hard_key_092758'
    app.config.from_object(config_filename)

    from app.model import db
    db.init_app(app)   

    return app

def initFuckingViews():
	from app import views
