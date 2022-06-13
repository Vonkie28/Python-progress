#dictionary for answers from the poll
favourite_languages = {
	'jen' : 'python',
	'sarah' : 'c',
	'edward' : 'ruby',
	'phil' : 'python',
	'robin' : 'php',
	'joris' : 'c',
}

#list of persons who might take the poll
persons = ['joris', 'robin', 'sam', 'job']

#looping to check who has answered the poll
for person in persons:
	if person in favourite_languages:
		print(f'{person.title()}, thank you for answering.')
	else:
		print(f'{person.title()}, can you answer.')