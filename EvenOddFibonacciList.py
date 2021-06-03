# This code will print the values of a fibonacci sequence for the number of values the user has requested for, and will also print the even and odd values in two separate lists. 

user_num = int(input("Enter the number of values upto which you want the Fibonacci numbers for : ")) # Takes input from the user for the size of the sequence. 

def fibonacci_sequence(user_num):

	x = 0 # First value of th sequence. 
	y = 1 # Second value of th sequence. 
	fibonacci_list = [0,1] # A list to store the fibonacci sequence. it already contains 0 and 1 as the starting values, so the logic only focuses on adding values from thereon. 
	even_list = [] # This is the list of the even values of the sequence. 
	odd_list = [] # This is the list of the odd values of the sequence.

	for value in range(0,user_num-2): # The for loop defining the range of iterations. Here we do user_num-2 since we already have the first two numbers, 0 & 1, in the fibonacci_list, and we want to increment it from hereon. 

	# A fibonacci sequence is one where we the sum of the previous two terms is equal to the next term. And hence we follow the logic below. 

		fibonacci_sum = x + y # The sum of the previous two terms equal to the next term.  
		fibonacci_list.append(fibonacci_sum) # We append this new value to the list. 
		# Now for moving towards the next value, we must asssign x to y and y to the sum, and find the sum of these two equal to the term after these two. 
		x = y 
		y = fibonacci_sum
		# We can then use these if else statements to append the sequence values to the even list or odd list depending on whether they satisfy the if condtion. 
		if fibonacci_sum%2 == 0: # A number will be even if it is divisible by two, hence the number mod 2 must be zero. 
			even_list.append(fibonacci_sum) # Append to even list, if even. 
		else: 
			odd_list.append(fibonacci_sum) # Else, if odd, append to odd list. 

	print("This is the list of fibonacci numbers: {}".format(fibonacci_list)) # Print the fibonacci sequence. 
	print("This is the list of the even fibonacci numbers: {}".format(even_list)) # Print the even numbers of the sequence. 
	print("This is the list of the odd fibonacci numbers: {}".format(odd_list)) # Print the odd numbers of the sequence.

fibonacci_sequence(user_num) # Call the function to execute.  






