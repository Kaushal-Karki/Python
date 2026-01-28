# Open the file in read mode and store it in variable f
f = open("time.txt", "rt")

# Read the content of the file
data = f.read()

# Print file content
print(data)

# Print the type of data
print(type(data))

# Close the file
f.close()
