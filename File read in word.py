# Open the file in read mode
f = open("time.txt", "r")

# Read first 5 characters from the file
data = f.read(5)

# Print the data read from the file
print(data)

# Close the file properly
f.close()
