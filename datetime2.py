from datetime import datetime


import datetime
from xmlrpc.client import DateTime

# date_time_str = '2018-06-29 08:15:27.243860'
# date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')

# print('Date:', date_time_obj.date())
# print('Time:', date_time_obj.time())
# print('Date-time:', date_time_obj)
userInput = input('please enter your birthdate(dd/mm/yy)')
currentdaate = datetime.date.today()
#converting the user input into a date 
birthday =datetime.datetime.strptime(userInput,'%d/%m/%Y').date
print(userInput)



days = currentdaate - birthday
print(days)