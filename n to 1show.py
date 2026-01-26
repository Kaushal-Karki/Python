# Define a recursive function named show
def show(n):
    # Check the base condition
    # If n becomes 0, stop the recursion
    if n == 0:
        return
    
    # Print the current value of n
    print(n)
    
    # Recursive call:
    # Function calls itself with n-1
    show(n - 1)

# Take input from the user
n = int(input("Enter your number: "))

# Call the show function with user input
show(n)
print("End")
