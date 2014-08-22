from flask.ext.wtf import Form
from flask.ext.wtf.recaptcha import RecaptchaField
from wtforms.fields import StringField, SubmitField, HiddenField
from wtforms.validators import DataRequired


class searchform(Form):
  local_number = StringField("NUMBER", validators=[DataRequired()], id='numbers') 
  cc = StringField("COUNTRY CODE", validators=[DataRequired()], id='numbers')
  #recap = RecaptchaField()

class emailForm(Form):
	email = StringField("Email", validators=[DataRequired()])
	recap = RecaptchaField()
