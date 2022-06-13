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