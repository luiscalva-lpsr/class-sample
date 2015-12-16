import turtle

notshawn = turtle.Turtle()

notshawn.speed(1)

count = 0

while count < 20:
	notshawn.fd(5)
	notshawn.penup()
	notshawn.fd(5)
	notshawn.pendown()
	count = count + 1
	
#go to the lower left of the screen
notshawn.penup()
notshawn.goto(-100,-55)
#when you get ther, draw me a circle
notshawn.pendown()
notshawn.circle(10)





turtle.exitonclick()

