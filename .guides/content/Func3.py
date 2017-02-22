#__________________________________________________________________
#notice the variable bill is inside the parenthesis. 

def FindSalary():
    hours = 40
    rate = 15
    bills = 2100
    salary = hours * rate * 4  #4 weeks in a month

    return round((salary - bills),2)   
#__________________________________________________________________



#__________________________________________________________________
#main part of program

afford = FindSalary()   
print ("You can afford a car payment of ", afford)
print ("Go find your car now!")

#__________________________________________________________________