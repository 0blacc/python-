#and statements
# and statements take precendence overf or statements 
# and overwrites evrythng
# #========================================================= 
#both statements have t be true for the code to execute 
#when you have more than 1 conditon that needs to be fulfilled
#true and  true = true
from pickle import TRUE

#user input
amount = 1000
gender = input('Are you male or female : ').upper()

#boolean variable for gender set to false
isFemale = False

#check the gender of the user
if gender == "FEMALE" :
    isFemale = True
else :
    isFemale = False

lottoNumber1 = int(input('Enter first lottery number :'))
lottoNumber2 = int(input('Enter powerball number :'))
isPowerballWinner = False
if lottoNumber1 == 3 and lottoNumber2 == 5 :
    isPowerballWinner= True
elif lottoNumber1 !=3 and lottoNumber2 != 5 :
    isPowerballWinner = False


if isPowerballWinner == True and isFemale== True :
    print("You are the new " , gender , "powerball winner" )
else :
    print('else you are not the winner sorry')