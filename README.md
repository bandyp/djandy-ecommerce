# Bali Silver

[![Build Status](https://travis-ci.org/bandyp/djandy-ecommerce.svg?branch=master)](https://travis-ci.org/bandyp/djandy-ecommerce)

After spending our honeymoon in Bali and seeing all the fantastic crafts Bali has to offer. My wife and I thought about importing
and selling some of the more unique items. Particularly the world renowned silver jewellery which we watched being hand crafted in Bali. 
Presently, this is a fictional ecommerce site, where users can register/log in. They can go through the process to buy jewellery; or read and post about the 
beautiful Indonesian island. 

## UX
[Bali Silver](https://bandy-ecommerce.herokuapp.com/)

Open on the home page, which gives a small taste of what the website offers, the user is invited register from a tab in the navigation bar. 
The unregistered user can only view the products and the about us page. 
After a seemless registration, all options appear at the top of the screen. Allowing the user to read blogs of fellow users and create their own. 
They can contact the admin via the 'contact us' page, or read more about the company selling the products by clicking the 'About us" tab. 

Naturally, they can search and buy products too.

[Click here](UXdesign/BaliSilverWireframes.pdf) to see the mock ups.

## Users
Anyone who is on the hunt for unique Balinese jewellery, especially those who have visited the tropical island before or perhaps want to in the future.

### User Stories
A couple who may have visited Bali but didn't end up buying some silver jewellery can do so here knowing thats its authentic products.

A business which already sells unique and rare hand crafted jewellery can top up their own selection by going through the Bali Silver website.

A buyer for a large department store may not even know of the unique offerings which come from Bali, 
by visiting the Bali Silver website they can test their own market by purchasing throug here. 


## Features
Account setup - once the initial account is setup the user can then edit their details through the profile page.
Admin - the super user can go into the admin page to add/edit products and accounts. They are also able to edit any users blog posts, both from the admin panel or the website. 
Cart - only when the user has registered and logged in can they add items to their cart.
Payment system - Using stripe the user is invited to add card details for payment. They will recieve an email as confirmation.
Blog - Users can also add their experience in Bali, jewellery from Bali by using this site to the blog page. Editing posts can only be done by the authot or the superuser.

## Technology Used
* [HTML](https://www.w3schools.com/html/) - for the structure of the content of the page
* [CSS3](https://www.w3schools.com/css/) - for making small adjustments to the materialize framework
* [Javascript](https://www.javascript.com/) - to initialise some components on the Bootstrap framework
* [Balsamiq](https://www.balsamiq.com/wireframes/) - for the wireframe
* [Git](https://www.git-scm.com/) - for version control
* [GitHub](https://www.github.com/) - to host the repository
* [Heroku](https://www.heroku.com) - to deploy the app
* [Python](https://www.python.org/) - for back end implementation
* [Bootstrap](https://www.getbootstrap.com/)
* [Django](https://www.djangoproject.com/) - framework used to build the e commerce site
* [stripe](https://www.stripe.com/gb/) - used for the payment system

## Testing

### Automated Tests
Automated testing was done using Travis-CI. There is automated testing done for apps with views, models, and forms (where applicable). 


### Manual Tests
* Chrome Developer Tools - to ensure all screen sizes responded correctly
* W3C HTML & CSS Validation - used to test HTML and CSS

A lot of manual testing was done for registration, blog details, cart, payments system and logging out. 

## Deployment
The app was developed using AWS Cloud9. The git repository was initiated through 
the bash terminal and regular commits were made after each piece of development. 
The project was then deployed to Heroku through the following steps.

* Created new app titled "bandy-ecommerce"
* The repository was cloned by using: heroku git:clone -a bandy-ecommerce
* A requirments file and procfile was added
* The Git repository was added using: git push heroku master

To deploy your own version:
* Visit the repository [here](https://github.com/bandyp/djandy_ecommerce)
* Click 'clone' to copy
* Open your IDE
* Type 'git clone https://github.com/bandyp/djandy_ecommerce.git' in the terminal window of the root directory

As this is a fictional site, no actual card payments are processed. 
Also, any emails sent to the user are sent to teh console instead. The links are available in the console.


Take a walk through the Bali Silver app [here](https://bandy-ecommerce.herokuapp.com/)

## Credits

### Content
All descriptions of products were written by myself. The blog posts and pictures were cut from [bali.com](https://www.bali.com) and wikipedia. Jewellery images were taken from the TJC website.

### Acknowledgments
Code institue mentor Suen Owonikoko and numerous tutors. Code for the authentication, registration process and payment system is based on the CI tutorials 
