from app import app
from flask import render_template, session, redirect, url_for, flash, request
from flask.ext.login import login_user, login_required, logout_user, current_user
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from app import model, send_mail
from model import User, db
from forms import LoginForm, NameForm, RegistrationForm, ChangePasswordForm, ResetPasswordFirstForm, ResetPasswordFinalStepForm, ChangeEmailForm

bootstrap = Bootstrap(app)

@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.name.data).first()
        if user is None:
            user = User(username = form.name.data)
            db.session.add(user)
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index.html', form = form, name = session.get('name'), known = session.get('known', False))

@app.route('/user/<name>')
def user(name):
    User.query.delete()
    return render_template('user.html', name = name)

@app.route('/auth/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('index'))
        flash('Invalid username or password')
    return render_template('auth/login.html', form = form)

@app.route('/auth/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out')
    return redirect(url_for('index'))

@app.route('/auth/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data)
        user.password = form.password.data
        db.session.add(user)
        db.session.commit()
        token = user.generate_confirmation_token()
        send_mail(user.email, 'Confirm Your Account', 'mail/confirm', user = user, token = token)
        flash('A confirmation email has been sent to you by email.')
        return redirect(url_for('index'))
    return render_template('auth/register.html', form = form)

@app.route('/auth/confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('index'))
    if current_user.confirm(token):
        flash('You have confirmed your account, thanks!')
    else:
        flash('The confirmation link is invalid or has expired')
    return redirect(url_for('index'))

@app.route('/auth/unconfirmed')
def unconfirmed():
    if current_user.is_anonymous or current_user.confirmed:
        return redirect('index')
    return render_template('auth/unconfirmed.html')

@app.route('/auth/resend_confirm')
@login_required
def resend_confirmation():
    token = current_user.generate_confirmation_token()
    send_mail(current_user.email, 'Confirm Your Account', 'mail/confirm', user = current_user, token = token)
    flash('A new confirmation email has been sent to you')
    return redirect(url_for('index'))

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

@app.route('/profile/change_password', methods = ['GET', 'POST'])
@login_required
def change_password():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        current_user.password = form.password.data
        db.session.add(current_user)
        db.session.commit()
        send_mail(current_user.email, 'Password was change', 'mail/change_password_mail', user = current_user)
        flash('Email about changing password has been sent to you by email.')
        return redirect(url_for('login'))
    return render_template('change_password.html', form = form)

@app.route('/login/reset_password', methods = ['GET', 'POST'])
def reset_password():
    form = ResetPasswordFirstForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if not user:
            flash('Invalid email')
        else:
            token = user.generate_confirmation_token()
            send_mail(user.email, 'Reset password', 'mail/reset_password_mail', user = user, token = token)
            flash('Email to reset your password has been sent to you by email.')
            return redirect(url_for('index'))
    return render_template('reset_password.html', form = form)

@app.route('/login/reset_password_final/<token>', methods = ['GET', 'POST'])
def reset_password_final(token):
    form = ResetPasswordFinalStepForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if not user:
            flash('Invalid email')
        else:
            if not user.confirm(token):
                flash('The confirmation link is invalid or has expired')
            else:
                user.password = form.password.data
                db.session.add(user)
                flash('Your password has been reset')
        return redirect(url_for('index'))
    return render_template('reset_password_final.html', form = form)

@app.route('/auth/change_email', methods = ['GET', 'POST'])
@login_required
def change_email():
    form = ChangeEmailForm()
    if form.validate_on_submit():
        token = current_user.generate_confirmation_token()
        send_mail(form.email.data, 'Change email address', 'mail/change_email_mail', user = current_user, token = token, email = form.email.data)
        flash('Mail to confirm has been send in your new address')
        return redirect(url_for('index'))
    return render_template('auth/change_email.html', form = form)

@app.route('/auth/confirm_change_email/<token>/<email>')
@login_required
def confirm_change_email(email, token):
    if current_user.confirm(token):
        current_user.email = email;
        db.session.add(current_user)
        flash('You changed your email address')
    else:
        flash('The confirmation link is invalid or has expired')
    return redirect(url_for('index'))

def before_request():
    if current_user.is_authenticated and not current_user.confirmed and request.endpoint[:5] != 'auth.':
        return redirect(url_for('unconfirmed'))