from flask_wtf import FlaskForm
from sqlalchemy import table
from sqlalchemy.sql.functions import current_user
from wtforms import SelectField, StringField, PasswordField, SubmitField, BooleanField, FloatField, TextAreaField, \
    IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, InputRequired

# 注册校验
from app import User


class RegistrationForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(), Length(3, 30, message="请输入6到30位的用户名")])
    password = PasswordField('密码', validators=[DataRequired(), Length(6, 30, message="请输入6到30位的密码")])
    email = StringField('邮箱', validators=[Email(message="请输入正确的邮箱类型")])  # test@qq.com
    confirm = PasswordField('确认密码', validators=[EqualTo('password', message="两次密码输入不一致")])
    submit = SubmitField('注册')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已经存在')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('该邮箱已经被注册,请选用其它邮箱')


# 登录校验
class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(), Length(3, 30, message="请输入6到30位的用户名")])
    password = PasswordField('密码', validators=[DataRequired(), Length(6, 30, message="请输入6到30位的密码")])
    remember = BooleanField('记住我')
    submit = SubmitField('登录')


# 收货人地址表单验证
class CustomerDetailForm(FlaskForm):
    consignee = StringField("收货人姓名", validators=[InputRequired(), Length(max=20, min=2)])
    address = StringField("收货地址", validators=[InputRequired(), Length(min=10, max=40)])
    telephone = StringField("电话", validators=[InputRequired(), Length(max=20, min=9)])
    submit = SubmitField("添加地址")


# 地址更新
class UpdateCustomerDetailForm(FlaskForm):
    consignee = StringField("收货人姓名", validators=[InputRequired(), Length(max=20, min=2)])
    address = StringField("收货地址", validators=[InputRequired(), Length(min=10, max=40)])
    telephone = StringField("电话", validators=[InputRequired(), Length(max=20, min=9)])
    submit = SubmitField("修改地址")


# 安全校验
class SecurityCheck(FlaskForm):
    password = PasswordField('密码', validators=[DataRequired()])
    submit = SubmitField('验证身份')


# 用户信息更新
class UpdateInfo(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('邮箱', validators=[DataRequired(), Email()])
    submit = SubmitField('更新用户名和邮箱')

    def validate_username(self, username):
        user = table.query.filter_by(username=username.data).first()
        if user and user.username != current_user.username:
            raise ValidationError("这个用户名已经被用过了，换一个吧！")

    def validate_email(self, email):
        user = table.query.filter_by(email=email.data).first()
        if user and user.username != current_user.username:
            raise ValidationError("这个邮箱已经被用过了，换一个吧！")


