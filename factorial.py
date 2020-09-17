# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# This function returns the factorial of a given number.

def factorial(n):
    # Write code here
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    print(n * factorial(n - 1))
n = int(input("input a number to compute the factorial: "))
print(factorial(n))

print(factorial(5))

# print(factorial(5))
# => 120