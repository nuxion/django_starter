# Django starter project

This is a starter project for Django which integrate REST APIs, Javascript ecosystem and traditional html rendering using django. 

The project aims to understand how to integrate a client like javascript or mobile to the auth system provided by django introducing the least amount of modifactions to it. 

From the javascript perspective, the library could use Session type authentication if the requests to the API are made from the django context.

## Features

- Django rest framework
- OpenApi 3.0
- OAuth 2.0 with Google and Github as providers
- JWT tokens
- Javascript integration through Vite
- Tailwindcss framework

## Auth system

The project includes their own User model extended from AbstractUser. 
Email is used as unique identifier for a user.

## Dir structure

- `core`: core to the app like the auth system, REST configuration, admin, and so on
- `theme`: related to javascript ecosystem and tailwdin
- `home`: `_base.html` layout and landing page
- `dist`: collected static content from django and vite build process

## Build

As simple shortcut:

```
make build
```

The build process has several steps:
1. Built a python docker image, it is prepared to run django with gunicorn
2. Built a nodejs docker image to compile javascripts files and tailwind styles
3. Collect static content in the `dist` folder

## Devlopment server

Two process are needed: Django runserver and vite dev server. 

Running manually:
In two different terminals you should run:

`python manage.py runserver` 

`yarn dev`

Or only in one terminal:
`python3 src/run.py`


## TODO

- [ ] Testing
- [ ] CORS Headers
- [ ] CSRF requests from javascript
- [x] Docker Production deploy



