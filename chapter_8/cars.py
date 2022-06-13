def make_car(manufacturer, model, **car):
	"""For use to display information about a car"""
	car['manufacturer'] = manufacturer
	car['model'] = model
	return car 

car = make_car('opel', 'meriva',
	color= 'grey',
	tow_package= True,)

print(car) 