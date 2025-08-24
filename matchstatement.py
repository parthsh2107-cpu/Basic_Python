# MATCH STATEMENTS

3 Problem1-Given a predefined variable day, write a Python program using the match-case statement to print the 'Thursday'. If the value does not match any of these, print "Invalid day" 



day = 4
match day:
       case 1:
          print("Monday")
       case 2:
            print("Tuesday")
       case 3:
            print("Wednesday")
       case 4:
            print("Thursday")
       case 5:
            print("Friday")
       case 6:
            print("Saturday")
       case 7:
            print("Sunday")
       case _:
            print("invalid day")

