
You are going to finish a function that will mimic an `if` program from Module 1.  The `if` program is here below for you to use. 

    if age ==16:
          print ('you can get your license')
      elif age < 16:
          print ('you are too young')
      else:
          print ('you already have your license')
      
- Create a function that will use the variable `age` and the `if` statement. 
- Then call that function in the main part of your program.

{Check It!|assessment}(code-output-compare-2344740477)

||| guidance
# Solution
```python
#age will be sent from challenge
age = int(sys.argv[1])

#function
def DriveStatus():    #student may name it different
  age=14
  if age ==16:
      print ('you can get your license')
  elif age < 16:
      print ('you are too young to get your license')
  else:
      print ('you already have your license')
      
#main program     
DriveStatus()
```
|||


