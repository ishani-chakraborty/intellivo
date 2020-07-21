## Structure of intellivo-app 

### This directory contains the content for the flask app. The structure is as follows: 

```bash
.
├── README.md
├── intellivo_package
│   ├── __init__.py
│   ├── forms.py
│   ├── intellivoUser.db
│   ├── models.py
│   ├── routes.py
│   ├── static
│   │   ├── assets
│   │   │   ├── logo\ icon.jpg
│   │   │   └── logo.png
│   │   └── main.css
│   └── templates
│       ├── README.md
│       ├── about.html
│       ├── form.html
│       ├── home.html
│       ├── layout.html
│       ├── login.html
│       ├── prefForm.html
│       ├── profile.html
│       ├── register.html
│       └── userChats.html
├── old
│   ├── forms.py
│   ├── userdatabase.db
│   └── usermanager.py
├── requirements.txt
└── run.py
```

* intellivoUser.db - current database being used 
* models.py - contains classes for app's databases
* routes - all website urls 
* run.py - main python file, used to run the app 
* forms.py - where all user forms are configured
* templates - the html files that can have embedded jinja (language to connect with flask app data)
* static - currently just has the main.css file 
* assets - all logos, images 

## To Run Application 

1. Make sure Flask and all dependencies are installed 
 - Flask 
 - Flask-SQLAlchemy (pip install -U Flask-SQLAlchemy)
   - database ORM
 - Flask login (pip install flask-login)
   - for login validation
 - Flask-Bcrypt (pip install bcrypt)  
   - for password encryption 
 - Flask-SocketIO (pip install -U flask-socketio)
   - for chatting via web sockets
 - Flask-WTF (pip install Flask-WTF)
   - for login, registration, and preference forms 
2. In terminal: 
```bash
export FLASK_APP=run.py
export export FLASK_DEBUG=1 
flask run -h localhost -p (port you want to run application on)
```
Or you can do: 
```bash
python run.py
```

