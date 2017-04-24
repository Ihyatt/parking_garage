# Parking Garage - Interview Design Challenge

## About
When approaching this project, I made the assumption that motorcycle, compact and large spots are all grouped consecutively allowing me to use a numeric value to keep track of available and taken spots.  

## Contents
* [Technologies Used](#technologiesused)
* [parking_garage.py](#parking_garage.py)
* [general_tests.py](#general_tests.py)
* [time_tests.py](#time_tests.py)
* [Setup](#setup)

### <a name="technologiesused"></a>Technologies Used


* [Python](https://www.python.org/)
* [Classes](https://docs.python.org/3/tutorial/classes.html)


### <a name="parking_garage.py"></a>parking_garage.py
Within parking_garage.py, 


#### <a name="main"></a>Main Movie Page
![fandor_challenge](https://cloud.githubusercontent.com/assets/11432315/24968447/1bdc576e-1f62-11e7-91b7-50c9a3ba63c3.gif)


Movies are organized by the following:
- Popularity
- Year released
- All films

Users can up vote or down vote each film with data retrieved in real time using AJAX and JSON.


#### <a name="search"></a>Movie Search Page
![fandor_challenge2](https://cloud.githubusercontent.com/assets/11432315/24941183/692066ec-1efd-11e7-9a48-21b3e8c9d3fc.gif)

Once typed in the search engine, movies are parsed by each word, and returned in real time using AJAX and JSON. The results are paginated using JQuery. 


#### <a name="run"></a>How to Run Fandor_Challenge Locally

##### General Setup
* Set up and activate a python virtualenv, and install all dependencies:
    * `pip install -r requirements.txt`
 * Make sure you have PostgreSQL running. Create a new database named fandor_challenge:
   * `createdb fandor_challenge`
 * Create the tables in your database:
    * `python -i model.py`
 * Then seed database
   * `python seed.py`
 * Start up the flask server:
    * `python server.py`
 * Go to localhost:5000 to see the web app