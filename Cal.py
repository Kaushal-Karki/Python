# Input two numbers from the user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Perform all basic arithmetic operations
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division a/b:", a / b)
print("Division b/a:", b / a)

# Provide choices for user to select an operation
print("\n1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Input the user's choice
choice = int(input("Enter your choice: "))

# Perform operation based on user choice using if-elif-else
if choice == 1:
    print("Result:", a + b)
elif choice == 2:
    print("Result:", a - b)
elif choice == 3:
    print("Result:", a * b)
elif choice == 4:
    print("Result:", a / b)
else:
    print("Invalid choice")
