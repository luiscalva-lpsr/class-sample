import random

L = random.randint(5,100)

print("Welcome to the quest game!")

print("Enter your name:")

name = raw_input()

print("You have 15 points to spend.")

print("Enter strength:")

strength = int(raw_input())

print("Enter health:")

health = int(raw_input())

print("Enter luck:")

luck = int(raw_input())

if luck+health+strength > 15:
    print("You went over the skill points limit, your stats will be set to default: strength 5, health 5, luck 5.")
    luck = 5
    health = 5
    strength = 5
else:
    print("Your skills have been set. health:" + str(health) +  " luck:" + str(luck) + " strength:"+ str(strength))

print("You've come to come to a fork in the road. Do you want to go to the left, to the right, or stay there? Enter left, right, or stay?:")
path = raw_input()
if path == "right":
        if strength >= 6 or health >= 7:
                print("You came across an ice troll. You defeated him and kept his head as price.")
        else:
                print("You came across an ice troll. He tore you to peices and fed on your corpse.... what was left of it.")
                print("Your health or strength were not high enough.")
elif path == "left":
        if strength >= 8 or health >= 8:
                print("You came across a necromancer, you took him down and recovred his spell book.")
        else:
                print("You came across a necromancer, he defeated you easily and you became his skeleton slave.")
                print("Your luck or health were not high enough.")
elif path == "stay":
	if L >= 75 and luck >= 6: 
        	print("You decided to stay where you are and a horse with bags of gold showed up after  while. You are now the richest person in the kingdom") 
	else:
		print("You fell alseep after few hours and woke up in a dungeon which you never managed to escape.")
		print("You just weren't lucky enough.")
