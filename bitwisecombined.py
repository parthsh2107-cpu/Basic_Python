# Problem1 - Given x = 10, write a Python program to perform a bitwise OR operation between x and x left-shifted by 1 position, and print the result.

x = 10
y = x << 1
result = x | y
print(result)
    
# Problem2 - Given p = 14, write a Python program to perform a bitwise XOR operation between p and the bitwise NOT of p, and print the result.

p = 14
y = ~p
result = p ^ y
print(result)

# Problem3 - Given a = 20 and b = 15, write a Python program to perform a bitwise AND operation on a and b, then left shift the result by 1 position, and print the result.

a = 20
b = 15
result = a & b
result = result << 1
print("Final Result:", result)
