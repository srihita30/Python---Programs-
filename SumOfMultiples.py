# This program will print the the multiples of 3 or 5 below the user entered value and find their sum.  

#Below we will take input from the user, and use that number as a parameter for our function and to set the range for our for loop in that function.  
user_num = int(input("Enter a value upto which you want to print the mutliples of 3 or and 5 and find their sum: "))

def find_multiple_vals_sum(user_num): 

	sum = 0 # This variable is used to hold the sum of all the multiples. 
	list_of_multiples = [] # An empty list has been created to whihc multiples will be appended to later on. 

	# The for loop below will iterate through all the numbers below 1000 and return the sum of the numbers are multiples of 3 or 5. 
	for number in range(0,user_num): 

		# The if condition below will check if 3 the numbers in the range are mutliples of 3 or 5. 
		if number%3 == 0 or number%5 == 0: 
			sum = sum+number # If the are multiples then we add the numbers to the sum. 
			list_of_multiples.append(number)
		else: 
			pass # Else, we pass. 

	print("The list of all the multiples of 3 and 5 below 1000 is: {}".format(list_of_multiples)) # We print the list of multiples.
	print("The sum of all the multiples of 3 or 5 below 1000 is {}.".format(sum)) # We print the final sum. 


find_multiple_vals_sum(user_num) # We must call the function in order to execute. 