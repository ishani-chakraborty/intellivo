from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired, Length, Email, EqualTo

# class inherits FlaskForm 
class RegistrationForm(FlaskForm):
	username = StringField('Username', 
							validators=[DataRequired(), Length(min=2, max=20)]
							)
	email = StringField('Email',
						validators=[DataRequired(), Email()]
						)
	password = PasswordField('Password',
							validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password',
									validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
	email = StringField('Email',
						validators=[DataRequired(), Email()])
	password = PasswordField('Password',
							validators=[DataRequired()])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Log In')

class ProfileForm(FlaskForm):
	firstname = StringField(u'First Name', 
							validators=[DataRequired(), Length(min=2, max=40)], 
							description=u"(First name only")
	age = SelectField(u"Your Age: ", [DataRequired()],
            choices=[("0", ""), ("1", "Under 18"), ("2", "18-25"), ("3", "26-40"), ("4", "40+")],
            description=u"(Select an age range.)",
            render_kw={})
	spirituality = SelectField(u"How would you describe your belief in a higher power?", [DataRequired()],
            choices=[("0", ""), ("0", "atheist"),("py", "agnostic"), ("rb", "spiritual but not religious"), ("js", "spiritual but also religious"),
            		("0", "devout religious")],
            description=u"(How spiritual are you?)",
            render_kw={})
	location = SelectMultipleField(u"Location: ", [],
            choices=[("rb", "West Coast (US)"), ("js", "Mountain Region (US)"), ("js", "Midwest (US)"), ("js", "East Coast (US)"), ("py", "Canada"), 
            		("js", "South America"),("js", "Mexico"), ("js", "East Coast"), ("js", "Europe"), ("js", "Africa"), 
            		("js", "Western Asia"), ("js", "Eastern Asia"), ("js", "Southern Asia"),("js", "Australia"),("js", "Other"),],
            description=u"(Your general place of residence)",
            render_kw={"multiple": "multiple"})
	engagement = SelectField(u"When newsworthy things are happening in the world, at what level do you engage?", [DataRequired()],
            choices=[("0", ""), ("py", "I do not engage"), ("rb", "I educate myself to understand the gist of it"), 
            		("js", "In addition to educating myself, I initiate hard conversations with family and friends"),
            		("py", "I participate in community-wide events surrounding social justice issues"),
            		("py", "I am a full on activist: I organize events, create social media content, etc.")],
            description=u"(Your engagement to events around you.)",
            render_kw={})

	submit = SubmitField('Save')
