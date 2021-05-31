# This code will count the number of prime numbers upto a certain user entered number. 

input_number = int(input("Enter the number upto which you want to count the prime numbers: "))

def prime_num_counter(input_number):

    prime_num_list = [2] # To store the values of the prime numbers list. 
    x = 3 # x is the counter that is going upto the input input_number. 
    
    if input_number < 2:  # Check for 0 and 1 input. 
        return 0
        
    # If the "of" condition failed, then enter while loop. 
    while x <= input_number: # Iterate  through input_number list qith x. 

        for y in range(3,x,2):  # Check if x is prime with y. 
        
            if x%y == 0:
                x += 2 # Increment counter to hop ahead of the even number. 
                break # Break out of it the if condition. 

        else: # But if we have a prime number, then we have this else condition. 
            prime_num_list.append(x) # Append the prime number to the primes list. 
            x += 2 # Jump ahead the even number. 

    print('The prime numbers list is: {}'.format(prime_num_list))
    print('The number of prime numbers are: {}'.format(len(prime_num_list)))


prime_num_counter(input_number)