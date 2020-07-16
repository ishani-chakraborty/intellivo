from intellivo_package import db, login_manager
from flask_login import UserMixin


def init_db():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(40), nullable=False)
    lastname = db.Column(db.String(40))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    pref = db.relationship('UserPref', backref='user', uselist=False) # one to one relationship

    def __repr__(self):
        return f"User('{self.firstname}', '{self.lastname}', '{self.email}')"

class UserPref(db.Model):
    age = db.Column(db.Integer, unique=False, nullable=False, primary_key=True)
    spirituality = db.Column(db.Integer, unique=False, nullable=False, primary_key=True)
    location = db.Column(db.Integer, unique=False, nullable=False, primary_key=True)
    engagement = db.Column(db.Integer, unique=False, nullable=False, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True)

    def __repr__(self):
        return f"UserPref('{self.age}', '{self.spirituality}', '{self.location}', '{self.engagement}')"
