#creating a prompt for pizza toppings.
toppings = "\nWhat kind of toppings on your pizza would you like?"
toppings += "\nEnter quit to end the program."

#While loop for toppings
message = ""
while message != 'quit':
	message = input(toppings)
	print(message)