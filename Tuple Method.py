# Create a tuple
tup = (1, 2, 3, 4, 5, 2, 3, 2)

# type() – check data type
print("Type:", type(tup))

# len() – length of tuple
print("Length:", len(tup))

# count() – count occurrences of an element
print("Count of 2:", tup.count(2))

# index() – find index of an element
print("Index of 3:", tup.index(3))

# Accessing elements (indexing)
print("First element:", tup[0])

# Slicing tuple
print("Slice (1 to 5):", tup[1:5])

# Iterating through tuple
print("Tuple elements:")
for i in tup:
    print(i)

# min() – minimum value
print("Minimum value:", min(tup))

# max() – maximum value
print("Maximum value:", max(tup))

# sum() – sum of tuple elements
print("Sum:", sum(tup))

# Tuple concatenation
tup2 = (10, 20)
new_tup = tup + tup2
print("After concatenation:", new_tup)

# Tuple repetition
repeat_tup = tup * 2
print("After repetition:", repeat_tup)
