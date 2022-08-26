#nested statements.

from operator import truediv


isMonday = True
freshCoffe = False 

todayDay = input('What day is it :').upper()
isCoffee = input('Do you have coffee? :').upper()

if isCoffee == 'YES'  :
   freshCoffe = True
   print('you have coffee')
else :
    freshCoffe = False
    print('You do not have coffee')

if todayDay == 'MONDAY'  :
    isMonday = True
else :
    isMonday = False
    print('atleast its not monday')
#=================================================

if isMonday :

    if not freshCoffe :
        print('go buy cofee')
    print ('i hate mondays ')

print('now you can start work')