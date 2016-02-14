from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import Form

app = Flask(__name__)
from app import views
