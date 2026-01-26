def show(n):
    # Base condition to stop recursion
    if n == 0:
        print("End")
        return
    
    # Print the current value
    print(n)
    
    # Recursive call
    show(n - 1)

# Function call
show(3)
