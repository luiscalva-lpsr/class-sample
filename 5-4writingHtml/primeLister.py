#makes a list of numbers ranging from 1 to 10,000
TheList = range(1,10001)

#opens a file and allows it to be written on it
afile = open("primenumbers.txt", "w")

#creates a function that will find the remainder of all numbers in the list divided by all numbers in the list to determine which are prime numbers and which are not
def isprime(num):
	#writes a for loop 
	for n in range(2, num):
		#divides all the numbers in the list by all the numbers in the list and then shows their remainder
		if num % n == 0:
			return False
	
	return True
	
#writes a for loop which will find all the prime numbers and then write them in separate lines to a file 		
for num in TheList:
	if isprime(num):
		afile.write(str(num) + "\n")
print("The numbers will be in the file 'primenumbers.txt'")

#closes the file
afile.close()
