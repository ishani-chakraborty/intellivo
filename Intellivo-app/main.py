from flask import Flask, render_template, url_for, flash, redirect# import the Flask class
from flask_sqlalchemy import SQLAlchemy #orm to run queries 
from forms import RegistrationForm, LoginForm

app = Flask(__name__) # set app variable to an instance of the flask class

#create secret key
app.config['SECRET_KEY']='a27adadd2e3e4bb099e737cd7c3257e4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # chose your database

# db = SQLAlchemy(app)

# class User(db.Model):
# 	id = db.Column(db.Integer, primary_key=True)
# 	username = db.Column(db.String(20), unique=True, nullable=False)
# 	fistname = db.Column(db.String(40), nullable=False)
# 	lastname = db.Column(db.String(40))
# 	email = db.Column(db.String(120), unique=True, nullable=False)
# 	password = db.Column(db.String(60), nullable=False)

# 	def __repr__(self):
# 		return f"User('{self.username}', '{self.email}', '{self.email}')"

# db for chat preference form 
# class ChatPreferences(db.Model):
	# preferences = db.relationship('Preference', backref='author') # lazy=dynamic?
	# user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	# include columns for actual preferences from form here 


# blog data 
posts = [
	{
		'author': 'Chelsea Fernandes',
		'title': 'How to be more Cool',
		'content': 'First post in a series',
		'date_posted': 'July 5, 2020'
	},
	{
		'author': 'Hannah Fernandes',
		'title': 'Blog Post',
		'content': 'My life in a blog',
		'date_posted': 'June 22, 2020'
	}

]


@app.route("/") # home page 
@app.route("/home")
def home():
	return render_template('home.html', title='Home')



@app.route("/about") # home page 
def about():
	return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
 	form = RegistrationForm()
 	if form.validate_on_submit():
 		flash(f'Account created for {form.username.data}!', 'success')
 		return redirect(url_for('home'))
 	return render_template('register.html', title='Register', form=form)
	
@app.route("/login", methods=['GET', 'POST'])
def login():
	form=LoginForm()
	if form.validate_on_submit():
			if form.email.data == 'admin@log.com' and form.password.data == 'password':
				flash('You have been logged in!', 'success')
				return redirect(url_for('home'))
			else:
				flash('Login unsucessful. please check credentials', 'danger')
	return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
	app.run(debug=True)

