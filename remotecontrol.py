import turtle
from Tkinter import *
def star(myTurtle):
	side = 0
	myTurtle.color('purple')
	myTurtle.left(36)
	myTurtle.forward(100)
	while side < 10:
		myTurtle.left(144)
		myTurtle.forward(100)
		side = side + 1
# create the root Tkinter window and a Frame to go in it
root = Tk()
frame = Frame(root)

# create our turtle
shawn = turtle.Turtle()

# make some simple buttons
fwd = Button(frame, text='fwd', command=lambda: shawn.forward(50))
left = Button(frame, text='left', command=lambda: shawn.left(90))
right = Button(frame, text='right', command=lambda: shawn.right(90))
pu = Button(frame, text ='penup', command=lambda: shawn.pu())
pd = Button(frame, text ='pendown', command=lambda: shawn.pd())
bwd = Button(frame, text='bwd', command=lambda: shawn.backward(50))
shape = Button(frame, text='Shape', command=lambda: star(shawn))

# put it all together
fwd.pack(side=LEFT)
left.pack(side=LEFT)
right.pack(side=LEFT)
pu.pack(side=LEFT)
pd.pack(side=LEFT)
bwd.pack(side=LEFT)
shape.pack(side=LEFT)
frame.pack()

turtle.exitonclick()
