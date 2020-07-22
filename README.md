# Intellivo 

## Introduction

Intellivo is a web application built with the Flask framework. The app facilitates an intellectual conversation between two users by providing starter questions in the chat room. Our matching algorithm intelligently matches users based on differences, similar to the idea behind a dating-app. 

## Why Intellivo?

While important intellectual conversations have been happening on social media platforms, the problem is that these difficult discussions tends to happen over social media, where we have platforms such as Instagram composed of friends and other like-minded individuals whose beliefs and values tend to align with their own. Intellivo works to elimintate the creation of this echo chamber by providing a safe place to both better educate ourselves and understand the origins of various perspectives. 

## Our Awesome Team

* [Madhu Akula](https://github.com/madhuakula) - mentor 
* [Jake Schechner](https://github.com/JSchechner) - mentor 
* [Chelsea Fernandes](https://github.com/ccfernandes) - product manager
* [Ishani Chakraborty](https://github.com/ishani-chakraborty) - software developer
* [Sejal Dua](https://github.com/sejaldua) - software developer
* [Cindy Ramirez](https://github.com/ramir262) - software developer
* [Adeline Leung](https://github.com/adelineleung) - UI/UX designer 

## Setup

There are 4 main features that we want to have implemented for our MVP

1. User authentication - Oauth 2.0  
2. Chat room backend - Flask-SocketIO & SQLALCHEMY 
3. Matching algorithm - Principle Component Analysis + K-Means Clustering in Python 
4. Website interface - Flask, HTML, CSS, Bootstrap 

## The simplest Docker setup

* Anyone can pull the docker image and quickly run locally using the below command

```bash
docker run --name intellivo-app -p 5000:5000 ishanichakraborty1/intellivo
```

* Then navigate to the [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Roadmap

This project is part of the internHacks 2020, a 6-week hackathon. 

Week 1: ideation & basic design  
Week 2: initial architectural and visual design  
Week 3: work on tasks asynchronously  
Week 4: user testing and structural implementation of the app  
Week 5: integration  
Week 6: deployment & design considerations  

## Contributions

