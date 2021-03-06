# GM-Personal-Training

GM-Personal-Training is a site made for the code institute Full Stack Developers milestone project. the purpose of this site is to provide an online platform where signed up users can buy products to help with their fitness and also book personal training sessions through a contact form. 

## UX

Pages on this site include a products page, cart, checkout, class booking, login and registration page. All pages are easily accessible through the well laid out and clean nav bar however some pages require you to be logged in for access for example the classes page.

The home page for this site is the products page were everything GM-Personal-Training wants to sell will be displayed professionally and with details on each product including name, price, image and description of that product. The buyer then selects the quantity of that product they would like to buy and adds it to their cart. If the buyer is struggling to find what they are looking for then they can use the filter application to either search for a specific product or narrow down their choices using the categories filter.

Once the item is added to the cart, the cart page will then display that same item along with the quantity the buyer has chosen and the total price of all items added together. here they have a chance to amend their quantity if they need or can move on to the checkout page.

In the checkout page there is a payment form and an order form which allows the user to pay online and have the product delivered to them. All the products are once again displayed for the buyer to see however by this point, they cannot amend the quantity unless they go back a page.

If the user is looking to book a personal training session with GM-Personal-Training they can do this in the classes page. A user must be logged in to access this page but once logged in it then allows them access to contact GM-Personal-Training to book a session.

## Features 

this site has login, logout and registration features that allow the user access to different areas of the site and its features. The user also has the ability to change their password if they have previously forgotten it by using email.

This site allows people to find products easily using the search feature on the products page. A personal trainer could recommend a specific product and this feature makes it easy for the user to find said product.

The categories filter helps those users just looking to browse narrow down the product range to what they came to see. They can narrow down the products to just for men/women or equipment which means the site can display a wide variety of products but make it still easy for a user to find what they are looking for.

The site allows users to select a quantity of products which is good for the business and user as it's easy to work with and creates potential for GM-Personal-Training to sell higher amounts.

The checkout page is linked with Stripe which allows user to pay safely for their product and knowing all their payment details will be handled with securely and privately.

The classes page contact form is clearly laid out using Django forms for a professional look. When completed the information is put through emailjs to then send an email to GM-Personal-Training that is well formatted and easy to read displaying who sent it and what their request was.

Also, on the classes there is a map displaying clearly where GM-Personal-Training is based using the google my maps API feature.

## Future Features

In the future I wish to have more ways to filter down the products for example by price or by colour. 

I also aim to add a calendar that displays available time slots for a user to book a session straight away and then also pay straight away rather than contact through email services.

I would like for users to be able to add multiple different products to the cart at the same time rather than adding each separately.

## Technologies Used

Django https://www.djangoproject.com/ has been the main framework behind this project in helping to create applications, run them and display them on this site.

Google Chrome developer tools https://www.google.com/chrome/ I used these to test my site on different device sizes and to receive information from JavaScript in the console.

Bootstrap 3.3.7 https://getbootstrap.com/docs/3.3/ Bootstrap was used throughout this site for its grid system and different layout features. It has allowed me to change sizes and add form features to my site which has helped give it a more professional look and easier for the user to understand.

Google MyMaps https://www.google.co.uk/maps/d/u/0/ has allowed me to easily display a map and directly pin pointing the location of GM-Personal-Training for users to see.

JQuery https://jquery.com/ JQuery has made it easier to target specific aspects of the site in JavaScript by simplifying the DOM.

W3C validator https://validator.w3.org/ The W3C validator allowed to check my code is clean and had no faults.

Flask https://www.fullstackpython.com/flask.html Flask is a framework that has help make the code easier to write and display.

GitHub https://github.com/grantymartin/gm-personal-training has been used throughout to continuously track and record all changes made to the website. 

Heroku https://www.heroku.com Heroku allows me to create a link with the site running with a working application.

Stripe https://stripe.com/gb Was used to make all payment methods on this site secure and reliable.

Postgres https://www.postgresql.org/ is the database we have used to store our data in from this site.

## Testing

Testing for this site began with running the HTML and CSS through the W3C validator to confirm the code was clean and without error. If any errors showed up, they were changed to show the correct HTML/CSS. 

Next up I wrote python tests for the forms created in Django, in the classes/checkout and account apps. These tests checked the defaults of the form’s answers, checked to make sure the forms were fully filled out and to check they were completed with appropriate answers. 

In the classes form I checked to make sure that the form had to be fully completed before being able to be sent away and to double check that if the form wasn't completed the appropriate message appeared for the user.

In the checkout form I checked to make sure the form had to be fully completed and the appropriate message appeared for the user if it wasn't. I also completed the payment form manually on the checkout app with the Stripe test fill out form and it worked perfectly.

In the account app there are a couple different forms so I had to check different things for each form. For the login form in accounts I simply checked to make sure that the form was fully filled out and the appropriate message appeared for the user again however for the registration form I checked more. I wrote code to test the email. If the email wasn't in the appropriate format, it wouldn't be accepted. I also tested the form so that it wouldn't accept it completed if both password1 and password2 didn't match perfectly. 

I then went on to test the models in the checkout and products apps. in the Checkout form I wanted to make sure that the postcode could be left blank however every other field had to be completed and filled in. I also checked that the date would be submitted in the correct format that I want it in.

In the products app I checked the name, description, price and category were all being recorded properly and the defaults were correct.

After testing my site with the W3C validator and the python testing code I tested it with 5 other people. I allowed each person to look through the site on different devices of different screen sizes and different browsers. I then asked for feedback on design, ease of use, general functionality and potential updates/improvements.

Feedback on design was positive with the site being presented in a professional style, neat and clean. It looked good on all screen sizes from large desktop screens to small mobile devices. 

Feedback on ease of use was again positive. In general, everyone found what I asked them to find easy enough but some made a point that the classes should be more advertised for user who are not logged in to promote the site. I took this feedback into consideration and changed the home products page to promote the classes of GM-Personal-Training as well. 

Feedback on general functionality was also positive. The login/ registration forms worked well, the classes contact form worked as supposed to and the adding to cart and removing from cart also worked. However, it was pointed out to me that if something was added to the cart without putting a value in the quantity box, the site would produce an error. As for general improvements it was suggested to me that it would be good if I could add multiple different items to my cart in one go rather than adding each separately. I have added this idea to my future features section.

Finally, I asked them to do their best to break the site. When I did this, it was pointed out to me that the functionality of my reset email feature wasn't working properly and this is due to the fact my own email wasn't set up to allow less secure apps to connect to it.

It was also pointed out that when adding a product to the cart and the quantity was on zero then the page returned an error page. So, to fix that I set a min, max and a starting value so that zero would never be an option to cause a problem.

## Deployment

This site has been developed on AWS cloud 9 and continuously pushed to Github pages throughout the process. This site was then connected to Heroku through Github to run the app live. A postgres database was created on Heroku and linked with the page. The config variables were set with the IP equal to 0.0.0.0 and the PORT set to 5000. 

### During deployment it was noticed that Django version used in this project was coming to an end in the supported community but as long as the correct python version was used it should continue to work as supposed to

All the static files including CSS, Images and JS are held using the AWS S3 bucket.  



### Content

All written content in this site was done by myself. The content of this site was written for the purpose of the Code institute Full Stack developers milestone project and the information provided may be false.

### Media

All photos used on this site came under the labelled for reuse section of google images and links to each are provided below.

https://www.needpix.com/photo/635124/weight-sport-crossfit-training-workout-fitness-fit-gym-weight-training

https://www.flickr.com/photos/floris-oosterveld/35562172343

https://www.getsweatgo.com/workout/guides/guide-to-getting-a-personal-fitness-trainer-153

https://man-man.nl/fitness-routine/

https://nkpersonaltraining.nl/project/female-shape-programma/

https://vitalgym.nl/diensten/personal-training-diensten/personal-training-duo/pt-duo-vital-gym-arnhem-aanbod/

http://j-your-fitness.torbara.com/home/home-2.html

### Acknowledgements

I received inspiration for the project from code institute mentor Aaron Sinnott during our first call to discuss the project.
