#dates and time
#datetime class from library 
from datetime import date, datetime
#import the library so you can use the functions for date and time
import datetime
from this import d
from tkinter import Y
from xmlrpc.client import DateTime

currentDate = datetime.date.today()
#string from time (strftime) allows you to specify date format
print(currentDate.strftime
('Please attend our event on the day %d of  %B ,the year %Y'))
#%d is day, %b is months , %Y is year

print(currentDate.weekday())
#print(currentDate.month)
#print(currentDate.year)
#print(currentDate.day)
#functions give me something 
#methods do something

#ask user to input a date 
userInput = input('please enter your date of birth ')
birtdday = datetime.datetime.strptime(userInput, '%m/%d/%Y')
print(birtdday)