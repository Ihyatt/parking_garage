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


#### <a name="general_tests.py"></a>general_tests.py
Using unittest, I imported the parking_garage module and tested for the success and failures of my code looking specifically at the only public method, park_vehicle(). 


#### <a name="time_tests.py"></a>time_tests.py
Using time, I once again imported the parking_garage module and checked for the time it took in terms of seconds for parking_garage() to run in terms of seconds.


#### <a name="setup"></a>Setup

##### General Setup
* Download or git clone to desktop, then cd into directory. 
