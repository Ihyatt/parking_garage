import parking_garage
import time    

class TestTimeOnParkingGarage:

    def check_time_park_vehicle(self):
    	garage = parking_garage.Garage(2, 1, 1, 5)
    	start_time = time.time()
    	garage.park_vehicle("bus")
    	print ("--- %s seconds ---" % (time.time() - start_time))







if __name__ == '__main__':
	time_test = TestTimeOnParkingGarage()
	print time_test.check_time_park_vehicle()