import random

myNum = random.randint(1,1000)

print("I'm thinking of a number between 1 and 1000. Enter a guess!")

userNum = raw_input()

while userNum > 805:
	print("Nope, too low. Guess again.")
	userNum = raw_input()
	while userNum < 805:
		print("Nope, too high. Guess again.")
		userNum = raw_input()
else:
	print("Hooray! You got the number.")	
