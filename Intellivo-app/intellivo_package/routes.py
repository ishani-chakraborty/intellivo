from flask import render_template, request, url_for, flash, redirect # import the Flask class
from intellivo_package import app, db, bcrypt, socketio
from intellivo_package.models import User, UserPref
from intellivo_package.forms import RegistrationForm, LoginForm, ProfileForm
from flask_login import login_user, current_user, logout_user, login_required

# home page 
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title='Home')

# about page 
@app.route("/about")
def about():
    return render_template('about.html', title='About')

# register page 
@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('user'))
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
   
# login page  
@app.route("/login", methods=['GET', 'POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            next_page = request.args.get('next') # redirect to next page if it exits (user tried accessing and is now logging in)
            return redirect(next_page) if next_page else redirect(url_for('profile'))
        else:
            flash('Login unsucessful. Please check credentials.', 'danger')
    return render_template('login.html', title='Login', form=form)

# Preferences form (connected to UserPref). Access through profile page
@app.route("/preferences",  methods=['GET', 'POST'])
def preferences():
    form=ProfileForm()
    if form.validate_on_submit():
        if current_user.is_authenticated:
            # check if row with user_id already exists. if exits, update row. else make new row 
            user=current_user
            if UserPref.query.filter_by(user_id = user.id).first():
                UserPref.query.filter_by(user_id = user.id).delete()
            userpref = UserPref(age=int(form.age.data), spirituality=int(form.spirituality.data), location=int(form.location.data), 
                                engagement=int(form.engagement.data), user=user)
            db.session.add(user)
            db.session.commit()
        return redirect(url_for('profile')) # was 'home'
    return render_template('form.html', title='Preferences', form=form)

# profile page 
@app.route("/profile")
@login_required
def profile():
    user = current_user
    userpref = UserPref.query.filter_by(user_id = user.id).first()
    return render_template('profile.html', title='Profile', userpref=userpref)

# logout 
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

#################### chat routes ####################
@app.route('/chat', methods=["POST", "GET"])
@login_required
def user():
    return render_template('userChats.html', title='User Home')

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)

#################### end chat routes ####################