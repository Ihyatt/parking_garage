import unittest
import parking_garage



class TestOnParkingGarage(unittest.TestCase):
    def setUp(self):
        #creates instance of Garage class from parking_garage module test on
        unittest.TestCase.setUp(self)
        self.test = parking_garage.Garage(2, 1, 1, 5)

    def test_park_vehicle(self):
        #general tests for successes and failures
    	assert self.test.park_vehicle("bus") == "bus has been parked."
    	assert self.test.park_vehicle("bus") == "bus has been parked."
    	assert self.test.park_vehicle("bus") != "bus has been parked."
    	assert self.test.park_vehicle("car") == "car has been parked."
    	assert self.test.park_vehicle("car") == "car has been parked."
    	assert self.test.park_vehicle("car") != "car has been parked."
    	assert self.test.park_vehicle("motorcycle") == "motorcycle has been parked."
    	assert self.test.park_vehicle("motorcycle") == "motorcycle has been parked."
    	assert self.test.park_vehicle("motorcycle") != "motorcycle has been parked."


if __name__ == '__main__':
    unittest.main()
