# Iseult McCormack Creations

Iseult McCormack Creations is an online store where she can sell her art.

Website Links : [Iseult McCormack Creations](https://iseult-mccormack-shop.herokuapp.com/)

---

---

## Authors

## Technologies

### Core Languages, Frameworks, Editors

- [HTML 5](https://en.wikipedia.org/wiki/HTML) ~ Markup language designed to be displayed in a web browser.
- [CSS 3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) ~ Style sheet language used for describing the presentation of a document in HTML.
- [Python 3.9.2](https://code.jquery.com/) ~ High-level, general-purpose programming language.
- [Django 3.2.1](https://www.djangoproject.com/) ~ Django is a high-level Python Web framework.
- [jQuery 3.5](https://code.jquery.com/) ~ lightweight JavaScript library.
- [Bootstrap 4.6](https://getbootstrap.com/) ~ Design and customize responsive mobile-first sites.
- [Heroku](https://heroku.com) ~ A cloud based platform - as a service enabling deployment of CRUD applications
- [Heroku Postgres](https://www.heroku.com/postgres) ~ PostgreSQL's capabilities - as a fast, functional, and powerful data resource.

#### Third-Party Tools

- [GitHub](https://github.com/) ~ Distributed version control and source code management (SCM) functionality of Git, plus its own features.
- [Font Awesome](https://fontawesome.com/) ~ Font Awesome icons
- [Cloudinary](https://cloudinary.com/) ~ Cloud-based image and video management platform
- [Git](https://git-scm.com/) ~ Distributed version control system
- [autopep8](https://pypi.org/project/autopep8/) ~ A tool that automatically formats Python code to conform to the PEP 8 style guide
- [Codacy](https://app.codacy.com/) ~ Automated Code Review
- [Google Fonts](https://fonts.google.com/) ~ A library free licensed font families, an interactive web directory for browsing the library.

## Features

- User Reg & login: Using 3rd party [Django-Alluth](https://django-allauth.readthedocs.io/en/latest/#) Is used to manage the registration and login process. In order to ensure the security of costume details, every precaution must be taken.

- Postal Charges: Considering that the products vary in size, the postage will have to be adjusted accordingly, considering the products and location.
- Stock Control: The product is unique, so the stock control must be accurate. Upon the payment of an item and the completion of an order, the quantity is deducted from the inventory and the item is placed into inventory.
- Administration area: A web application's Administration area serves as its control centre. Here, you may change the product details, user status, user details, orders, and stock levels. You may only access this if you are authorised.
- The About bio and product general information can be edited in the administration area. Here you can edit the information independently as the products evolve.
- STRIPE payment system: Fully integrated STRIPE API, using all of the internal security features
- Confirmation email: Following the completion of a STRIPE payment. The customer receives a confirmation email and a second email with the details of the order is sent to the store administrator.
- User Dashboard with Order history: When a user registers and logs in, he or she is automatically given a dashboard. Here you will be able to access previous orders, including the STRIPE receipt associated with that order.
  It is possible for users to change their shipping information here.

---

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

| Key                 |      Value      |
| ------------------- | :-------------: |
| SECRET_KEY          | < Your Values > |
| EMAIL_HOST_PASS     | < Your Values > |
| EMAIL_HOST_USER     | < Your Values > |
| NOTIFY_EMAIL        | < Your Values > |
| DEFAULT_FROM_EMAIL  | < Your Values > |
| STRIPE_PUBLIC_KEY   | < Your Values > |
| STRIPE_SECRET_KEY   | < Your Values > |
| STRIPE_SECSTRIPE_WH | < Your Values > |
| CLOUD_NAME          | < Your Values > |
| API_KEY             | < Your Values > |
| API_SECRET          | < Your Values > |

---

## Acknowledgements

[Pure CSS Loaders](https://loading.io/css)

## Deployment

This Project is deployed on [Heroku](https://dashboard.heroku.com/) using [Cloudinary](https://cloudinary.com/) to host the images and [Whitenoise](http://whitenoise.evans.io/en/stable/index.html) to serve the static files.
