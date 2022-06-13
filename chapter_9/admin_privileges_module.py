#Importing the User class
from separate_user_module import User

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