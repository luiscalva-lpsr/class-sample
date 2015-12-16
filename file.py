def listAvg(myList):
        mySum = 0
        myCount = 0
        for myItem in myList:
                mySum = mySum + myItem
                myCount = myCount + 1
        avg = mySum / myCount
        return avg
 
myGrades = [80, 90, 100, 60, 30, 20]
myAvg = listAvg(myGrades)
print("My average is " + str(myAvg))
 
yourGrades = [100, 90, 100, 60, 100, 100]
yourAvg = listAvg(yourGrades)
print("Your average is " + str(yourAvg))
