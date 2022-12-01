import turtle
import time
import random

wn=turtle.Screen()
wn.bgcolor('white')
wn.setup(width=1.0, height=1.0, startx=None, starty=None)



t=turtle.Turtle()
t.speed(0)
t.pencolor("#640AC2")

pen=turtle.Turtle()
pen.penup()
pen.ht()
pen.goto(150,350)

t.ht()
t.penup()
t.goto(-120,360)
t.pendown()
t.write("Turtle Race", font=("Comic Sans MS",30, "bold"))
t.pencolor("black")
t.penup()
t.goto(-700,240)
t.pendown()
t.pensize(3)
t.forward(200)
t.right(90)
t.forward(400)
t.right(90)
t.forward(200)
t.right(90)
t.forward(400)

a=turtle.Turtle()
a.speed(5)
a.penup()
a.shape('turtle')
a.pensize(3)
a.shapesize(1.5)
a.goto(-650,200)
a.color('#DC143C')

b=turtle.Turtle()
b.speed(5)
b.penup()
b.shape('turtle')
b.pensize(3)
b.shapesize(1.5)
b.goto(-650,100)
b.color('#00FA9A')

c=turtle.Turtle()
c.speed(5)
c.penup()
c.shape('turtle')
c.pensize(3)
c.shapesize(1.5)
c.goto(-650,0)
c.color('#1E90FF')

d=turtle.Turtle()
d.speed(5)
d.penup()
d.shape('turtle')
d.pensize(3)
d.shapesize(1.5)
d.goto(-650,-100)
d.color('#8A2BE2')

e=turtle.Turtle()
e.speed(5)
e.penup()
e.shape('turtle')
e.pensize(3)
e.shapesize(1.5)
e.goto(-570,200)
e.color('#6600FF')
f=turtle.Turtle()
f.speed(5)
f.penup()
f.shape('turtle')
f.pensize(3)
f.shapesize(1.5)
f.goto(-570,100)
f.color('#CCFF00')

g=turtle.Turtle()
g.speed(5)
g.penup()
g.shape('turtle')
g.pensize(3)
g.shapesize(1.5)
g.goto(-570,0)
g.color('#F06292')

h=turtle.Turtle()
h.speed(5)
h.penup()
h.shape('turtle')
h.pensize(3)
h.shapesize(1.5)
h.goto(-570,-100)
h.color('#FDD835')

t.ht()
t.penup()
t.home()
t.goto(0,-350)
t.pendown()
t.pencolor("white")
t.fillcolor("pale green")
t.begin_fill()
t.circle(350)
t.end_fill()

t.penup()
t.goto(0,-310)
t.pendown()
t.fillcolor("pink")
t.begin_fill()
t.circle(310)
t.end_fill()

t.penup()
t.goto(0,-270)
t.pendown()
t.fillcolor("yellow")
t.begin_fill()
t.circle(270)
t.end_fill()
t.penup()


t.penup()
t.goto(92.35,-253.72)
t.pendown()
t.pensize(3)
t.goto(119.71,-328.89)
t.pencolor("black")
t.penup()
t.goto(0,-270)
t.pendown()
t.pensize(8)
t.goto(0,-350)

#green turtle
bob=turtle.Turtle()
bob.penup()
bob.shape('turtle')
bob.pensize(3)
bob.shapesize(1.5)
bob.goto(0,-330)
bob.speed(0)
bob.color('#038D05')
bob.circle(330,20)
print(bob.position())

#pink turtle
jim=turtle.Turtle()
jim.penup()
jim.shape('turtle')
jim.pensize(3)
jim.shapesize(1.5)
jim.goto(0,-290)
jim.speed(0)
jim.color('#CD047D')
jim.circle(290,20)
print(jim.position())

#taking player names
player1name=turtle.textinput("name","Player 1")
player2name=turtle.textinput("name","Player 2")

die=[7,10,15,19]

pen.goto(270,300)
pen.color('#DA6E0C')
pen.write("Welcome to the race {} and {}.".format(player1name,player2name), move=True, align='left', font=('Gisha', 18, 'bold'))
turtle.ontimer(pen.undo(), t=1000)

pen.color('#383838')
pen.goto(300,340)
pen.write("The rules of the game are as follows:".format(player1name,player2name), move=True, align='left', font=('Arial', 12, 'normal'))
pen.goto(270,310)
pen.write("1.Each player gets a chance to roll the die alternately".format(player1name,player2name), move=True, align='left', font=('Arial', 12, 'normal'))

pen.goto(270,290)
pen.write("2.The player has to press the 'Enter' key to roll the die.".format(player1name,player2name), move=True, align='left', font=('Arial', 12, 'normal'))

pen.goto(270,270)
pen.write("3.The die will take up random values.".format(player1name,player2name), move=True, align='left', font=('Arial', 12, 'normal'))

pen.goto(270,250)
pen.write("4.The turtle will move ahead accordingly.".format(player1name,player2name), move=True, align='left', font=('Arial', 12, 'normal'))


pen.goto(270,230)
pen.write("5.The player whose turtle crosses the black finish line first, wins".format(player1name,player2name), move=True, align='left', font=('Arial', 12, 'normal'))

pen.goto(380,190)
pen.write("Good luck!".format(player1name,player2name), move=True, align='left', font=('Arial', 20, 'normal'))
pen.color('Black')
pen.goto(-20,-30)
pen.write("3".format(player1name,player2name), move=True, align='left', font=('Arial', 60, 'normal'))
turtle.ontimer(pen.undo(), t=1000)
pen.write("2".format(player1name,player2name), move=True, align='left', font=('Arial', 60, 'normal'))
turtle.ontimer(pen.undo(), t=1000)
pen.write("1".format(player1name,player2name), move=True, align='left', font=('Arial', 60, 'normal'))
turtle.ontimer(pen.undo(), t=1000)
pen.goto(-40,-10)
pen.write("Start!".format(player1name,player2name), move=True, align='left', font=('Arial',30, 'normal'))
turtle.ontimer(pen.undo(), t=1000)
while(1):
   
   print("Player 1's turn i.e pink turtle",player1name)
   p1=input("press 'enter' to move your turtle" )
   dieOut=random.choice(die)
   jim.circle(290,dieOut)
   if((0<=bob.xcor()<112.87)&(-330<=bob.ycor()<-310.10)):
      wn.clearscreen()
      winner=player2name
      
      break
   else:
       if((0<=jim.xcor()<99.19)&(-290<=jim.ycor()<-272.51)):
          wn.clearscreen()
          winner=player1name
          
          
          break
   print("Player 2's turn i.e green turtle",player2name)
   p2=input("press 'enter' to move your turtle" )
   dieOut=random.choice(die)
   bob.circle(330,dieOut)
   if((0<=bob.xcor()<112.87)&(-330<=bob.ycor()<-310.10)):
      winner=player2name
      wn.clearscreen()
      
      break
   else:
       if((0<=jim.xcor()<99.19)&(-290<=jim.ycor()<-272.51)):
          winner=player2name
          wn.clearscreen()
          break
         
wn=turtle.Screen()
wn.bgcolor('black')
wn.setup(width=1.0, height=1.0, startx=None, starty=None)


r=turtle.Turtle()
r.speed(0)


r.shape('turtle')
r.shapesize(1)
r.goto(-20,20)
r.pendown()
r.getscreen().bgcolor('black')
colorlist=['purple','indigo','blue','green','yellow','orange','red']
r.pensize(2)

for i in range(30):
      r.color(colorlist[i%7])
      r.circle(180)
      r.right(12)

pen=turtle.Turtle()

pen.penup()
pen.ht()
pen.goto(-500,0)
pen.color('white')
pen.pendown()
pen.write("Congratulations {}! You have won the race.".format(player1name,player2name), move=True, align='left', font=('Arial', 35, 'bold'))
