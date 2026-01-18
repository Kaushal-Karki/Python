# Assigning a string to the variable 'str'
str = "Time is a time but time is not a time"

# Print characters from index 0 to 4 (0 is included, 5 is excluded)
print(str[0:5])      # Output: Time 

# Print the entire string from start to end
print(str[0:])       # Output: Time is a time but time is not a time

# Print characters from start up to index 19
print(str[:20])      # Output: Time is a time but

# Print characters using negative indexing (from -37 to -10)
print(str[-37:-10])  # Output: is a time but time is

# Print the total length of the string
print(len(str))      # Output: 41
