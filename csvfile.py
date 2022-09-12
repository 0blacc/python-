from fileinput import filename

#typically when you use comma separated variable files, you use csv
fileName = 'userDetails.csv'
accessMode = 'w'
UserD = input('please enter Name and surname')
userAge = input('Enter your age')
myfile = open(fileName, accessMode)
myfile.write(UserD+','+userAge+'\n')
myfile.write("Tebogo Ramonyai, 23 \n")
myfile.write("Lesedi Monakhisi, 25 \n")
myfile.write("Lememo Mapoti, 23")
myfile.close()
