from flask import (Blueprint, render_template, redirect, url_for, flash, )
from jobplus.forms import LoginForm,RegisterForm
from flask_login import login_user
from jobplus.models import User,Company

front = Blueprint("front", __name__)


@front.route("/")
def index():
    return render_template('index.html')


@front.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        login_user(user, form.remember_me.data)
        if user.is_admin:
            pass
        elif user.is_boss:
            pass
        else:
            pass
    flash("您的邮箱或密码输入错误,请重新输入", "error")
    return render_template('login.html', form=form)


@front.route("/register/boss",methods=["GET","POST"])
def register_boss():
    form=RegisterForm()
    if form.validate_on_submit():
        form.create_bose()
        flash('注册成功，请登录！', 'success')
        return redirect(url_for('.login'))
    return render_template('register_boss.html', form=form)

@front.route("/register/user",methods=["GET","POST"])
def register_user():
    form=RegisterForm()
    if form.validate_on_submit():
        form.create_user()
        flash('注册成功，请登录！', 'success')
        return redirect(url_for('.login'))
    return render_template('register_user.html', form=form)