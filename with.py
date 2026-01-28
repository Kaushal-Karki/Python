# Open the file "Kaushal karki.txt" in read mode using with statement
with open("Kaushal karki.txt", "r") as f:
    
    # Read the entire content of the file
    data = f.read()
    
    # Print the content of the file
    print(data)
