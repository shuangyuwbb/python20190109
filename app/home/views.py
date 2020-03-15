from flask import request, render_template, redirect, url_for, flash
from sqlalchemy.sql.functions import current_user
from flask_login import current_user, logout_user, login_user
from app import db
from app.home.forms import RegistrationForm, LoginForm
from app.models import User, Goods, Cart, Collection,Orders
from . import home
from app.pojo import query_goods, queryId, add_cart_collection, login_required, queryKey,querymohu
from app.pojo import del_cart_collection,queryClassfy
from flask import jsonify


# 首页
@home.route('/')
def index():
    goods = query_goods(Goods)
    return render_template("home/index.html", goods=goods)

# 主页

@home.route('/main/')
@login_required
def main():
    goods = query_goods(Goods)
    return render_template("home/main.html", username=current_user.username, goods=goods)


# 详情页
@home.route('/detail/<int:id>/')
@login_required
def detail(id):
    content = Goods.query.get(id)
    return render_template('home/detail.html', content=content)


# 注册
@home.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        u = User(username=username, password=password, email=email)
        db.session.add(u)
        db.session.commit()
        flash('Your account has been created,now you can login in!', 'success')
        return redirect(url_for('home.login'))
    else:
        return render_template('home/register.html', form=form)


# 登录
@home.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        remember = form.remember.data
        user = User.query.filter_by(username=username).first()
        if not user:
            flash('该用户不存在')
        elif User.query.filter_by(password=password).first():
            login_user(user, remember=remember)
            return redirect(request.args.get('next') or url_for('home.main'))
        else:
            flash('无效的密码')
    return render_template('home/login.html', title='Login', form=form)


# 退出
@home.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for('home.index'))


# 添加购物车
@home.route('/cart/<int:id>/')
@login_required
def addCart(id):
    user_id = current_user.id
    if id == 1:
        col = queryKey(Cart, user_id)
        col = list(col)
        li = []
        for i in range(len(col)):
            content = queryId(Goods, col[i].goods_id)
            li.append(content)
        if not len(li):
            flash("赶快去找找喜爱的宝贝吧！")
        return render_template('home/cart.html', content=li)
    else:
        add_cart_collection(Cart, id)
        flash("添加成功")
        return redirect(url_for("home.detail",id=id))


# 收藏商品

@home.route('/collection/<int:id>/')
@login_required
def collection(id):
    user_id = current_user.id
    if id == 1:
        col = queryKey(Collection, user_id)
        col = list(col)
        li = []
        for i in range(len(col)):
            content = queryId(Goods, col[i].goods_id)
            li.append(content)
        if not len(li):
            flash("赶快去找找喜爱的宝贝吧！")
        return render_template('home/collection.html', content=li)
    else:
        add_cart_collection(Collection, id)
        flash("收藏成功")
        return redirect(url_for("home.detail",id=id))

# 关键字查找
@home.route('/search/',methods=['GET'])
def searchKey():
    keyword = request.args.get('keyword')
    data = querymohu(keyword)
    return render_template('home/search.html',content=data)

# 从购物车表中移除
@home.route('/del_cart/<int:id>/')
def del_cart(id):
    del_cart_collection(Cart,id)
    flash("移除成功")
    return redirect(url_for('home.addCart',id=1))

# 从收藏表表中移除
@home.route('/del_col/<int:id>/')
def del_col(id):
    del_cart_collection(Collection,id)
    flash("移除成功")
    return redirect(url_for('home.collection',id=1))

# 购买
@home.route('/buy/<int:id>/')
def buy(id):
    data = queryId(Goods, id)
    order = Orders(username=current_user.username,goodsname=data.goodsname,address=current_user.address,account_price=data.goods_price)
    db.session.add(order)
    db.session.commit()
    data = queryId(Goods, id)
    return render_template('home/pay.html',content=data)

# 分类查找
@home.route('/classfy/<string:keyword>')
def classfy(keyword):
    data = queryClassfy(keyword)
    print(data)
    return render_template('home/classfy.html',content=data)

