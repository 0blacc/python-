#making decisions with code 
#----------------------------------------------------------
#libraries 
import datetime
from tkinter import Y
#----------------------------------------------------------
#Date and time 
todaysDate = datetime.datetime.today()
print( 'Todays Date : ' , todaysDate.date())
print( 'Time now    : ' , todaysDate.now().time())
print('------------------------------------------')

#-----------------------------------------------------------
#if statements allow yputo specify code that only executes if a specific condition is tru
#== means equal to/ its not tye same as =
#!= not equal to / if not answer
#< less than 
#> greater than
#<= less than or equal to
#>= greater of equal to
totalAmount = float(567.345664)

answer1 = input("Would you like express shipping (YES/NO)? ").upper()
if answer1 == 'YES' :               
    print('')
    print('You will be charged extra R10 ')  

    answer2 = input('Is that okay? Y/N :').upper()
    if  not answer2 == 'N' :
        finalAmount = totalAmount + 10.00
        print('Your total before shipping :{0:.2f}'.format(totalAmount))
        print('your total amount after shipping is : {0:.2f}'.format(finalAmount))

print('')
print('Your Total is : {0:.2f}'.format(totalAmount))
print('Thank you for shopping at SIMS')
#------------------------------------------------------------------------------------
#if statemets with numbers

age = int(input('How old are you :'))
if age < 18 :
    print ('you are too young for alcohol')   
print('Thank you')

#always test >< and boundry conditions