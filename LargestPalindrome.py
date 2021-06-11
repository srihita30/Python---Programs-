# This program will find the product of the first and the second largest 3-digit palindrome numbers. 

# This first function will check if a number in the given range is a palindrome. And if yes, then it will appaend it to the palindrome list. 

def palindrome_check(): 

	string_val = '' # This variable is to assign each integer value to the string and check if it is a palindrome through string slicing. 

	palindrome_list = [] # Empty list to whcih the palindrome values will be appended. 

	for val in range(100,1000):

		string_val = str(val) # We are converting the integer values into strings. 

		if string_val[::1] == string_val[::-1]: # This is used to check if the numbers are palindromes. We are checking for this by converting the numbers into strings. 
			palindrome_list.append(val) # If they are palindrome numbers, then we append them to the palindrome string. 
		else:
			pass

	return palindrome_list

#palindrome_check()

# This second function will check for the second largest palindrome in the list. (Keep in mind that we already know the first largest one to be 999)

def largest_palindrome(p_list): # The parameter passed for this function is the palindrome list from the previous one. 

	x = 0 # This variable will be used for comparing the numbers in the palindrome list, and for looping through the list.  
	
	while x < len(p_list)-2: 

		'''
		We are subtracting two from the length of the list. 
		1 is to avoid the list index out of range exception. 
		And the other 1 is to avoid going up until 999 again, since if we do then we would multiply 999 with itself instead of multiplying 999 with the second largest palindrome number. 
		'''
		
		if p_list[x+1] > p_list[x]: # This will compare the adjacent values of the list and check for which one is greater. 
			largest_second = p_list[x+1] # The largest_second variable is used for representing the second largest palindrome value. 
		else:
			largest_second = p_list[x] 

		x = x + 1
	return largest_second # We return the second largest palindrome number. 

#largest_palindrome()

# This third (and last) function will multiply the first and the second largest palindrome values to find their product and return the same. This is also the aim of the program. 

def palindrome_product(second_largest_palindrome): # The parameter passed for this function is the second largest palindrome found from the previous function. 

	first_largest_palindrome = 999 # The first largest three digit palindrome value. 
	
	product = first_largest_palindrome * second_largest_palindrome

	print(product)

	return product

 #palindrome_product()



p_list = palindrome_check() # We call the first function to check for palindromes and append them to a list. Then we returned this list.  
second_largest_palindrome = largest_palindrome(p_list) # We pass the palindrome list as a parameter for the second function to check for the second largest palindrome and return that. 
palindrome_product(second_largest_palindrome) # Then we call the thrid function which'll return the product of the first and second largest palindromes. 





