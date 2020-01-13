# Bali Silver

After spending our honeymoon in Bali and seeing all the fantastic crafts Bali has to offer. My wife and I thought about importing
and selling some of the more unique items. Particularly the world renowned silver jewellery which we watched being hand crafted in Bali. 

## UX
![Bali Silver](#)

Open on the product page the user is invited register from a tab in the navigation bar. After a seemless registration, 
all options appear at the top of the screen. Allowing the user to read blogs of fellow users and create their own. 
They can contact the admin via the 'contact us' page, or read more about the company selling the products by clicking the 'About us" tab. 

Naturally, they can search and buy products too.

[Click here](library/BaliSilver.pdf) to see the mock ups.

## Users
Anyone who is on the hunt for uniques Balinese sounveniers. 

### User Stories

## Features
Account setup - once the initial account is setup the user can then edit their details through the profile page.
Admin - the super user can add go into the admi page to add/edit products and accounts
Cart - only when th euser has registered and logged in can they add items to their cart.
Payment system - Using stripe the user is invited to add card details for payment. They will recieve an email as confirmation.
Blog - Users can also add their experience in Bali, jewelery from bali or using this site to the blog page.

## Technology Used
* [HTML](https://www.w3schools.com/html/) - for the structure of the content of the page
* [CSS3](https://www.w3schools.com/css/) - for making small adjustments to the materialize framework
* [Javascript](https://www.javascript.com/) - to initialise some components on the Materialize framework
* [Balsamiq](https://www.balsamiq.com/wireframes/) - for the wireframe
* [Git](https://www.git-scm.com/) - for version control
* [GitHub](https://www.github.com/) - to host the repository
* [GitHup Pages](https://www.pages.github.com/) - Website hosting.
* [Heroku](https://www.heroku.com) - to deploy the app
* [Flask-Pymongo](https://www.flask-pymongo.readthedocs.io/en/latest/) - for interaction with the front end
* [Python](https://www.python.org/) - for back end implementation
* [Bootstrap](https://www.getbootstrap.com/)
* [Django](https://www.djangoproject.com/) - framework used to build the e commerce site
* [stripe](https://www.stripe.com/gb/) - used for the payment system
* [Travis](https://www.travis-ci.org/) - for testing

## Testing

### Manual Tests


### Automated Tests
* Chrome Developer Tools - to ensure all screen sizes responded correctly
* W3C HTML & CSS Validation - used to test HTML and CSS

## Deployment
The app was developed using AWS Cloud9. The git repository was initiated through 
the bash terminal and regular commits were made after each piece of development. 
The project was then deployed to Heroku through the following steps.

* Created new app titled "postal-hazards-uk"
* The repository was cloned by using: heroku git:clone -a postal-hazards-uk
* A requirments file and procfile was added
* The Git repository was added using: git push heroku master

To deploy your own version:
* Visit the repository [here](https://github.com/bandyp/djandy_ecommerce)
* Click 'clone' to copy
* Open your IDE
* Type 'git clone https://github.com/bandyp/djandy_ecommerce.git' in the terminal window of the root directory

Take a walk through the Bali Silver app [here](https://djandy_ecommerce.herokuapp.com/)

## Credits
Code institue mentor Suen Owonikoko

[![Build Status](https://travis-ci.org/bandyp/djandy-ecommerce.svg?branch=master)](https://travis-ci.org/bandyp/djandy-ecommerce)