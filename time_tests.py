import parking_garage
import time    

class TestTimeOnParkingGarage:

    def check_time_park_vehicle(self):
    	#creates instance of Garage class from parking_garage module test on
    	garage = parking_garage.Garage(2, 1, 1, 5)
    	start_time = time.time()
    	garage.park_vehicle("bus")
   		#Returns time taken to run a single vehicle insertion
    	return ("--- %s seconds ---" % (time.time() - start_time))







if __name__ == '__main__':
	time_test = TestTimeOnParkingGarage()
	print time_test.check_time_park_vehicle()