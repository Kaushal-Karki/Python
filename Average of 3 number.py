# Function to calculate average of three numbers
def Average(a, b, c):
    # Add all three numbers and divide by 3
    return (a + b + c) / 3


# Taking input from the user
a = float(input("Enter first number: "))   # First number
b = float(input("Enter second number: "))  # Second number
c = float(input("Enter third number: "))   # Third number


# Calling the function and storing the result
result = Average(a, b, c)

# Printing the average
print("Average =", result)
