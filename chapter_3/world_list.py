#List beginning
city = [ 'lissabon', 'praag', 'amsterdam', 'houston', 'groningen']

#Temporary sorting list and printing back normal
print(city)
print(sorted(city))
print(city)

#Temporary sorting list in reverse and printing back normal
print(sorted(city,reverse=True))
print(city)

#Reversing the list and back
city.reverse()
print(city)
city.reverse()
print(city)

#Permanently storing the list in alphabetical and reverse
print(city.sort())
print(city)
city.sort(reverse=True)
print(city)

