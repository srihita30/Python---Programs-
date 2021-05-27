# This code is used for taking in data for the members that are a part of the sports team, and printing the same. 

name_team = input('Name of the sports team:')
number = int(input("Enter the number of members on the '{}' team:".format(name_team)))

counter = 0
while counter < number :

	name = input('Enter name:')
	age = input('Enter age:')
	sport = input('Enter the sport she/he will be playing:')
	
	print(f'The name of the participant is {name}.')
	print(f'The age of the participant is {age}.')
	print(f'The sport of the participant is {sport}.')

	counter += 1


	
