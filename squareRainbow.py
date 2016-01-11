import turtle
brush = ['blue','green','yellow','red']
def drawSquareRainbow(myTurtle):
	count = 0
	while count < 5:
		drawColorfulSqaure(myTurtle)
		turtle.pu()
		turtle.left(120)
		turtle.fd(40)
		turtle.pd()
		turtle.right(120)
		count = count + 1 

def drawColorfulSqaure(myTurtle):
	turtle.color('blue')
	drawSquare(myTurtle)
	turtle.color('green')
	drawSquare(myTurtle)
	turtle.color('yellow')
	drawSquare(myTurtle)
	turtle.color('red')
	drawSquare(myTurtle)

def drawSquare(myTurtle):
	count = 0
	while count < 4:
		turtle.fd(20)
		turtle.left(90)
		count = count + 1
	turtle.right(90)
	
Miguel = turtle.Turtle()

drawSquareRainbow(Miguel)

turtle.exitonclick()
