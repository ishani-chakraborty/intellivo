from flask import render_template, request, url_for, flash, redirect# import the Flask class
from intellivo_package import app, db, bcrypt 
from intellivo_package.models import User, UserPref
from intellivo_package.forms import RegistrationForm, LoginForm, ProfileForm
from flask_login import login_user

# db for chat preference form 
# class ChatPreferences(db.Model):
    # preferences = db.relationship('Preference', backref='author') # lazy=dynamic?
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    # include columns for actual preferences from form here 

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
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(firstname=form.firstname.data, lastname=form.lastname.data, email=form.email.data,
                    password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created. You are now able to log in!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
    
@app.route("/login", methods=['GET', 'POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('user'))
        else:
            flash('Login unsucessful. Please check credentials.', 'danger')
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
