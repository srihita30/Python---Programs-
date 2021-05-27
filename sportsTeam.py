# This code is used for taking in data for the members that are a part of the sports team, and printing the same. 

name_team = input('Name of the sports team:')
number = int(input("Enter the number of members on the '{}' team:".format(name_team)))

counter = 0
while counter < number :

	Name = input('Enter name:')
	Age = input('Enter age:')
	Sport = input('Enter the sport she/he will be playing:')
	
	print(f'The name of the participant is {Name}.')
	print(f'The age of the participant is {Age}.')
	print(f'The sport of the participant is {Sport}.')

	counter += 1


	