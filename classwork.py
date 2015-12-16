import turtle

z = turtle.Turtle()
x = turtle.Turtle()

count = 100
turtle.colormode(255)

def makeStar(myTurtle):
	side_count = 0
	while side_count < 10:
		myTurtle.color(138, 4, 186)
		myTurtle.forward(side)
		myTurtle.left(36)
		myTurtle.forward(side)
		myTurtle.color(255, 0, 2)
		myTurtle.right(157)
	
side = 200
radius = 100
while count < 100:
	makeStar(x)
	z.circle(radius)
	side = side - 10
	radious = radious - 10
turtle.exitonclick()
