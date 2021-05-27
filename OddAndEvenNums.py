# This code will print the odd and even numbers separately from a list that the user has entered.   

list_size = int(input("How many numbers do you want to enter: ")) # This input will be used for defining the number of iterations for the while loop. 


my_list = [] # An empty list to which user input will be appended. 
x = 0 # A counter for the while loop. 

# The while loop below will take in input from the user, and append the values to a list. The number of the iterations are based on the size of the list defined above.
while x < list_size:

	num = int(input('Enter a number into the list: '))
	my_list.append(num)
	x = x + 1

statement = "The list is:{}"

print(statement.format(my_list)) # Printing the list of values entered by the user. 

print() # This is for an empty line between the print statements above and below. 


odd_list = [] # An empty odd list to which the odd user input will be appended. 

for numbers in my_list:
	if numbers % 2 != 0: # This like meams: If the reminder of the number when divided by 2 is not zero, then the number is odd. 
		odd_list.append(numbers) # We append the number to the list if it is odd. 
	else: 
		pass # Else, we perform no action.

print("The odd numbers of the list are: {}".format(odd_list)) # We are printing the odd list. 


even_list = []  # An empty even list to which the even user input will be appended. 

for numbers in my_list: 
	if numbers % 2 == 0: # This like meams: If the reminder of the number when divided by 2 is zero, then the number is even. 
		even_list.append(numbers) # We append the number to the list if it is even. 
	else: 
		pass # Else, we perform no action.

print("The even numbers of the list are: {}".format(even_list)) # We are printing the even list. 



