#addition + ,subtraction -,multiplication * ,divison / ,exponent **
#modulo %
#order of operations work here(my dear aunt sally)

#variables
area = 0
height = 10
width = 20

#calculating the area 
area = width * height/10

#shown to the user
print('the area of triangle is is: %d ' %area) #decimal (whole integers)
print('the are is  : %f ' %area) #float (value which has decimals)
print('the area is : %.2f' %area) #specifies number of decimal places
print('the area is : %6d'%area)#make number 6 digits long (width)
print('the area is : %06d'%area)#takes up 6 digits leading with 6 0s

#.format synax
print("the area 1 is : {0:f}".format(area))
print("the area 1 is : {0:d} the secons is {1:.2f}".format(42,area) )


#inputting numbers 
salary = int(input('enter a your salary amount1'))
bonus = int(input("please enter yur bonus amount"))
paychecAmaount = salary + bonus
print(paychecAmaount)
