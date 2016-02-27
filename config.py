import os

SECRET_KEY = 'very_hard_key_092758'
SQLALCHEMY_DATABASE_URI = 'sqlite:////Users/chausovalexander/Documents/surfstudio_project/microblog_tutorial/app/data.sqlite'
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')