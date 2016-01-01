from flask.ext.wtf import Form
from flask_wtf import Form, RecaptchaField
from flask_wtf.html5 import IntegerField, TelField, TelInput
from wtforms import StringField, BooleanField, TextField, validators
from wtforms.fields.html5 import URLField
from wtforms.validators import DataRequired, url

class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

class LinkForm(Form):
    url = URLField(validators=[url()])
    phone = IntegerField('mobilephone', [validators.NumberRange(min = 0, max = 11)])

class SignupForm(Form):
    username = TextField('Username')
    recaptcha = RecaptchaField()
