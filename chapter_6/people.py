#Making dictionaris of people
person_0 = {
	'first_name' : 'kim',
	'last_name' : 'van duin vonk',
	'age' : '23',
	'city' : 'warmenhuizen',
}

person_1 = {
	'first_name' : 'robbin',
	'last_name' : 'ploeger',
	'age' : '25',
	'city' : 'daalmeer'
}

person_2 = {
	'first_name' : 'coen',
	'last_name' : 'merkus',
	'age' : '23',
	'city' : 'daalmeer'
}

#Dictionaris in a list
persons = [person_0, person_1, person_2]

#Looping through list and printing the list
for person in persons:
	print(person)