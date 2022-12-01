# import turtle
import turtle
# import random
from random import randint
 
roja=turtle.Turtle()
# speed to draw to color
roja.speed(0)
 
# size of the pen
roja.pensize(10)
 
# colormode should be 255 to
# show every type of color

roja.shape('turtle')
 

# To display the color continuously the
# while loop is true
while True:
     
    # randint will have random color based on
    # every randint the color will be called
        roja.color('red')
             
            # it will begin to fill the circle with color
        roja.begin_fill()
             
            # generate circle
        roja.circle(randint(1,100))
             
            # it will end to fill color
        roja.end_fill()
             
            # it will start to draw
        roja.penup()
             
            # x axis and y axis
        roja.goto(randint(-500, 500), randint(-300, 270))
             
            # it wil stop to draw
        roja.pendown()
