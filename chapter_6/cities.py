#Creating a dictionary in a dictionary
cities = {
	'amsterdam' : {
		'country' : 'Netherlands',
		'population' : '905.234',
		'fact' : 'it has the most nationalities in a city of the world',
	},

	'rotterdam' : {
		'country' : 'Netherlands',
		'population' : '588.490',
		'fact' : 'it has the biggest port in the world',
	},

	'alkmaar' : { 
		'country' : 'Netherlands',
		'population' : '91.035',
		'fact' : 'the city organises a weekly cheese market for six months',
	},
}

print(cities.items())