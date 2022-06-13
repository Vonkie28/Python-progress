major_rivers = {
	'danube' : 'austria',
	'dnieper' : 'ukraine',
	'loire' : 'france',
}

for key, value in major_rivers.items():
	print(f"The {key.title()} runs through {value.title()}.")