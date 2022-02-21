#Python program to check leap year using Nested if statements
year=int(input("Please enter the year for check leap or not: "))
#Ask input from the user and store the value in the year variable
if(year%4==0):
    if(year%100==0):
      if(year%400==0):
          #if the all statements are true
    # it is a leap year
       print("%d is a leap year"%year)
       #if the all statements are false
    # it is not a leap year
      else:
        print("%d is not a leap year"%year)
    else:
      print("%d is a leap year"%year)
      #it is a leap year
else:
    print("%d is not a leap year"%year)