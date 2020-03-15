from datetime import datetime
from app import db
from flask_login import UserMixin


# 管理员
class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    sex = db.Column(db.String(2), nullable=False)
    password = db.Column(db.String(6), nullable=False)
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)


# 用户
class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(6), nullable=False)
    sex = db.Column(db.String(2), nullable=False)
    email = db.Column(db.String(30), unique=True)
    address = db.Column(db.String(30), unique=True)
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)


# 商品
class Goods(db.Model, UserMixin):
    __tablename__ = "goods"
    id = db.Column(db.Integer, primary_key=True)
    goodsname = db.Column(db.String(255), nullable=False)
    sort = db.Column(db.String(40), nullable=False, default="尚未填写")
    goods_dec = db.Column(db.String(255))
    goods_price = db.Column(db.Integer, nullable=False)
    goods_pics = db.Column(db.String(255))
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)


# 订单
class Orders(db.Model, UserMixin):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    goodsname = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    account_price = db.Column(db.Integer, nullable=False)
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)


# 购物车
class Cart(db.Model):
    __tablename__ = "cart"
    id = db.Column(db.Integer, primary_key=True)
    goods_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)


# 收藏
class Collection(db.Model):
    __tablename__ = "collection"
    id = db.Column(db.Integer, primary_key=True)
    goods_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)

# db.drop_all()
# db.create_all()
