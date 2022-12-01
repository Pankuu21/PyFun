import turtle
import random
t=turtle.Turtle()
t.speed(0)
def curve(n):
    for i in range (n):
        turtle.left(i)
        turtle.fd(5)
for i in range (100):

    die=[0,1,2,3,4,5,6]
    curve(10*random.choice(die))
    t.stamp()

