import turtle
picColor = input('enter the desired color')
lineLength = int(input ('Enter the desired line length '))
picAngle = int(input('enter teh angle you want the line to turn'))

while lineLength != 0 :
    turtle.color(picColor)
    turtle.forward(lineLength)
    turtle.right(picAngle)
    picColor = input('enter the desired color')
    lineLength = int(input ('Enter the desired line length '))
    picAngle = int(input('enter teh angle you want the line to turn'))  
print('Thank you')
turtle.Screen().exitonclick()