import turtle

def drawTriPattern(myTurtle):
	count = 0
	while count < 3:
		triLine(myTurtle)
		myTurtle.penup()
		myTurtle.backward(80)
		myTurtle.pendown()
		myTurtle.left(30)
		count = count + 1
	myTurtle.left(110)
	count = 0
	while count < 3:
		triLine(myTurtle)
		myTurtle.penup()
		myTurtle.backward(80)
		myTurtle.pendown()
		myTurtle.left(30)
		count = count + 1


def triLine(myTurtle):
	count = 0
	while count < 4:
		drawTriangle(myTurtle)
		myTurtle.penup()
                myTurtle.fd(20)
                myTurtle.pendown()
		count = count + 1		

def drawTriangle(myTurtle):
	count = 0
	while count < 3:
		myTurtle.fd(10)
		myTurtle.left(120)
		count = count + 1

Tri = turtle.Turtle()

drawTriPattern(Tri)

turtle.exitonclick()
