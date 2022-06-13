#First conditional test
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

#Second conditional test
dj = 'DRS'
print("\nIs dj == 'korsakof'? I predict False.")
print(dj == 'korsakof')

#Third conditional test
phone = 'android'
print("\nIs phone == 'android'? I predict True.")
print(phone == 'android')

#Fourth conditional test
weather = 'cloudy'
print("\nIs weather == 'sunny'? I predict False.")
print(weather == 'sunny')

#Fifth conditional test
life = 'good'
print("\nis life == 'good'? I predict True.")
print(life == 'good')

#Sixth conditional test
excited = 'Elden Ring'
print("\nAm i excited for 'Elden Ring'? I predict True.")
print(excited == 'Elden Ring')

#Seventh conditional test
smoking = 'bad'
print("\nIs smoking 'bad' for me? I predict True.")
print(smoking == 'bad')

#Eight conditional test
love = 'real'
print("\nIs love 'fake'? I predict False.")
print(love == 'fake')

#Ninth conditional test
amerika = 'boring'
print("\nIs amerika 'fun'? I predict False.")
print(amerika == 'fun')

#Tenth conditional test
rammstein = 'good'
print("\nIs rammstein 'bad'? I predict False")
print(rammstein == 'bad')

#Conditional test 'inequality' True
requested_booze = 'wine'
if requested_booze != 'beer':
	print('\nBring the beer!')

#Conditional test 'inequality' False
requested_booze = 'beer'
if requested_booze != 'beer':
	print('\nBring the beer!')

#Numerical condition equality True
number = 30
print(number == 30)

#Numerical condition equality False
number = 25
print(number == 30)

#Numerical condition inequality True
number = 40
print(number != 28)

#Numerical condition inequality False
number = 28
print(number != 28)

#Numerical condition greater than True
number = 10
print(number >= 5)

#Numerical condition greater than False
number = 20
print(number >= 40)

#Condition test keyword or True
number_1 = 13
number_2 = 17
print(number_1 >= 15 or number_2 <= 20)

#Condition test keyword and false
age_1 = 19
age_2 = 21
print(age_1 >= 18 and age_2 <= 15)

#Condition test item in list True
used_cars = ['subaru', 'bmw']
car = 'bmw'

if car in used_cars:
	print('\nCar is available!')

#Condition test item in list False
used_cars = ['subaru', 'bmw']
car = 'opel'

if car in used_cars:
	print('\nCar is not available')

#Condition test item not in list True
phones = ['motorola', 'apple']
phone = 'android'

if phone not in phones:
	print('\nPhone is not available!')

#Condition test item not in list False
phones = ['motorola', 'apple']
phone = 'apple'

if phone not in phones:
	print('\nPhone is available')