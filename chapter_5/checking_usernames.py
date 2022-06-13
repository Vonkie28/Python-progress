current_users = ['max', 'sean', 'justin', 'leonidas', 'dennis']
new_users = ['sainz', 'JUSTIN', 'alonzo', 'max', 'sam']

#Converting current_users list in uppercase
current_users_upper = [x.upper() for x in current_users]
print(current_users)
print(current_users_upper)

#Checking if username has been used.
for new_user in new_users:
	if (new_user in current_users) or (new_user in current_users_upper):
		print('Username not available')
	else:
		print('Username available')

# for new_users in new_users:
# 	if new_users in current_users:
# 		print('Username not available') 
# 	if new_users in current_users_upper:
# 		print('Username not available')	
# 	else:
# 		print('Username available')

