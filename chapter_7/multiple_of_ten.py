#asking for a number
number = input("Choose a number.: ")
number = int(number)

#Showing if the answer is multiple of 10 through a if statement
if number % 10 == 0:
	print("The number is divisible by 10")
else:
	print("The number is not divisible by 10")