import turtle

def makeTriangle(myTurtle, side):
	myTurtle.fd(side)
	myTurtle.left(120)
	myTurtle.fd(side)
        myTurtle.left(120)
	myTurtle.fd(side)
        myTurtle.left(120)

#make our turtle
kipp = turtle.Turtle()
kipp.forward(150)
kipp.right(180)

#kipp makes triangles centered at a point that shifts 

#then decreases in size wih each loop
length = 100
while length > 0:
	makeTriangle(kipp, length)
	kipp.fd(3)
	length = length - 1
  
