# This code will print the values of a fibonacci sequence for the number of values the user has requested for, and will also print the even and odd values in two separate lists. 

user_num = int(input("Enter the number of values upto which you want the Fibonacci numbers for : "))

def fibonacci_sequence(user_num):

	x = 0
	y = 1 
	fibonacci_list = [0,1] 
	even_list = []
	odd_list = []

	for value in range(0,user_num-2):

		fibonacci_sum = x + y 
		fibonacci_list.append(fibonacci_sum)
		x = y 
		y = fibonacci_sum

		if fibonacci_sum%2 == 0: 
			even_list.append(fibonacci_sum)
		else: 
			odd_list.append(fibonacci_sum)	

	print("This is the list of fibonacci numbers: {}".format(fibonacci_list))
	print("This is the list of the even fibonacci numbers: {}".format(even_list))
	print("This is the list of the odd fibonacci numbers: {}".format(odd_list))

fibonacci_sequence(user_num)






