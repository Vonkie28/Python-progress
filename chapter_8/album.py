#Defining a function to create a dictionary
def make_album(artist, album):
	"""Putting the function arguments in a dictionary"""
	album = {'artist': artist.title(), 'album': album.title()}
	return album

#Building dictionary with inputs
record = make_album('rammstein', 'zeit')
record_1 = make_album('nirvana', 'nevermind')
record_2 = make_album('rammstein', 'mutter')

#Printing the result
print(record)
print(record_1)
print(record_2)