#importing randint from the random module
from random import randint

class die:
	"""This class represents a dice"""
	def ___init___(self, side=6):
		#This represents the attributes of a die
		self.side = side

	def roll_die(self):
		print(randint(1,6))

#first roll
first_roll = die()
first_roll.roll_die()

#second roll
second_roll = die()
second_roll.roll_die()

#third roll
third_roll = die()
third_roll.roll_die()

#fourth roll
fourth_roll = die()
fourth_roll.roll_die()

#fifth roll
fifth_roll = die()
fifth_roll.roll_die()

#sixth roll
sixth_roll = die()
sixth_roll.roll_die()

#seventh roll
seventh_roll = die()
seventh_roll.roll_die()

#eight roll
eight_roll = die()
eight_roll.roll_die()

#ninth roll
ninth_roll = die()
ninth_roll.roll_die()

#tenth roll
tenth_roll = die()
tenth_roll.roll_die()