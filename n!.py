# Define a function to calculate factorial using recursion
def fact(n):
    # Base condition:
    # Factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive call
        return n * fact(n - 1)

# Take input from the user
n = int(input("Enter your number: "))

# Call the function and print the result
print("Factorial =", fact(n))
