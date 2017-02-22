The last example was very simplistic and most likely would never be used in a program.  What would happen instead is that information would be sent to and from the function. 

Think of it this way 

- Joe goes to the movie theater.  
- He gives the teller money 
- and the teller gives him a ticket. 


The teller could be a function:  
- Money is given (called a parameter)
- Function does a task (does some calculations, prints out the ticket)
- Ticket is given (called return)

![Movie Ticket Teller](.guides/img/movieteller1.jpg)


There are actually 4 ways a parameters/returns can be used

1. no parameter, no return - function does everything inside of it (our first FindSalary example) 
2. yes parameter, no return - function received data but doesn't return any data
3. no parameter, yes return - function doesn't receive anything but returns some data
4. yes parameter, yes return - function receives data and returns data (Movie Teller example)