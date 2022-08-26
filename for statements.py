# repeating events 
# loops repeat  tasks
# turtle is used t use loops 

# is a little turtle who moves around the screan and draws
import turtle

# we can all methods in turdle

# rotate right x degrees
# turtle.color('red')
# turtle.right(90)

# steps is a variable name that keeps track of how many times you do soethisn
# steps = -1
#pythin starts counting at 0
for steps in range(4) :
    #this is the code that will be repeated
    # only the indented code is run

    turtle.forward(100)
    turtle.right(90)
    turtle.color('red')
    turtle.forward(150)
turtle.Screen().exitonclick()