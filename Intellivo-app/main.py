from flask import Flask, render_template, request, url_for, flash, redirect# import the Flask class
from flask_sqlalchemy import SQLAlchemy #orm to run queries 
from forms import RegistrationForm, LoginForm, ProfileForm

import os

app = Flask(__name__) # set app variable to an instance of the flask class

# create secret key
app.config['SECRET_KEY']='a27adadd2e3e4bb099e737cd7c3257e4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # chose your database

db = SQLAlchemy(app)

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

def init_db():
    db.create_all()

class User(db.Model):
    first_name = db.Column(db.String(80), unique=False, nullable=False, primary_key=True)
    age = db.Column(db.Integer, unique=False, nullable=False, primary_key=True)
    spirituality = db.Column(db.Integer, unique=False, nullable=False, primary_key=True)
    location = db.Column(db.Integer, unique=False, nullable=False, primary_key=True)
    engagement = db.Column(db.Integer, unique=False, nullable=False, primary_key=True)

    def __repr__(self):
        return "<First Name: {} Age: {} Spirituality: {} Location: {} Engagement: {}>".format(self.first_name, self.age, self.spirituality, self.location, self.engagement)


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
                return redirect(url_for('user')) # was 'home'
            else:
                flash('Login unsucessful. please check credentials', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/user")
def user():
    return render_template('userChats.html', title='User Home')

@app.route("/preferences",  methods=['GET', 'POST'])
def preferences():
    form=ProfileForm()
    if form.validate_on_submit():
        print(form.firstname.data, form.age.data, form.spirituality.data, form.location.data, form.engagement.data)
        user = User(first_name=form.firstname.data, age=int(form.age.data), spirituality=int(form.spirituality.data), location=int(form.location.data), engagement=int(form.engagement.data))
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('user')) # was 'home'
    return render_template('form.html', title='Preferences', form=form)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)

