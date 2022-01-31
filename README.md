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

## TODO

- [ ] Testing
- [ ] CORS Headers
- [ ] CSRF requests from javascript
- [ ] Docker Production deploy



