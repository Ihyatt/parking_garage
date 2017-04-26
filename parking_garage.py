
class Garage: 
	def __init__(self, rows, moto_spots, comp_spots, large_spots):
		#creation of parking garage
		self.rows = rows
		self.open_moto_spots = self.rows * moto_spots
		self.open_comp_spots = self.rows * comp_spots
		self.open_large_spots = self.rows * large_spots

		self.capacity =(self.open_moto_spots + self.open_comp_spots + self.open_large_spots)
		self.spaces_taken = 0 
		self.garage = {}

		#data structure reperesentation of the garage
		for i in range(self.rows):
			self.garage[i] = [moto_spots, comp_spots, large_spots]


	def park_vehicle(self, vehicle):
		#Public method to be called to park vehicle

		if self.capacity == self.spaces_taken:
			return vehicle + " cannot be parked in this garage."

		if vehicle == "motorcycle":
			return self.__find_moto_spots(vehicle)
		elif vehicle == "car":
			return self.__find_comp_spots(vehicle)
		elif vehicle == "bus":
			return self.__find_large_spots(vehicle)
		else:
			return vehicle + " cannot be parked in this garage."


	def __find_moto_spots(self, vehicle):
		#Private method to park motorcycle only
		if self.open_moto_spots == 0:
			return self.__find_comp_spots(vehicle)

		parked = False
		for i in range(self.rows):
			if self.garage[i][0] > 0:
				self.garage[i][0] -= 1
				self.spaces_taken += 1
				self.open_moto_spots -= 1
				parked = True
				return vehicle + " has been parked."

		if parked == False:
			return self.__find_comp_spots(vehicle)

	def __find_comp_spots(self, vehicle):
		#private method to park either motorcycle or car only
		if self.open_comp_spots == 0:
			return self.__find_large_spots(vehicle)

		parked = False
		for i in range(self.rows):
			if self.garage[i][1] > 0:
				self.garage[i][1] -= 1
				self.spaces_taken += 1
				self.open_comp_spots -= 1
				parked = True
				return vehicle + " has been parked."
				
		if parked == False:
			return self.__find_large_spots(vehicle)

	def __find_large_spots(self, vehicle):
		#Private method to park motorcycle, car or bus
		if self.open_large_spots == 0: 
			return vehicle + " will not fit in this garage."

		parked = False
		for i in range(self.rows):
			if vehicle == "bus":
				if self.garage[i][2] >= 5:
					self.garage[i][2] -= 5
					self.spaces_taken += 5
					self.open_large_spots -= 5
					parked = True
					return vehicle + " has been parked."
			else:
				if self.garage[i][2] > 0:
					self.garage[i][2] -= 1
					self.spaces_taken += 1
					self.open_large_spots -= 1
					parked = True
					return vehicle + " has been parked."

		if parked == False:
			return vehicle + " will not fit in this garage."





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



