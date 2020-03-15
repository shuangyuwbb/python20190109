# 新增商品
from functools import wraps
from flask import flash, redirect, url_for, request, session
from flask_login import current_user

from app import db, Goods


# 管理员后台添加商品
def add_goods(Md):
    pass


# 商品下架
def del_goods(id):
    pass


# 商品修改
def update_goods(id):
    pass


# 商品查询
def query_goods(Md):
    content = Md.query.filter().all()
    return content


# 枫叶查询
def query_goods_pag(Md):
    page = request.args.get('page', 1, type=int)
    pagination = Md.query.filter().paginate(page, per_page=7, error_out=False)
    data = pagination.items
    return data, pagination


# 通过id条件查找
def queryId(Md, id):
    data = Md.query.get(id)
    return data


# 根据属性查找
def queryKey(Md, Key):
    data = Md.query.filter(Key == Md.user_id)
    return data


# 模糊查找
def querymohu(keyword):
    data = Goods.query.filter(Goods.goods_dec.like("%" + keyword + "%") if keyword is not None else "").all()
    return data


# 分类查找
def queryClassfy(keyword):
    data = Goods.query.filter(Goods.sort.like("%" + keyword + "%") if keyword is not None else "").all()
    return data


# 添加收藏商品
def add_cart_collection(Md, id):
    goods_id = id
    user_id = current_user.id
    # 声明对象
    md = Md(goods_id=goods_id, user_id=user_id)
    # 调用添加方法
    db.session.add(md)
    # #提交入库
    db.session.commit()


# 生成订单
def create_order(Md):
    md = Md
    db.session.add(md)
    db.session.commit()


# 判断是否登录装饰器
def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if current_user.is_authenticated:
            return func(*args, **kwargs)
        else:
            return redirect(url_for('home.login'))

    return wrapper


# 判断是否登录装饰器
def admin_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if session.get('admin'):
            return func(*args, **kwargs)
        else:
            return redirect(url_for('admin.index'))

    return wrapper


# 从购物车表-收藏表中删除
def del_cart_collection(Md, id):
    li = []
    li.append(Md.user_id == current_user.id)
    li.append(Md.goods_id == id)
    md = Md.query.filter(*li).first()
    db.session.delete(md)
    db.session.commit()
