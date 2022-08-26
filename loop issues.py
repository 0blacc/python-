import turtle
#make sure your consition changes 
#if your loop ins inifine, use the stop debugging 

moverA = 0

while moverA < 4 :
    turtle.color('blue')
    turtle.forward(100)
    turtle.right(90)
    turtle.color('red')
    moverA = moverA +1
turtle.Screen().exitonclick()