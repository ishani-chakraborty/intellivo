## Structure of intellivo-app 

### This directory contains the content for the flask app. The structure is as follows: 

```bash
.
├── README.md
├── forms.py
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
│       ├── profile.html
│       ├── register.html
│       └── userChats.html
├── run.py
├── userdatabase.db
└── usermanager.py
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
 - Flask SQLAlchemy (pip install -U Flask-SQLAlchemy)
2. In terminal: 
```bash
export FLASK_APP=main.py
flask run -h localhost -p (port you want to run application on)
```
Or you can do: 
```bash
python run.py
```

