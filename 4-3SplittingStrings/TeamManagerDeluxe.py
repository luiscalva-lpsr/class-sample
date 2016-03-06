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

def saveTeam(playerlist, filename):
	userFile = open(filename, 'a')
	for player in FUT:
		userFile.write(player.name + " "  + str(player.age) + " " + str(player.goals) + " "  + str(player.kitNumber) + " "  + str(player.position) + '\n')
	userFile.close()


def loadTeam(filename):
	list = []
	userFile = open(filename, 'r')
	myString = userFile.readline()
	while myString != "":
		myLine = myString.split()
		list.append(Player(myLine[0], myLine[1], myLine[2], myLine[3], myLine[4]))	
		myString = userFile.readline()
	userFile.close()
	return list

#prints the words in the parenthesis
print("Welcome to team manager delux!" + '\n' + " Would you like to load an exising team?")
print("1. To load team")
print('2. To start a new team')
#creates a variable and sets its value to whatever the user inputs
teamManagerChoice = int(raw_input())

if teamManagerChoice == 1:
	print("Enter your team file name plus its 'tmd' extension.")
	userfile = raw_input()
	TheTeam = loadTeam(userfile)
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
			teamManagerChoice = teamManagerChoice - 1

else:
	list = []
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
 
 
