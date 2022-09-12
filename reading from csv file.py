#reading from a csv file
#if you create a list , you need to be able to read it 
#example is a E-reader 
#create the file
fileName = 'AnimalWorld.txt'
animalFile = open(fileName, 'w')
animalFile.write('Tazmanian Brown ,Extinct')
animalFile.write('Tazmanian blue ,common')
animalFile.write('Tazmanian red ,Extinct')
#animalFile.close()

#step 1 : Open the file
animalFile = open(fileName,'r')

#read all file contents
#allFileContents = animalFile.read()
#print(allFileContents)
#print('')

#print first line
firstAnimal = animalFile.readline()
print(firstAnimal)