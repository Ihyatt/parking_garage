

class Garage: 
	def __init__(self, levels, moto_spots, comp_spots, large_spots):
		#creation of parking garage
		self.levels = levels
		self.open_moto_spots = self.levels * moto_spots
		self.open_comp_spots = self.levels * comp_spots
		self.open_large_spots = self.levels * large_spots

		self.capacity =(self.open_moto_spots + self.open_comp_spots + self.open_large_spots)
		self.garage = {}

		#data structure reperesentation of the garage
		for i in range(self.levels):
			self.garage[i] = [moto_spots, comp_spots, large_spots]


	def park_vehicle(self, vehicle):
		#Public method to be called to park vehicle

		if self.capacity == 0:
			return vehicle + " cannot be parked in this garage."

		if vehicle == "motorcycle":
			return self.__find_spots(vehicle, 0)
		elif vehicle == "car":
			return self.__find_spots(vehicle, 1)
		elif vehicle == "bus":
			return self.__find_spots(vehicle, 2)
		else:
			return vehicle + " cannot be parked in this garage."


	def __find_spots(self, vehicle, row):
		#Private method to park motorcycle, car or bus
		if row > 2:
			return vehicle + " will not fit in this garage."
			
		parked = False
		for i in range(self.levels):
			if vehicle == "bus":
				if self.garage[i][row] >= 5:
					self.garage[i][row] -= 5
					self.capacity -= 5
					parked = True
					return vehicle + " has been parked."
			else:
				if self.garage[i][row] > 0:
					self.garage[i][row] -= 1
					self.capacity -= 1
					parked = True
					return vehicle + " has been parked."

		if parked == False:
			return self.__find_spots(vehicle, row + 1)





if __name__ == '__main__':
	#Sample instanct of Garage
	lot = Garage(2, 2, 2 , 5)
	#Series of sample data to populate garage
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


