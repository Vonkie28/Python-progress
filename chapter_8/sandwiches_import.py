def make_sandwich(*toppings):
	"""Saves and prints the toppings it gets"""
	print(f"\nMaking a sandwich with these topping:")
	for topping in toppings:
		print(f"- {topping}")