#Creating answer to input for restaurant seating
seat = input("How many people are you eating with?: ")
seat = int(seat)

#If statement for the reaction at the answer
if seat >= 8:
	print("We are making a table ready for you.")
else:
	print("Your table is ready.")