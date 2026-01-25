# Function to calculate factorial of a number
def factorial(n):
    if n == 0 or n == 1:  # Factorial of 0 or 1 is 1
        return 1
    else:
        result = 1
        for i in range(2, n + 1):  # Multiply numbers from 2 to n
            result *= i
        return result

# Taking input from the user
n = int(input("Enter a number: "))

# Function call and print result
print(f"Factorial of {n} is {factorial(n)}")
