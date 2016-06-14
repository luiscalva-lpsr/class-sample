# Caesar Cipher Decoder
# Author: Luis Calva


# import statements here
import string


# calls function to create a list with the letters from a to z
# DOES NOT manually create the list
# use Google and/or Stack Overflow to find how to do this in python!
# returns a list with the lowercase letters a to z
def getLowercaseAlphabet():
    alphabetLow = list(string.ascii_lowercase)
    return alphabetLow

def getUppercaseAlphabet():
	alphabetUp = list(string.ascii_uppercase)
	return alphabetUp

def getReorderedLowercaseAlphabet(key):
	alphabet = string.ascii_lowercase
	lowerCase = []
	letter = 0
	while letter != 26:
		lowerCase.append(alphabet[(key+letter) % 26])
		letter = letter + 1
	return lowerCase



# makes a mapping of encoded alphabet to decoded alphabet
# arguments: key
# returns: dictionary of mapped letters
def createDictionary(key):
	lower = list(string.ascii_lowercase)
	upper = list(string.ascii_uppercase)
	mapped = {}
	count = 0
	for a in lower:
		mapped[a] = lower[(count + key) % 26]
		count = count + 1
	for A in upper:
		mapped[A] = upper[(count + key) % 26]
		count = count + 1
	mapped[" "] = " "
	return mapped
	
# gets the encrypted message from the user
# print message user typed
# arguments: none
# returns: encoded message
def getMessage(message):
	return message

# for each letter in the message, decodes and records 
# arguments: encoded message, dictionary 
# returns: decoded message
def decodeMessage(message, dictionary):
	newMessage = ""
	for msg in message:
		aMSG = dictionary[msg]
		newMessage = aMSG + newMessage
	return newMessage

# outputs the decoded mesage to the terminal 
# arguments: decoded message
# returns: none
def printMessage(newMessage):
	print(newMessage)

# execution starts here

# ask user for a key
print("What key would you like to use to decode?")

userKey = int(raw_input())

dictionary = createDictionary(userKey)

print("What is the message you want to decode?")
message = raw_input()
encodedMessage = getMessage(message)
decodedMessage = decodeMessage(encodedMessage, dictionary)

print("here is your message")
print("")
printMessage(decodedMessage)
exit()
