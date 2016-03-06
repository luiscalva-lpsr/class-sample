Haiku = []

# greets the user 
print("Welcome to the Haiku Generator!")

# tells the user to write the first line of their haiku
print("Enter the first line of your haiku")

#creates a variable for the user to input a line
firstLine = raw_input()

# tells the user to write their second line of their haiku
print('Enter the second line of your haiku')

# creates a varible for the user to write their second line for their haiku
secondLine = raw_input()

# tells the user to input the third line of their haiku 
print('Enter the third line of your haiku')

# creates variable for the user to intput their last line for haiku
thirdLine = raw_input()

# tells their user to give their haiku a title
print('Enter the name of your Haiku')

# creates a variable for the user to write their haiku's title
userHaiku = raw_input()

# creates a variable and makes its value open the file the user created for his haiku
userFile = open(userHaiku, 'w')

# creates a list that contains all the lines of the user's haiku
Haiku.append()

# creates a for loop that writes to a new file writing each line of the haiku on separate line 
for line in Haiku:
	userFile.write(str(line) + '\n')
# closes the file
userFile.close()

# tells the user what to write to view their haiku
print("Done! to view your haiku type cat and then the name of your file at the command line")



