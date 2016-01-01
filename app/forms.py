from flask.ext.wtf import Form
from flask_wtf import Form, RecaptchaField
from wtforms import StringField, BooleanField, TextField
from wtforms.fields.html5 import URLField
from wtforms.validators import DataRequired, url


class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)


class LinkForm(Form):
    url = URLField(validators=[url()])
