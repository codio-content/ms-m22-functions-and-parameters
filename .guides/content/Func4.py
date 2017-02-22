#__________________________________________________________________
#notice the variable bill is inside the parenthesis. 

def FindSalary(bills):
    hours = 40
    rate = 15
    salary = hours * rate * 4  #4 weeks in a month
    return round((salary-bills),2)   
#__________________________________________________________________



#__________________________________________________________________
#main part of program

bills = 2100
afford = FindSalary(bills)   
print ("You can afford a car payment of ",afford)
print ("Go find your car now!")

#__________________________________________________________________