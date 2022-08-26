#or statement
#=======================================================


#only 1 condition should be true
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
if (lottoNumber1 == 3 or lottoNumber2 == 5) and amount == 1000:
    isPowerballWinner= True
elif lottoNumber1 !=3 and lottoNumber2 != 5 :
    isPowerballWinner = False


if isPowerballWinner == True and isFemale== True :
    print("You are the new " , gender , "powerball winner" )
else :
    print('else you are not the winner sorry')