# SI507 - Final Project by Roy Wang

----------
## Overall

My project will present a database of Marvel superhero characters and the movies. There will be a route for looking for the superheroes' information and description, and another route will be the presentation of past and upcoming Marvel movies. The user can click into their favorite character to check his/her superpower, history, background story and also be able to see what movies he/she were in or they can also click into their favorite movie to see what characters were in there.

I want to focus on sourcing data from a website or API based on user input and processing it.


## Interface description
- Route 1: /index   →   
  Homepage that shows the upcoming Marvel movies.
  
- Route 2: /superhero/<name>  →   
  The introduction of superheroes.
  
- Route 3: /movie/<name>  →   
  The introduction of movies.



## Specifics

I will be relying on data from scraping [a specific website or multiple websites/multiple pages from the same website], making requests to [a specific API / multiple APIs], user input to a form or in a URL, or a downloaded dataset that I found [at this link]. You should describe exactly what data you plan to use and where and how you will get it. It may be any of those options, or multiple of them.

An example of my data OR link to documentation of the API I’ll use OR the website I will be scraping is here: (here goes any link/s pointing to the data sources, and/or a short description of the data source if it is user input)

I expect my database schema to include number tables. The entities each table will represent are: list entities, e.g. Movies, Directors, etc. 

There will be a many to many or many to one relationship between relevant tables. 

Any additional details about my database structure plans.

I will be populating the database by saving data to the database when users enter it into a form on a page on my app, OR writing a script to load it in to a .sqlite database file which my Flask app will rely on and have models to describe, OR saving data to a database when it’s accessed via scraping or an API.

I am planning to use the following modules in writing my code, aside from Flask and SQLAlchemy or some equivalent: list of modules I plan to use, with the module’s name and specifically what I want to do with it


> Example: 
> - plotly - for charting/graphing data
> - matplotlib - also for charting, maybe better for me
> - Folium - for maps… not sure how to use this one
> - requests_cache - for caching data I scrape

I will be defining the following functions outside of Flask routes: brief description of one or two functions that will be defined and what they’ll each do/take as input(s)/return

I will be defining the following classes outside of Flask routes/models: brief description of an object or objects — what it will inherit from if anything, what input the constructor will require, what one instance will represent, what it will help you to do, where you will create instances of it — see https://learningpython-today.github.io/pip2/Classes/ThinkingAboutClasses.html and our OOP work from earlier in the semester

The assignment(s) in 507 we’ve done that are most like what I want to do are:  whichever assignment(s)

Other useful resources for this project for me will be: links or references to specific things I think will be helpful to reference, including specific lecture notes, lab examples, code examples from class, readings, or anything on the internet you’ve found useful


## Other

My biggest concerns about my work on this project are short description of my concerns

I feel confident that I can complete these parts of the project I am planning (a brief description)

Also, anything else you want instructors to know SPECIFICALLY ABOUT YOUR PROJECT — this is not a good space for major personal concerns, because we’ll be reviewing these very rapidly
