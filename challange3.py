#shipping charges challane
totalPurchase = float(input('Please eneter your toal purchase amount'))
if totalPurchase < 50 :
    print('Your total before shipping : R{0:.2f}'.format(totalPurchase))
    totalPurchase = totalPurchase + 10.00
    print('Your Total after shipping : R{0:.2f}'.format(totalPurchase))
else : 
    print('your shipping is free ')
    print('your total with free shipping is : R {0:.2f}'.format(totalPurchase))

print('')
print("----------------------------------------------------")
print("Thank you for shopping wth us")