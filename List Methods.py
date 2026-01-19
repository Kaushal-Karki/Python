# Creating a list
marks = [98, 45, 56, 78, 64, 57, 78]

# len() – length of list
print("Length:", len(marks))

# append() – add element at end
marks.append(88)
print("After append:", marks)

# insert() – insert at specific index
marks.insert(2, 99)
print("After insert:", marks)

# extend() – add another list
marks.extend([60, 70])
print("After extend:", marks)

# remove() – remove first occurrence of value
marks.remove(45)
print("After remove:", marks)

# pop() – remove element by index
marks.pop(3)
print("After pop:", marks)

# index() – find index of element
print("Index of 78:", marks.index(78))

# count() – count occurrences
print("Count of 78:", marks.count(78))

# sort() – sort list
marks.sort()
print("After sort:", marks)

# reverse() – reverse list
marks.reverse()
print("After reverse:", marks)

# min() – minimum value
print("Minimum:", min(marks))

# max() – maximum value
print("Maximum:", max(marks))

# sum() – sum of list elements
print("Sum:", sum(marks))

# copy() – copy list
new_marks = marks.copy()
print("Copied list:", new_marks)

# clear() – remove all elements
marks.clear()
print("After clear:", marks)
