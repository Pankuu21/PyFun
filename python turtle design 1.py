
import random
import turtle
import math
bob=turtle.Turtle()
bob.speed(-200000)


bob.shape('turtle')
bob.shapesize(1)
bob.left(180)
bob.speed(0)
bob.penup()
bob.forward(100)
bob.right(180)
bob.pendown()
bob.getscreen().bgcolor('black')
colorlist=['purple','indigo','blue','green','yellow','orange','red']
bob.pensize(2)

for i in range(25):
      bob.color(colorlist[i%7])
      bob.circle(200)
      bob.right(12)

