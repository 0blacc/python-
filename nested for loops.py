import turtle

numberSides = 100
for counter in range(numberSides):
    turtle.color('red')
    turtle.forward(10)
    turtle.right(360/numberSides)
    for steps in range(numberSides):
        turtle.color('blue')
        turtle.forward(10)
        turtle.right(360/numberSides)
turtle.Screen().exitonclick()