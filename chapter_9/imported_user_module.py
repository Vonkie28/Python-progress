#Importing Admin and Privileges classes from the user_module.py file
from user_module import Admin, Privileges
 
#Creating a instance to test out if the importing works
first_admin = Admin()
first_admin.privileges.show_privileges()