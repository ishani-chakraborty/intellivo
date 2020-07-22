FROM python:3
LABEL MAINTAINER="Team Intellivo"

ENV FLASK_APP=run.py

COPY Intellivo-app /intellivo-app
COPY matching-algorithm /intellivo-app/matching-algorithm

WORKDIR /intellivo-app

RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "flask", "run", "--host", "0.0.0.0" ]
