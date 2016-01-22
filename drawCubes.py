import turtle

#Draws multiple cubes with different color sides
def drawPattern(myTurtle):
	count = 0
	while count < 9:
		drawCubeLine(myTurtle)
		myTurtle.pu()
		myTurtle.backward(525)
		myTurtle.left(90) 
		myTurtle.fd(60)
		myTurtle.right(90)
		myTurtle.pd()
		count = count + 1

#Draws 8 cubes in a straigt line 
def drawCubeLine(myTurtle):
	count = 0
	while count < 8:
		myTurtle.pu()
		myTurtle.fd(70)
		myTurtle.pd()
		drawCube(myTurtle)
		count = count + 1

#Draws a cube with different color sides 
def drawCube(myTurtle):
	myTurtle.fillcolor("light blue")
	myTurtle.begin_fill()
	drawRhombus(myTurtle)
	myTurtle.end_fill()
        myTurtle.fillcolor("blue")
        myTurtle.begin_fill()
        drawRhombus(myTurtle)
        myTurtle.end_fill()
        myTurtle.fillcolor("dark blue")
        myTurtle.begin_fill()
        drawRhombus(myTurtle)
        myTurtle.end_fill()


#Draws a rhombus 
def drawRhombus(myTurtle):
		myTurtle.left(30)
		myTurtle.fd(40)
		myTurtle.left(120)
		myTurtle.fd(40)
		myTurtle.left(60)
		myTurtle.fd(40)
		myTurtle.left(120)
		myTurtle.fd(40)
		myTurtle.right(90)
#Creates a variable and sets its value to turtle
kronos = turtle.Turtle()

#increases the speed of kronos
kronos.speed(10000)
#kronos turns left 90 degrees
kronos.left(90)
#kronos picks up the pen so he won't draw
kronos.pu()
#kronos moves backwards 240 pixels 
kronos.backward(240)
#kronos turns right 90 degrees
kronos.right(90)
#kronos moves backward 35 degrees 
kronos.backward(35)
#kronos puts the pen down so he can draw
kronos.pd()
#creates a variable and sets its value to turtle
nero = turtle.Turtle()

#increases the speed of nero
nero.speed(10000)
#nero turns left 90 degrees
nero.left(90)
#nero picks the pen up
nero.pu()
#nero moves backwards 300 pixels 
nero.backward(300)
#nero turn right 90 degrees
nero.right(90)
#nero turns right 180 degrees
nero.right(180)
#nero moves forward 560 pixels 
nero.fd(560)
#nero turns right 180 degrees
nero.right(180)
#nero puts the pen down 
nero.pd()

#nero draws his part of the cube pattern 
drawPattern(nero)
#kronos draws his part of the cube pattern 
drawPattern(kronos)

turtle.exitonclick()
