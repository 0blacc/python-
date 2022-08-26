#loan Calculator

print('loan calculator \n')
costOfLoan = (input("please enter the cost of loan amount :"))
costOfLoan =float(costOfLoan)

interestRate = (input('please entr the interest rate :'))
interestRate = float(interestRate)/100

numberOfYears= (input('please enter the number of years o pay the loan :'))
numberOfYears= float(numberOfYears)


#interst1= (interestRate + 1.00)
#nminus1 = numberOfYears - 1.00

monthlyRepayments =float((costOfLoan * (interestRate + 1.00) * numberOfYears )/ ((interestRate + 1.00) * numberOfYears - 1.00 ))
print('your monthy payment amount is : {0:.2f}' .format(monthlyRepayments))
