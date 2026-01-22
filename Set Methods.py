# Creating a set
numbers = {1, 2, 3, 4, 5}
print("Original set:", numbers)

# add() – add a single element
numbers.add(6)
print("After add(6):", numbers)

# update() – add multiple elements (can be list, tuple, set)
numbers.update([7, 8], {9, 10})
print("After update([7,8], {9,10}):", numbers)

# remove() – remove a specific element (raises error if not found)
numbers.remove(3)
print("After remove(3):", numbers)

# discard() – remove an element if present (no error if not found)
numbers.discard(100)  # 100 not present, no error
print("After discard(100):", numbers)

# pop() – remove and return a random element
popped = numbers.pop()
print("Popped element:", popped)
print("After pop():", numbers)

# clear() – remove all elements
numbers.clear()
print("After clear():", numbers)

# copy() – make a shallow copy of the set
numbers = {1, 2, 3, 4, 5}
numbers_copy = numbers.copy()
print("Copied set:", numbers_copy)

# union() – union of two sets (returns a new set)
A = {1, 2, 3}
B = {3, 4, 5}
print("Union of A and B:", A.union(B))

# intersection() – common elements
print("Intersection of A and B:", A.intersection(B))

# difference() – elements in A not in B
print("Difference A - B:", A.difference(B))

# symmetric_difference() – elements in A or B but not both
print("Symmetric difference A ^ B:", A.symmetric_difference(B))

# issubset() – check if A is subset of B
print("Is A subset of B?", A.issubset(B))

# issuperset() – check if A is superset of B
print("Is A superset of B?", A.issuperset(B))

# isdisjoint() – check if A and B have no common elements
C = {6, 7}
print("Are A and C disjoint?", A.isdisjoint(C))
