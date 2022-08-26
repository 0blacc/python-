import datetime

#if then otherwise 
#elif = elsde if (its not indented, if will run otherwise)
#this is a compound if statement
#oder doea matter
print('=================================================')

todaysDate = datetime.datetime.today()
print('Todays date and time : ', todaysDate , '\n')

country = input('Where are you from :').upper()
total1 = 0
if country == 'CANADA' :
    print(' Hey you win a canadian doll ')
    total1 = int(input('Enter the total amount of your order'))
    if total1 > 500 :
        print('You get free shipping')

elif country == 'NIGERIA' : 
    print('you are probably a scammer')

elif country == 'AUSTRALIA' : 
    print('HELLO mate')    
else :
    print('Thank you for your interest')