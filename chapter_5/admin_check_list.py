usernames = []

if usernames:
	print('Users are active')
else:
	print('Users are not active')


for usernames in usernames:
	if usernames == 'admin':
		print('Hello admin, would you like to see the status report?')
	else:
		print(f'Hello {usernames}, welcome back.')