#date time library
import datetime
from tkinter import Y
from xmlrpc.client import DateTime

todaysDate = datetime.date.today().strftime('%d/%m/%y')
print('Todays Date :' + todaysDate)
print('-------------------------------------------------')

#prompt the user to enetr Date of birth
userInput = input('enter your date of birth dd/mm/yyyy')
print(userInput)

userBirthdate = datetime.datetime.strptime(userInput,'%d/%m/%y').date()
print(userBirthdate)


#ageOfUser = todaysDate - birthDay
#print(ageOfUser)