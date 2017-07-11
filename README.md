# UrlShortener
[![forthebadge](http://forthebadge.com/badges/built-with-swag.svg)](http://forthebadge.com)     
[![Build Status](https://travis-ci.org/p53ud0k0d3/UrlShortener.svg?branch=master)](https://travis-ci.org/p53ud0k0d3/UrlShortener)     [![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)


# URL Shortener Intro

Shortens Lengthy URLs.
Allows to choose from a number of hosts for shortening.

## Getting Started

Start your own virtual environment:

```
mkdir shortURLapp
```
```
cd shortURLapp
```
pip install virtualenvironment.
```
virtualenv myvenv
source myvenv/bin/activate
```
clone the repository

### Prerequisites
Install the dependencies:

```
pip install -r requirements.txt
```



### Installing



Apply the migrations:
```
cd UrlShortener
```
```
python manage.py migrate
```

run the server
```
python manage.py runserver
```

goto:

  127.0.0.1:8000
