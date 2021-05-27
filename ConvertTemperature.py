# This program will convert the user input temperature in celsius into fahrenheit. 

numberOfTemps = int(input("How many temperature values do you want to convert?\n")) # This will decide the number of temperature values the user wants to convert. 

x = 0
celcius_temps = [] # An empty list has been created, to which we add the user entered temperatures in celsius. 

# The while loop below will add the user entered values into the list of temperatures in celsius. 

while x < numberOfTemps: 

	celcius_temps.append(float(input("Enter the temperature in celsius:")))
	x = x + 1

print(f"These are the temperatures in celsius: {celcius_temps}")


fahrenheit_temps = [] # An empty list has been created, to which we add the converted temperatures in fahrenheit.
new_temp = 0.0 # This new_temp variable is a temporary placeholder for each of the temperature values that has been converted to fahrenheit before it is added into the list. 

# The for loop below will convert the user entered values in celsius into the list of temperatures in fahrenheit. 

for temp in celcius_temps:

	new_temp = (9/5)*temp + 32 # The conversion logic for celsius to fahrenheit. 
	fahrenheit_temps.append(new_temp) 
	final_temps = ["%2f" % values for values in fahrenheit_temps] # This is the final list of temperatures in fahrenheit, with the converted values rounded off to the second decimal place. 

print('These are the temperatures in fahrenheit:{}'.format(final_temps))








