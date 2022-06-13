class User:
	"""This represents an user."""

	def __init__(self, first_name, last_name, age, gender, residence):
		"""initializing the attributes"""
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.gender = gender
		self.residence = residence
		self.login_attempt = 0

	def describe_user(self):
		"""Method to describe the user"""
		print(f"first_name = {self.first_name}")
		print(f"last_name = {self.last_name}")
		print(f"age = {self.age}")
		print(f"gender = {self.gender}")
		print(f"residence = {self.residence}")

	def greet_user(self):
		"""Method to greet the user"""
		print(f"\nWelcome back {self.first_name} {self.last_name}!")

	def increment_login_attempt(self):	
		"""Increases the login attempts by one"""
		self.login_attempt += 1

	def show_login_attempt(self):
		"""Shows the amount of attempts"""
		print(f"\nThe amount of attempts = {self.login_attempt}.")

	def reset_login_attempt(self):
		"""Resets the login attempt to zero"""
		self.login_attempt = 0

class Admin(User):
	"""This represents an admin"""

	def __init__(self):
		#self.privileges = ["can add post", "can delete post", "can ban user", "can unban user"]
		self.privileges = Privileges()
	
	#def show_privileges(self):
		"""Shows the privileges the admin has"""
		#print(f"The admin has these privileges:")
		#print(f"{self.privileges[0]}")
		#print(f"{self.privileges[1]}")
		#print(f"{self.privileges[2]}")
		#print(f"{self.privileges[3]}")

class Privileges():
	"""This class is for privileges which are available"""

	def __init__(self):
		self.privileges = ["can add post", "can delete post", "can ban user", "can unban user"]

	def show_privileges(self):
		"""Shows the privileges the admin has"""
		print(f"The admin has these privileges:")
		print(f"{self.privileges[0]}")
		print(f"{self.privileges[1]}")
		print(f"{self.privileges[2]}")
		print(f"{self.privileges[3]}")

#Creating the first instance for the User class
first_user = User('Sam', 'Vonk', '23', 'Male', 'Warmenhuizen')
first_user.describe_user()
first_user.greet_user()

#Creating the second instance for the User class
second_user = User('Kim', 'van Duin-Vonk', '23', 'Female', 'Warmenhuizen')
second_user.describe_user()
second_user.greet_user()

#Creating the third instance for the User class
third_user = User('Mike', 'Bethlem', '23', 'Male', 'Langedijk')
third_user.describe_user()
third_user.greet_user()
third_user.show_login_attempt()
third_user.increment_login_attempt()
third_user.increment_login_attempt()
third_user.show_login_attempt()
third_user.reset_login_attempt()
third_user.show_login_attempt()

#Creating a instance from the admin class to use a method from the Privileges class
first_admin = Admin()
first_admin.privileges.show_privileges()