# creates a class called player
class Player(object):
	# creates the stats each player will have (age, name, goals)
	def __init__(self, name, age, goals, kitNumber, position):
		self.name = name
		self.age = age
		self.goals = goals
		self.kitNumber = kitNumber
		self.position = position
	
	# prints the player's information
	def show_stats(self):
		print('Kit Name: ' + self.name)
		print('Age: ' + str(self.age))
		print('Goals: ' + str(self.goals))
		print('Kit Number: ' + str(self.kitNumber))
		print('Position: ' + str(self.position))

#creates a function that will save the file of the user's team
def saveTeam(playerlist, filename):
	# opens the file 
	userFile = open(filename, 'a')
	# makes a for loop that will write each player the user created to the file
	for player in FUT:
		userFile.write(player.name + " "  + str(player.age) + " " + str(player.goals) + " "  + str(player.kitNumber) + " "  + str(player.position) + '\n')
	# closes the file
	userFile.close()


# creates a function that will load a team the user created
def loadTeam(filename):
	# makes an empty list
	list = []
	# opens a list and reads it
	userFile = open(filename, 'r')
	# Creates a variable to read the curren line of the file
	myString = userFile.readline()
	# creates a while loop that will appen each player to the list in the code
	while myString != "":
		# splits the file turning each line into a list
		myLine = myString.split()
		# appends each line to the list 
		list.append(Player(myLine[0], myLine[1], myLine[2], myLine[3], myLine[4]))	
		# reads the nexr line of the file 
		myString = userFile.readline()
	#closes the file
	userFile.close()
	# returns the list of players
	return list

#prints the words in the parenthesis
print("Welcome to team manager delux!" + '\n' + " Would you like to load an exising team?")
print("1. To load team")
print('2. To start a new team')
#creates a variable and sets its value to whatever the user inputs
teamManagerChoice = int(raw_input())

# starts a loop for the first chioce
if teamManagerChoice == 1:
	print("Enter your team file name plus its 'tmd' extension.")
	# creates a varirable fot the user to input their file name
	userfile = raw_input()
	# loads the user's file
	TheTeam = loadTeam(userfile)
	# starts team manager game
	game = 0
	while game == 0:
		#gives the user the options of what to do by picking a number
		print('This is the main menu')
		
		print("Pick a number")
		print("1. Add player 2. View players 3. Save squad 4. Exit to main menu")
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
			
			#asks the user to input the number of goals of the custom player
			print('Enter player kit number')
			user_player_kitNumber = raw_input()
	
			#asks the user to input the position the player plays
			print('Enter player position')
			player_position = raw_input()
	
			#adds the custom player to the squad(list)
			TheTeam.append(Player(user_player_name, user_player_age, user_player_goals, user_player_kitNumber, player_position))
			
			#gives the user the option to go the main menu or keep adding players
			print("Enter 0 to go back to the menu.")
			menu_button = int(raw_input())
			
			#ends option one loop
			if menu_button == 0:
				choice = 0
		
		#creates a while loop for the second choice (views players in squad)
		while choice == 2:
			TheTeam = loadTeam(userfile)
		#makes a for loop that prints the player stats until all players are displayed
			for player in TheTeam:
				player.show_stats()
				
			#tells user to go back to the main menu
			print('Enter 0 to go back to the menu')
			menu_button = int(raw_input())
			if menu_button == 0:
				choice = 0
		# creates a variable for the user to save their team
		while choice == 3:
			# ask their user to title their team
			print("What would you like to title your team?")
			userfile = raw_input()
			# Saves the user's team
			saveTeam(FUT, userfile + ".tmd")
			# tells the user to return to the main menu
			print('Enter 0 to go back to the menu')
			menu_button = int(raw_input())
	 		if menu_button == 0:
				choice = 0
	
		# makes a while loop to exit the game
		while choice == 4:
			
			choice = 0
			game = game + 1
			teamManagerChoice = teamManagerChoice - 1

# starts a loop for the second choice of the team
else:
	# makes an empty list
	list = []
	# starts up team manager game
	game = 0
	while game == 0:

	
	       	#gives the user the options of what to do by picking a number
	        print('This is the main menu')
	 
	        print("Pick a number")
	        print("1. Add player 2. View players 3. Save squad 4. Exit to main menu")
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
	 
	                #asks the user to input the number of goals of the custom player
	                print('Enter player kit number')
	                user_player_kitNumber = raw_input()
	 
	                #asks the user to input the position the player plays
	                print('Enter player position')
	                player_position = raw_input()
	 
	                #adds the custom player to the squad(list)
			list.append(Player(user_player_name, user_player_goals, user_player_goals, user_player_kitNumber, player_position))
	
			#gives the user the option to go the main menu or keep adding players
	                print("Enter 0 to go back to the menu.")
	                menu_button = int(raw_input())
	 
	                #ends option one loop
	                if menu_button == 0:
	                        choice = 0
	 
	        #creates a while loop for the second choice (views players in squad)
	        while choice == 2:
	                #makes a for loop that prints the player stats until all players are displayed
	             
			for player in list:
	                        player.show_stats()
	 
	                #tells user to go back to the main menu
	                print('Enter 0 to go back to the menu')
	                menu_button = int(raw_input())
	                if menu_button == 0:
	                        choice = 0
	 	# Saves the team just like in option 1
	        while choice == 3:
	                print("What would you like to title your team?")
	                userfile = raw_input()
	                saveTeam(FUT, userfile + ".tmd")
	                print('Enter 0 to go back to the menu')
	                menu_button = int(raw_input())
	                if menu_button == 0:
	                        choice = 0
	 
	        # makes a while loop to exit the game
	        while choice == 4:
	 
	                choice = 0
			game = game + 1
	                teamManagerChoice = teamManagerChoice + 1
 
 
