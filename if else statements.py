#else is ran if the condition is not true
deposit = float(input('how much do you want to deposit'))
if deposit > 100 :
    print("You get a cup, you get a free cup \n everybody gets a cup")
else :
    print('sorry, no cup for you')



#boolean variables : stores a value of true or false
#you have to initialize a boolean variable
freeToaster = False
if deposit > 100 :
    freeToaster = True

if freeToaster :
    print('Thank you')
print('have a nice day')
