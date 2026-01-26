# Recursive function to calculate sum of first n natural numbers
def sum_n(n):
    # Base condition
    if n == 0:
        return 0
    else:
        # Recursive call
        return n + sum_n(n - 1)

# Input from user
n = int(input("Enter a number: "))

# Output
print("Sum =", sum_n(n))
