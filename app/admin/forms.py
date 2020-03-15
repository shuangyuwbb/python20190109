from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FloatField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, InputRequired, EqualTo, Length


# 商品表单
class ProductForm(FlaskForm):
    name = StringField('商品名称', validators=[DataRequired(), Length(min=2, max=40)])
    sort = StringField('商品类别', validators=[DataRequired(), Length(min=2, max=40)])
    price = FloatField("商品价格", validators=[DataRequired()])
    detail = TextAreaField('商品细节', validators=[DataRequired(), Length(min=1, max=140)])
    start_count = IntegerField("初始库存", validators=[DataRequired()])
    confirm = IntegerField("确认初始库存", validators=[DataRequired(), EqualTo("start_count")])
    submit = SubmitField("添加商品")


# 添加商品
class AddProductCountForm(FlaskForm):
    count = IntegerField("增加的库存量", validators=[InputRequired()])
    confirm = IntegerField("确认增加的库存量", validators=[InputRequired(), EqualTo("count")])
    submit = SubmitField("添加库存")


# 更新密码
class UpdatePasswordForm(FlaskForm):
    password = PasswordField('密码', validators=[DataRequired(), Length(min=6, max=20)])
    confirm_password = PasswordField('确认密码',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('更新密码')
