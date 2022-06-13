#Importing multiple modules
from admin_privileges_module import Admin, Privileges

#Testing out if importing multiple modules works with an instance
first_admin = Admin()
first_admin.privileges.show_privileges()