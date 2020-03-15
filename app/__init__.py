import os

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

import pymysql

app = Flask(__name__)

login_manager = LoginManager()

login_manager.init_app(app)
pymysql.install_as_MySQLdb()

bootstrap = Bootstrap()
bootstrap.init_app(app)

db = SQLAlchemy()
db.init_app(app)
# app.config['SECRET_KEY'] = os.urandom(24) # 随机产生24位的字符串作为SECRET_KEY
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@localhost:3306/cjsc?charset=utf8"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config["SECRET_KEY"] = "12345678"

# print("创建数据")
from app.models import Goods, User, Goods


class Config(object):
    SQLALCHEMY_DATABASE_URI = "mysql://root:123456@localhost:3306/cjsc"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


app.config.from_object(Config)

from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix="/admin")


@app.errorhandler(404)
def page_not_found(error):
    return render_template("home/404.html"), 404


@login_manager.user_loader  # 这是个回调函数  也就是登录成功以后回来调用
def load_user(uid):
    return User.query.get(int(uid))
