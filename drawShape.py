import turtle

def drawSide(myTurtle):
	count = 0
	while count < 4:
		drawVee(myTurtle)
		count = count + 1

def drawVee(myTurtle):
	myTurtle.forward(20)
	myTurtle.right(90)
	myTurtle.forward(20)
	myTurtle.left(90)
	
shawn = turtle.Turtle()

count = 0

while count < 4:
	drawSide(shawn)
	shawn.right(90)
	shawn.backward(20)
	count = count + 1

turtle.exitonclick()
