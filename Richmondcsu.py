print("How many miles away do you live from Richmond")
miles = int(raw_input())

print("What's your GPA?")
GPA = float(raw_input())

print("What's your ACT score?")
ACT = int(raw_input())

if miles <= 30:
        if GPA >= 2.0 and ACT >= 13:
               print("you have been accepted to Richmond State")
        else:
               print("You have not been accepted to Richmond State")
else:
        if GPA >= 2.5 and ACT >= 18:
               print("You have been accepted to Richmond State")
               
        else:  
               print("You have not been accepted to Richmond State") 
