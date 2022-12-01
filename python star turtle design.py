import turtle

bob=turtle.Turtle()
bob.speed(0)


bob.shape('turtle')
bob.left(180)
bob.penup()
bob.forward(100)
bob.right(180)
bob.pendown()
def star():
    bob.color('cyan')
    for i in range(5):
        bob.forward(10)
    
        bob.right(144)
def stars():
    bob.color('light blue')
    for i in range(5):
        
        bob.forward(50)
        star()
        bob.right(144)
def starss():
    bob.color('cyan')
    for i in range(5):
        bob.forward(100)
        stars()
        bob.right(144)

for i in range(5):
    
    bob.forward(300)
    starss()
    bob.right(144)
bob.color
