# Open the file in read mode
f = open("time.txt", "r")

# Read one line from the file
line1 = f.readline()

# Read two line from the file
line2 = f.readline()

# Print the line
print(line1)

# Print the line
print(line2)

# Close the file properly
f.close()
