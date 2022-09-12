#=when reading a csv file you have to import the file
import csv

#reader funtion returns the vlaues in the files as a list
# assumes that values are separated by a comma by default
# datafromfiles = csv.reader(myCSVFiles)

fileName = "AnimalWorld.txt"
accessMode = "r"

with open(fileName , accessMode) as myCSVFile :
    #read file comments 
    dataFromFile = csv.reader(myCSVFile)

    for currentRow in dataFromFile :
        for currentWord in currentRow:
            print(','.join(currentRow ))
