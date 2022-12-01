import turtle
import math
tim =turtle.Turtle()
tim.speed(10000000000000000)
tim.shape('turtle')
tim.color('blue')
tim.getscreen().bgcolor('yellow')
for i in range(430):
    tim.forward(math.sin(i*200)*250)
    tim.right(20)
