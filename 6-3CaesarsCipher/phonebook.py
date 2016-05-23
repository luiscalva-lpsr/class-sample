PhoneBook = {}

while 805 == 805:
	print("Welcome to your phonebook" + '\n' + "Please enter what you would like to do:")
	print("1. Create contact")
	print("2. Show contacts")
	print("3. Enter contact name")
	print("4. Exit phonebook")
	choice = int(raw_input())
	
	if choice == 1:
		print("Enter name:")
		contactName = raw_input()
		print("Enter phone number:")
		number = int(raw_input())
		PhoneBook[contactName] = number
	if choice == 2:
		print("Contacts:")
		print(PhoneBook)
	if choice == 3:
		print("Enter the name of the person's whose number you want to retrive:")
		name = raw_input()
		print(PhoneBook[name])
	if choice == 4:
		exit()
