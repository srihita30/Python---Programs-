# This program will find the prime factors of a user entered number. 

'''
In order to find the prime factors we perform the following method: 

1) We require two while loops - one inner and one outer.   
    - The outer while loop'll check if the counter val is a factor of the input number.  
        - We can do this since the counter is iterating through all the numbers from 1 to the input number.
        - We also named the counter - "counter" :)
    - The inner while loop'll check if the counter has any other factors other than itself & 1. 
        - We will check for this counter value only if it's a factor of the user input.
        - In other words, the inner while loop will check if this counter is a prime factor of the input value. 

2) In the inner while loop we will have a counter called 'y' just like we did for the outer while loop. We will also have a variable x. 
    - This counter 'y' will iterate through all the values from 1 to the counter value.
    - While iterating, it'll check for its divisibility with the counter val for each number. 
    - If it is divisible then we increment x.  
    - Else we pass. 
    - If x = 1, after we come out of the inner while loop, then this means the counter, from the outer loop, is a prime factor. 
        * This is because the only factors this counter has are 1 and the number itself. 
        * Hence the counter is now a prime factor of the user input.
        * We then append it to the prime list and print the same. 
              
* "1" will not be included in the rpime_list since it is not a prime number.
'''

user_input = int(input("Enter a number to find its prime factors: "))

# Let's write a function within which we will find the prime factors of the user input. 

def prime_factors(user_input):

    '''
    The counter value below will iterate through all the numbers till the user input and check if they are factors of the input. 
    If they are factors, then inside the nested loop this counter will be used to check if it is a prime factor. 
    '''
    counter = 1
    prime_list = [] # We have created an empty list to which the prime factors will be appended.  
    
    '''
    The while loop below will allow the counter to loop through all numbers from 1 to the user input number. 
    Hence, we can check the divisibility of each number with the user input.  
    '''

    while(counter <= user_input):  
        
        x = 0 # This count vairable will be incremented when the counter value (which is a factor of the user input) is divisble by a certain number. 
        if(user_input % counter == 0):

            '''
            This variable, y, will iterate through all the value from 1 till the counter value. 
            It will then divide to check if the counter value has any factors. 
            We must remember that y is also a counter over here for the inner while loop. 
            '''
            y = 1
            while(y <= counter):
                if(counter % y == 0):
                    x = x + 1
                y = y + 1 # We increment the y variable. 
    
            '''
            The if condition checks if x remains at the count of 2. 
            If it does then this means that a certain factor of the user input (the counter value) only has factors of 1 & itself, and is hence a prime number. 
            '''
            if (x == 2): 
                prime_list.append(counter) # Since the counter value is a prime factor of the user input, we append it to the prime list.  
            else: 
                pass

        counter = counter + 1 # We increment the counter. 
    print("The prime factors list is: {}".format(prime_list)) 

prime_factors(user_input)