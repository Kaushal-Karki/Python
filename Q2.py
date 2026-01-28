# Open file in read + write mode
with open("A1.txt", "r+") as f:
    
    # Read the file content
    data = f.read()
    
    # Replace 'java' with 'Python'
    new_data = data.replace("Java", "Python")

# Open file in write mode to overwrite content
with open("A1.txt", "w") as f:
    
    # Write updated content back to the file
    f.write(new_data)

# Print updated content
print(new_data)
