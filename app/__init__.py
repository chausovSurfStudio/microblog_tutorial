from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'very_hard_key_092758'
from app import views
