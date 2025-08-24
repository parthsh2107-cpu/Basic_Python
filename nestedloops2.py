# NESTED CONDITIONS - 2

# Problem1- Write a program to check if a person is 18 or older, and if so, whether they are an Indian citizen.

age = int(input("Enter your age:"))
citizenship = input("Enter your citizenship:")
if age >= 18:
    if citizenship == "indian":
        print("You are 18 year older and indian citizen")
    else:
        print("You are 18 years older but not an indian citizen")
else:
    print("You are below 18")

# Problem2- Write a program that checks if a score is valid (0-100), then prints 'Pass' if above 40.

score = int(input("Enter your score"))
if 0 <= score <= 100:
    print("Valid score")
    if score > 40:
        print("Pass")
    else:
        print("Fail")
else:
    print("Invalid score")


