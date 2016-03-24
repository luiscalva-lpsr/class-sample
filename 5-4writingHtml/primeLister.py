TheList = range(1,10001)
afile = open("primenumbers.txt", "w")

def isprime(num):
	for n in range(2, num):
		if num % n == 0:
			return False
	
	return True
			
for num in TheList:
	if isprime(num):
		afile.write(str(num) + "\n")
print("The numbers will be in the file 'primenumbers.txt'")

afile.close()
