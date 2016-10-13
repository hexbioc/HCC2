from flask_wtf import Form 
from wtforms import RadioField,StringField,PasswordField,SubmitField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import USER
from .. import mysql


class LoginForm(Form):
	patientType = RadioField('Status :',choices=[('1','Student'),('2','Employee')])
	ID 		 = StringField("ID ",validators=[Required()])
	password = PasswordField("Password",validators=[Required()])
	submit   = SubmitField("Log in")



class RegistrationForm(Form):
	ID 		 	= StringField('ID',validators=[Required()])
	patientType = RadioField('Status :',choices=[('1','Student'),('2','Employee')])
	name 	 	= StringField('Full Name',validators=[Required()])
	email 	 	= StringField('Email',validators=[Required(),Email()])
	password 	= PasswordField('Password',validators=[Required()])
	password2	= PasswordField('Confirm Password',validators=[Required(),EqualTo('password',message='Password mismatch!')])
	submit   	= SubmitField('Register')

	'''def validate_email(self,field):
		cursor = mysql.connect().cursor()
		if USER.checkIfEmailExists(cursor,field.data):
			raise ValidationError('Email already registered.')

	def validate_ID(self,field):
		cursor = mysql.connect().cursor()
		if USER.checkIfIDExists(cursor,field.data):
			raise ValidationError('ID already registered.')
		tuple = USER.checkIfExistsInDB(cursor, self.patientType.data, field.data, self.email.data)
		if tuple is None:
			raise ValidationError('ID not recognized . probably this ID isnt present in College Database')
'''

			
