#Assume age to be 20 years and check whether a person is eligible for voting
name = input("Enter your name here ")
age = int(input("Your age"))
if age> 18:
   print("You are eligible to cast vote")
else: 
    print("sorry u are not eligible ")

# Python statement to print login successful only if password is 1234 and username is admin
username =  "admin"
password = "1234"
if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Wrong credentials")

# Checking a number whether even or odd
num = int(input("Enter a number:"))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# Grade checking using python codes 
num = int(input("Enter a number:"))
if num >= 90:
    print("Grade A")
elif num >= 80:
    print("Grade B")
elif num >= 60:
    print("Grade C")
else:
    print("Grade D")
    
