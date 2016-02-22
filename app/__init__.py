from flask import Flask
from flask.ext.login import LoginManager
from flask import render_template

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'

app = Flask(__name__)
app.config.from_object('config')

from app.model import db
db.init_app(app)  

login_manager.init_app(app)

from flask.ext.mail import Mail, Message

app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[Flasky]'
app.config['FLASKY_MAIL_SENDER'] = 'Flasky Admin <traktoro_13@mail.ru>'
mail = Mail(app)

def send_mail(to, subject, template, **kwargs):
	msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,
		          sender = app.config['FLASKY_MAIL_SENDER'], recipients =[to])
	msg.body = render_template(template + '.txt', **kwargs)
	msg.html = render_template(template + '.html', **kwargs)
	print('ready to sent')
	mail.send(msg)
	print('message was send')
	
from app import views
