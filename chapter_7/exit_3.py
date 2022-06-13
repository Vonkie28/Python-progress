#creating a prompt for pizza toppings.
toppings = "\nWhat kind of toppings on your pizza would you like?: "
toppings += "\nEnter quit to end the program."

#While loop for toppings
while True:
	message = input(toppings)

	if message == 'quit':
		break
	else:
		print(f"I will put {message} on your pizza.")