#Creating a dictionary of responses
responses = {}

#Setting a flag to indicate polling is active
polling_active = True

while polling_active:
	name = input("\nWhat is your name?: ")
	response = input("If you could visit a place in the world, where would you go?: ")

	responses[name] = response

	repeat = input("Would anyone else want to take the poll? (yes/ no): ")
	if repeat == 'no':
		polling_active = False

#Printing dictionary
print(responses)

#Polling is complete. Show the results
print("\n--- Poll Results ---")
for name, response in responses.items():
	print(f"{name} would like to visit {response}.") 