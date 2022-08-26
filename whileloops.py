#while is repeating events you dont know how many times they will happen
#


from typing import Counter


ageOfuser = 4
counterA = 0
while ageOfuser < 18 :
    ageOfuser = int(input('How old are you :'))
    print('Sorry you are not old enough')
print('Thank you')
multplesOf = 1
print('times tables')
while counterA < 5 :
    
    print('1 x ' , counterA, '= ', multplesOf * counterA)
    counterA = counterA + 1
    multplesOf = multplesOf +1
    print(counterA)