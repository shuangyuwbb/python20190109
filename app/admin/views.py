from os import abort

from flask import render_template, request, flash, redirect, url_for, session
from flask_login import current_user, login_user


from app.models import Goods, Admin, User, Orders
from app.pojo import login_required
from app.pojo.methods import query_goods_pag, admin_required
from . import admin



# 后台首页
@admin.route('/')
def index():
    return render_template('admin/login.html')


@admin.route('/main/<string:md>/', methods=['GET', 'POST'])
@admin_required
def main(md):
    Md = Goods
    if md == 'Goods':
        Md = Goods
    elif md == 'Admin':
        Md = Admin
    elif md == 'User':
        Md = User
    elif md == 'Order':
        Md = Orders
    print(Md)
    data, pagination = query_goods_pag(Md)
    print(data)
    return render_template('admin/index.html', username=session.get('admin'), data=data, pagination=pagination, md=md)


@admin.route('/login/', methods=['POST', 'GET'])
def Login():
    # result = face_first()
    # data = Admin.query.filter(name=result)
    # print(data)
    # if result == 'wbb':
    name = request.form.get('username')
    password = request.form.get('password')
    remember = request.form.get('remember')
    admin = Admin.query.filter_by(name=name).first()
    if not admin:
        flash('该用户不存在')
    elif Admin.query.filter_by(password=password).first():
        login_user(admin, remember=remember)
        session['admin'] = name
        return redirect(url_for('admin.main', md="Goods"))
    else:
        flash('无效的密码')
    return redirect(url_for('admin.main'))


@admin.route('/logout/')
def logout():
    session.pop("admin")
    return redirect(url_for('admin.index'))


# 添加商品
@admin.route('/addgoods/')
def addGoods():
    pass


# 删除商品
@admin.route('/del_goods/')
def delGoods():
    pass


# 删除用户
@admin.route('/del_uer/')
def delUser():
    pass


# 查询商品
@admin.route('/query/')
def queryGoods():
    pass


# 更新商品
@admin.route('/updata/')
def query(id):
    goods = Goods.query.get(id)
    # goods.goodsname =
