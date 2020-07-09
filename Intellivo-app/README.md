## Structure of intellivo-app 

### This directory contains the content for the flask app. The structure is as follows: 
* main.py - main python file, contains functions for website urls. 
* forms.py - where all user forms are configured
* templates - the html files that can have embedded jinja (language to connect with flask app data)
* static - currently just has the main.css file 
* assets - all logos, images 

## To Run Application 

1. Make sure Flask and all dependencies are installed 
 - Flask 
 - Flask SQLAlchemy (pip install -U Flask-SQLAlchemy)
2. In terminal: 
 - export FLASK_APP=main.py
 - flask run -h localhost -p <port you want to run application on>
 - (OR) python main.py 
