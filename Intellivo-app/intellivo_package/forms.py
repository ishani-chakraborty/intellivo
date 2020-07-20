from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from intellivo_package.models import User 


# class inherits FlaskForm 
class RegistrationForm(FlaskForm):
	firstname = StringField('Firstname', 
							validators=[DataRequired(), Length(min=2, max=20)]
							)
	lastname = StringField('Lastname', 
							validators=[DataRequired(), Length(min=2, max=40)]
							)
	email = StringField('Email',
						validators=[DataRequired(), Email()]
						)
	password = PasswordField('Password',
							validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password',
									validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Sign Up')

	# determines if email is unique/already taken
	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('Email is taken. Register with a new one or log in.')



class LoginForm(FlaskForm):
	email = StringField('Email',
						validators=[DataRequired(), Email()])
	password = PasswordField('Password',
							validators=[DataRequired()])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Log In')

class ProfileForm(FlaskForm):
	age = SelectField(u"Your Age: ", [DataRequired()],
            choices=[("1", "Under 18"), ("2", "18-25"), ("3", "26-40"), ("4", "40+")],
            description=u"(Select an age range.)",
            render_kw={})
	spirituality = SelectField(u"How would you describe your belief in a higher power?", [DataRequired()],
            choices=[("1", "atheist"),("2", "agnostic"), ("3", "spiritual but not religious"), ("4", "spiritual but also religious"),
            		("5", "devout religious")],
            description=u"(How spiritual are you?)",
            render_kw={})
	location = SelectField(u"Location: ", [],
            choices=[("1", "West Coast (US)"), ("2", "Mountain Region (US)"), ("3", "Midwest (US)"), ("4", "East Coast (US)"), ("5", "Canada"), 
            		("6", "South America"),("7", "Mexico"), ("8", "East Coast"), ("9", "Europe"), ("10", "Middle East"), ("11", "Africa"), 
            		("12", "Western Asia"), ("13", "Eastern Asia"), ("14", "Southern Asia"),("15", "Australia"),("16", "Other"),],
            description=u"(Your general place of residence)")
	engagement = SelectField(u"When newsworthy things are happening in the world, at what level do you engage?", [DataRequired()],
            choices=[("1", "I do not engage"), ("2", "I educate myself to understand the gist of it"), 
            		("3", "In addition to educating myself, I initiate hard conversations with family and friends"),
            		("4", "I participate in community-wide events surrounding social justice issues"),
            		("5", "I am a full on activist: I organize events, create social media content, etc.")],
            description=u"(Your engagement to events around you.)",
            render_kw={})

	submit = SubmitField('Save')
