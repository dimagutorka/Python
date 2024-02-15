import random


class Car:

	def __init__(self, model, collar):
		self.model = model
		self.fuel = random.randrange(0, 9)
		self.collar = collar
		self.trip_distance = 0

	def move(self, distance):
		self.trip_distance += distance
		self.fuel -= distance
		return self.fuel - self.trip_distance


Garage = [Car("Audi", "White"), Car("BMW", "Black"), Car("Hyundai", "Gray")]
# put all the instances in a list to have an opportunity to work with them in "for" cycle

desired_distance = 4
winner = True

while winner: 	# the cycle works until one of the car drives desired distance
	for i in Garage:
		i.move(random.randrange(0, 9))
		if i.trip_distance >= desired_distance: # here we check weather any of our car drove desired distance
			print(f"{i.model} is winner in a race having driven {i.trip_distance}")
			winner = False # change our var to get out of the cycle
			break


print(f"{Garage[0].model} has drove {Garage[0].trip_distance} and had {Garage[0].fuel} fuel left,\n"
      f"{Garage[1].model} has drove {Garage[1].trip_distance} and  had {Garage[1].fuel} fuel left,\n"
      f"{Garage[2].model} has drove {Garage[2].trip_distance} and had {Garage[2].fuel} fuel left")
