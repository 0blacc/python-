#index fucntion will search the lsits and return the inex position
#where the value was found
guests = ['I','Still ','Love', 'You', 'Lesedi', 'Monakhisi']
print(guests.index('I')) #this will return 2
#if index cannot find a value in the list, ypu will get  erro
steps = 0
#ow many values in the lst
numEntries = len(guests)

for steps in range(numEntries) :
    print(guests[steps])
    steps = steps +1 

#another loop

for guest in guests :
    print(guest)