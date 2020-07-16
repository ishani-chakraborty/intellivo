from flask import Flask 
from flask_sqlalchemy import SQLAlchemy #orm to run queries
from flask_bcrypt import Bcrypt 
from flask_login import LoginManager

app = Flask(__name__) # set app variable to an instance of the flask class
app.config['SECRET_KEY']='a27adadd2e3e4bb099e737cd7c3257e4' # create secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///intellivoUser.db' # chose your database

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login' # to redirect users to login if they haven't already 
login_manager.login_message_category = 'info' # for alert to login 


from intellivo_package import routes 