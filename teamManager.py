# creates a class called player
class Player(object):
	# creates the stats each player will have (age, name, goals)
	def __init__(self, name, age, goals):
		self.name = name
		self.age = age
		self.goals = goals
	
	# If a player scores a goal it adds plus 1 to his/her stats
	def goal_scored(self):
		self.goals = self.goals + 1
	
	# prints the player's information 
	def show_stats(self):
		print('Kit Name: ' + self.name)
		print('Age: ' + str(self.age))
		print('goals: ' + str(self.goals))

# players already in the team

# creates a player with the following stats
Eduardo = Player('Mota', '14', '2')

#creates a player with the following stats 
Hector = Player('Hecator', '15', '4')

#creates a blank list
FUT = []

#appends players already created 
FUT.append(Eduardo)
FUT.append(Hector)


#prints the words in the parenthesis 
print("Welcome to team manager. Press 5 to start")

#creates a variable and sets its value to whatever the user inputs 
leave_teamManager = int(raw_input())

#creates a while loop that starts up the 'Team manager' game
while leave_teamManager == 5:

	#gives the user the options of what to do by picking a number
	print('This is the main menu')
	
	print("Pick a number")

	print("1. Add player 2. View players 3. Exit Team Manager")	

	#creates a variable and sets it to the user choice
	choice = int(raw_input()) 
	
	#creates a while loop for the first option in the game
	while choice == 1:
		
		#asks the user to input the name of custom player
		print('Enter player name: ')
		user_player_name = raw_input()

		#asks the user to input the age of the custom player
		print("Enter player age: ")
		user_player_age = raw_input()

		#asks the user to input the number of goals of the custom player
		print('Enter player goals: ')
		user_player_goals = raw_input()
		
		#adds the custom player to the squad(list)
		FUT.append(Player(user_player_name, user_player_age, user_player_goals))
		
		#gives the user the option to go the main menu or keep adding players
		print("Enter 0 to go back to the main menu. Press enter to add another player")
		menu_button = int(raw_input())
		
		#ends option one loop
		if menu_button == 0:
			choice = 0	
	
	#creates a while loop for the second choice (views players in squad)
	while choice == 2:
		#makes a for loop that prints the player stats until all players are displayed
		for player in FUT:
			player.show_stats() 
		
		#tells user to go back to the main menu
		print('Enter 0 to go back to the main menu')
		menu_button = int(raw_input())
		if menu_button == 0:
			choice = 0
	# makes a while loop to exit the game
	while choice == 3:
		("Press 4 again to confirm 'exit'.")
		choice = 0

		leave_teamManager = leave_teamManager + 1
	

