#__________________________________________________________________
#notice the variable bill is inside the parenthesis. 

def FindSalary(bills):
    hours = 40
    rate = 15
    salary = hours * rate * 4  #4 weeks in a month
    afford = salary - bills
    print ("You can afford a car payment of ", round(afford,2))   
#__________________________________________________________________



#__________________________________________________________________
#main part of program

bills = 2100
#notice bill is being "sent" to function
FindSalary(bills)   
print ("Go find your car now!")

#__________________________________________________________________