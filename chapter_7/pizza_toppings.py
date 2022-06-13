#creating a prompt for pizza toppings.
toppings = "\nWhat kind of toppings on your pizza would you like?"
toppings += "\nEnter quit to end the program."

#While loop for toppings
message = ""

active = True
while active:
	message = input(toppings)

	if message == 'quit':
		active = False
	else:
		print(f"\nI will add {message} to your pizza!")