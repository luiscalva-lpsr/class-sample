import turtle

def draw4Ts(myTurtle):
	count = 0
	while count < 4:
		drawT(myTurtle)
		count = count + 1

def drawT(myTurtle):
        myTurtle.fd(50)
        myTurtle.backward(10)
        myTurtle.left(90)
	myTurtle.fd(10)
	myTurtle.backward(20)
	myTurtle.fd(10)
	myTurtle.left(90)
	myTurtle.fd(40)
	myTurtle.left(90)

Cas = turtle.Turtle()


draw4Ts(Cas)

turtle.exitonclick()
