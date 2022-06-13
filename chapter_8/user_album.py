#Defining a function to create a dictionary
def make_album(artist, album):
	"""Putting the function arguments in a dictionary"""
	album = {'artist': artist.title(), 'album': album.title()}
	return album
	print(album)

#Using a while loop to put user inputs in a dictionary
while True:
	print("Tell me your favorite artist and your favorite album.")
	print("Type 'q' to quit.")
	
	artist = input('artist: ')
	if artist == 'q':
		break

	album = input('album: ')
	if album == 'q':
		break

