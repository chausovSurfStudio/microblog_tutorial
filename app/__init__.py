from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import Form
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)
from app import views
