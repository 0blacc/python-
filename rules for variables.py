#rules of python variables
#1 its case sensitive  (be consistant)
#2 its space sensive
#you can not start a variable name with a number
#commands are case sensitive

#using camelCasing and PascalCasing
firstName = input('What is your name ?')
lastName =  input('what is yout surname ?')

country = input('what is your country')
country = country.upper()
print(country)
#show the details
print('Details: '+ firstName+' '+lastName)
print('\nYour name is '+' :'+ firstName+'\nYour surname :'+ lastName+'\nyour country :'+country )

#manipulating the string variables
#string functions 
print(firstName.upper())
print(lastName.lower())
print(lastName.swapcase())