# UrlShortener 
[![forthebadge](http://forthebadge.com/badges/built-with-swag.svg)](http://forthebadge.com)     
[![Build Status](https://travis-ci.org/p53ud0k0d3/UrlShortener.svg?branch=master)](https://travis-ci.org/p53ud0k0d3/UrlShortener)     [![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)

A Django web app that shortens long urls. User may select from a list of available hosts. 

#### Available Hosts
- Tinyurl
- Is.gd
- Bit.ly
- Google URL Shortener
- Rebrand.ly

## Pre-reqs

[Virtualenv](https://virtualenv.pypa.io/en/stable/) - Install required packages in a virtual enviroment. Not necessary, but recommended. 

## Installation

1. `virtualenv YOURENVNAME` - Create new virtualenv for this project
2. Navigate to directory containing 'requirements.txt'
3. `pip install -r requirements.txt` - Install required packages

## Usage


On first usage you'll need to apply database migrations: `python manage.py migrate`

Otherwise run development server using: `python manage.py runserver`

## Testing

Tests are run using `pytest`

For more information: [pytest](https://docs.pytest.org/en/latest/contents.html)

## Docker

Containerized version of the shoretener application for easy build/run process

This build is based on Docker python:3.6-alpine image and uses docker-compose to simplify the commands

Follow this link for docker installer [Docker](https://www.docker.com/community-edition#/download)
Download and Install docker for your Operating system

For more information, visit: [docker-compose](https://docs.docker.com/compose/overview/)


### Build
1. Run `docker-compose build` in the project directory

### Test
1. Run `docker-compose up test` to run test

### Run
1. Run `docker-compose up shortener` to run the application with console output
2. Run `docker-compose up -d shortener` to run the application without console output
3. Browse to `127.0.0.1:5000` to access the application
4. Edit line `"5000:5000"` to `"<your-port>:5000"` to run application in a different port 
    Docker container runs the application on port 5000 but the port can be mapped to any port

## Contributions
### Getting Started
1. Create a fork and then clone your fork of the repo
2. Follow steps for [Installation](#installation)
3. Ensure project runs: [Usage](#usage)
4. Ensure tests pass: [Testing](#testing)
5. Implement your changes along with tests for your change
6. Push changes to your fork and submit a pull request


### Adding a new host
This project uses the pyshorteners library for url shortening, read their documentation for more information on implementing a new host: [pyshorteners](http://www.ellison.rocks/pyshorteners/)
