# Parking Garage - Interview Design Challenge

## Contents
* [Technologies Used](#technologiesused)
* [parking_garage.py](#parking_garage.py)
* [general_tests.py](#general_tests.py)
* [time_tests.py](#time_tests.py)
* [Setup](#setup)

### <a name="technologiesused"></a>Technologies Used


* [Python](https://www.python.org/)
* [Classes](https://docs.python.org/3/tutorial/classes.html)
* [unittest](https://docs.python.org/2/library/unittest.html)
* [time](https://docs.python.org/2/library/time.html)


### <a name="parking_garage.py"></a>parking_garage.py
Within parking_garage.py, I have both public and private methods that are used to locate parking spots for either motorcycles, cars or buses. When approaching this project, I made the assumption that motorcycle, compact and large spots are all grouped consecutively allowing me to use a numeric value to keep track of available and taken spots. The time complexity for parking a vehicle is linear (O(rows)).

To Run: 
Create an instance of of the Garage, ex. lot = Garage(2, 2, 2 , 5). Then add vehicles to the garage. As a courtesy, there is test data available within parking_garage.py. 

	print lot.park_vehicle("horse")
	print lot.park_vehicle("motorcycle")
	print lot.park_vehicle("car")
	print lot.park_vehicle("bus")
	print lot.park_vehicle("car")
	print lot.park_vehicle("car")
	print lot.park_vehicle("motorcycle")
	print lot.park_vehicle("car")
	print lot.park_vehicle("bus")
	print lot.park_vehicle("motorcycle")
	print lot.park_vehicle("car")

To run, while in the challenge directory and type and enter 'python parking_garage.py'

Output to terminal: 

	horse cannot be parked in this garage.
	motorcycle has been parked.
	car has been parked.
	bus has been parked.
	car has been parked.
	car has been parked.
	motorcycle has been parked.
	car has been parked.
	bus has been parked.
	motorcycle has been parked.
	car will not fit in this garage.


#### <a name="general_tests.py"></a>general_tests.py
Using unittest, I imported the parking_garage module and tested for the success and failures of my code looking specifically at the only public method, park_vehicle(). Within setUp(), you will notice self.test = parking_garage.Garage(2, 1, 1, 5). This is simply an instance of the Garage class that we are going to test on. 

To Run:
cd to the challange directory and type and enter 'python general_tests.py'

Output to terminal: 

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK


#### <a name="time_tests.py"></a>time_tests.py
Using time, I once again imported the parking_garage module and checked for the time it took in terms of seconds for parking_garage() to run in terms of seconds. Within check_time_park_vehicle(), you will notice garage = parking_garage.Garage(2, 1, 1, 5). Once again, this is an instance of the Garage class that we are going to test on. 

To Run: 

cd to the challange directory and type and enter 'python time_tests.py'

Ouput to terminal: 

--- 4.05311584473e-06 seconds ---


#### <a name="setup"></a>Setup

##### General Setup
* Download or git clone to desktop, then cd into directory. 
