def build_profile(first, last, **user_info):
	"""Build a dictionary containing everything about a user"""
	user_info['first_name'] = first
	user_info['last_name'] = last
	return user_info

user_profile = build_profile('sam', 'vonk',
	location= 'alkmaar',
	job= 'military',
	age= '23')

print(user_profile)