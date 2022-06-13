class Restaurant:
	"""This class represents a restaurant"""

	def __init__(self, name, cuisine):
		"""Initialize attributes to describe restaurant"""
		self.name = name
		self.cuisine = cuisine
		self.customer_served = 0

	def describe_restaurant(self):
		"""Describes the restaurant"""
		print(f"\nThe {self.name} is a small and classy restaurant, the menu is {self.cuisine} style.")

	def open_restaurant(self):
		"""Prints a message that the restaurant is open"""
		print(f"\nThe restaurant: '{self.name}' is now open!")


	def set_customers_served(self, customer):
		"""Sets the number of customers served"""
		self.customer_served = customer	

	def customer_served_number(self):
		"""Prints the number of customer served"""
		print(f"The number of customers served is at the moment {self.customer_served}.")

	def increment_customer_served(self, customer):
		"""Adds the number of customer server"""
		self.customer_served += customer

class IceCreamStand(Restaurant):
	"""This class is representing an ice cream stand"""

	def __init__(self):
		"""Initialising attributes of this class"""
		self.flavours = 'vanilla', 'coockie', 'chocolate', 'strawberry'

	def show_flavours(self):
		print(f"These flavours are available: {self.flavours}")

#Making the first instance for the Restaurant class
first_restaurant = Restaurant('La place', 'Italian')

print(f"The restaurant's name is {first_restaurant.name}.")
print(f"The theme is {first_restaurant.cuisine}.")
first_restaurant.describe_restaurant()
first_restaurant.open_restaurant()

#Making the second instance for the Restaurant class
second_restaurant = Restaurant('Totidas', 'Mexican')
second_restaurant.describe_restaurant()

#Making the third instance for the Restaurant class
third_restaurant = Restaurant('La conja', 'Mediterranean')
third_restaurant.describe_restaurant()

#Creating a fourth instance and testing different attributes and methods
fourth_restaurant = Restaurant('De burg', 'German')
fourth_restaurant.set_customers_served(5)
fourth_restaurant.customer_served_number()
fourth_restaurant.increment_customer_served(10)
fourth_restaurant.customer_served_number()

#Creating a instance of IceCreamStand
first_icecreamstand = IceCreamStand()
first_icecreamstand.show_flavours()