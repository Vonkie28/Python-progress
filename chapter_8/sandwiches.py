def make_sandwich(*toppings):
	"""Saves and prints the toppings it gets"""
	print(f"Making a sandwich with these topping:")
	for topping in toppings:
		print(f"- {topping}")

make_sandwich('cucumber')
make_sandwich('tomato', 'chicken')
make_sandwich('beef', 'onion', 'lettuce')