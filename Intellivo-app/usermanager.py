import os

from flask import Flask
from flask import render_template
from flask import request

from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "userdatabase.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)

class User(db.Model):
    first_name = db.Column(db.String(80), unique=False, nullable=False, primary_key=True)
    age = db.Column(db.String(80), unique=False, nullable=False, primary_key=True)
    religion = db.Column(db.String(80), unique=False, nullable=False, primary_key=True)

    def __repr__(self):
        return "<First Name: {} Age: {} Religion: {}>".format(self.first_name, self.age, self.religion)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.form:
        user = User(first_name=request.form.get("first_name"), age=request.form.get("age"), religion=request.form['atheist'])
        db.session.add(user)
        db.session.commit()
    users = User.query.all()
    return render_template("profile.html", users=users)


  
if __name__ == "__main__":
    app.run(debug=True)
