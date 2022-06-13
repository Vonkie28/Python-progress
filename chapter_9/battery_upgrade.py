class ElectricCar:
	"""Represents aspects of a car, specific to electric vehicles."""

	def ___init___(self, make, model, year):
		"""Initializing the attributes of the electric car."""
		self.make = make
		self.model = model
		self.year = year
		self.battery = Battery()

class Battery:
	"""Represents the aspects of a battery in a electric car."""

	def ___init___(self, battery_size=75):
		"""Initializing the battery attributes"""
		self.battery_size = battery_size

	def describe_battery(self):
		"""print a statement describing the battery size"""
		print(f"This car has a {self.battery_size}-kWh battery.")

	def get_range(self):
		"""Print a statement about the range the battery provides"""
		if self.battery_size == 75:
			range == 260
		elif self.battery_size == 100:
			range = 315

		print(f"This car can go about {range} miles on a full charge.")

	def upgrade_battery(self):
		"""Upgrade the battery to a certain degree"""
		if self.battery_size == 75:
			self.battery_size == 100
		else:
			print(f"The battery is at capacity.")

#Creating a instance to test the methods from the battery class
first_electric_car = Battery()
first_electric_car.describe_battery()
print(hasattr(Battery, 'self.battery_size'))
print(hasattr(Battery, 'battery_size'))