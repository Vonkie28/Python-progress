#Making a dictionary of people their favourite places
favourite_places = {
	'kim' : 'thuis',
	'robbin' : 'bergen',
	'sam' : 'noorwegen',
}

#Looping the dictionary and printing the dictionary
for name, place in favourite_places.items():
	print(f"{name.title()}'s favourite place is {place.title()}")