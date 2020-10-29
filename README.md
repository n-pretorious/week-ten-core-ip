# Projects awards
This is an awarding site. A user gets to grade projects posted.


## Core Features

* An admin can upload new profiles, photos and comments through an admin panel
* An admin can update the said above model details
* A user can register and setup a profile
* A user can view their profile to see their information
* A user can search for other users
* A user can follow and unfollow other users
* A user can view images of people they have followed on their timeline
* A user can view a post's details

## Prerequisites

* Python3
* Django
* Postgres

## Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone git@github.com/<username>/<project_name>.git
    $ cd <project_name>

## Usage

### Activate the virtual enviroment for your project

    $ python3 -m venv --without-pip virtual
    $ source virtual/bin/activate

Download the latest version of pip in virtual our environment

    $ curl https://bootstrap.pypa.io/get-pip.py | python

Install project dependencies:

    $ pip install -r requirements.txt

### Setup database

    $ psql
    $ CREATE TABLE <table_name>;

### Setup cloudinary

If you don't have an account proceed to [https://cloudinary.com/users/register/free] and register to get cloudinary account details

## Environment variables

The `ENVIRONMENT` variable loads the correct settings. Fill in the correct credentials

    ```.env
    CLOUD_NAME=''
    API_KEY=''
    API_SECRET=''
    SECRET_KEY=''
    DEBUG=bolean
    DB_NAME='instclone'
    DB_USER=''
    DB_PASSWORD=''
    DB_HOST=''
    MODE=''
    ALLOWED_HOSTS='*'
    DISABLE_COLLECTSTATIC=''
    ```

Then simply apply the migrations:

    $ python3 manage.py migrate
    $  python3 manage.py makemigrations <app_name>

Run tests:
    $ python3 manage.py test <app_name>

You can now run the development server:

    $ python3 manage.py runserver

## BDD

| BEHAVIOUR    | INPUT   |  OUTPUT |
| :------------- | :------------- | :--------------- |
| User scrolls | Scrolling y axis | Navbar appears |
| User clicks on a project | Click project | Project redirects to a page with the project|
| User clicks rate | Button clicked | Form to submit rating toggles|
| User inputs rating |  Number to represent rating | Number input shows |
| User submits rating | Click submit button  | Values become empty |

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Copyright (c) 2020 Pretorious Ndung'u
