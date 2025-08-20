# Assume number is 15 check it is divisible by both 3 and 5 or not
number = 15
if number % 3 == 0 and number % 5 == 0:
    print(f"{number} is divisible by both 3 and 5")
else:
    print(f"{number} is not divisible by both 3 an d 5")

# Write a statement to check whether marks is in range from 0 to 100 assume marks = 85

marks = 85
if marks in range(0,101):
    print("Yes")
else:
    print("No")
