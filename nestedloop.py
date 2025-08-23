# NESTED CONDITIONS

# Problem1 - Write a Python program that checks if a number is positive and also checks if it's even using nested conditions.

num = int(input("Enter a number"))
if num>0:
    print("Number is positive")
      
    if num % 2 == 0:
        print("Number is also even number")
    else:
        print("Number is not even")
else:
    print("Number is not positive number")

# Problem2- Write a program that checks if marks are above 50, then further check if marks are above 75 to print 'Distinction'.

marks = int(input("Enter your marks:"))
if marks > 50 :
    print("Marks are above 50")
    if marks > 75 :
        print("Distinction")
else:
        print("Marks do not meet criteria")
    

# Problem3 - Write a Python program to check username and then password using nested conditions.

username = "admin"
password = "1234"
if username == "admin" and password == "1234":
   print("Login successful")
else:
    print("Unauthorised login")



