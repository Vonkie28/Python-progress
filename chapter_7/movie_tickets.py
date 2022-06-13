#Creating a prompt for the user to enter so they know what the prices are
age = "\nEnter your age so i can define the price of the ticket."
age += "\nEnter 'quit' to terminate the program."

#While loop and if statement to determine price for the tickets
message = ""

active = True
while active:
	message = input(age)
	message = int(message)

	if message == 'quit':
		active = False
	elif message < 3:
		print('The ticket is free')
	elif message in range(3, 12):
		print('The ticket is $10')
	elif message >= 12:
		print('The ticket is $15') 
	