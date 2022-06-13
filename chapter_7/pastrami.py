#Making lists of orders and finished sandwiches
sandwich_orders = ['pastrami', 'chicken teriyaki', 'pastrami', 'BBQ', 'caesar salad', 'pastrami']
finished_sandwiches = []

#Creating a while loop to remove pastrami
print("The deli has run out of pastrami")
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

#Creating a while loop to finish sandwiches and move them to a different list
while sandwich_orders:
	current_sandwich = sandwich_orders.pop()

	print(f"I made your {current_sandwich.title()}.")
	finished_sandwiches.append(current_sandwich)

#Display all finished sandwiches
print("\nThe following sandwiches has been made:")
for finished_sandwiches in finished_sandwiches:
	print(finished_sandwiches.title())