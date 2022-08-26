myGuest = ['I', 'still', 'love']

#update a list

myGuest[2]= 'hate'
print(myGuest[2])

#adding items
#items will be added at the end
myGuest.append('you')
print(myGuest[-1])

#removing an item from a list(doesnt leave a blank )
myGuest.remove('still')
#or you can use delete
del myGuest[0]
#the following command shows you the last item on the lsit
print(myGuest[-1])