# Create a dictionary
student = {
    "name": "Yogendra",
    "age": 19,
    "course": "BCA"
}

# get() – get value of a key
print("Name:", student.get("name"))

# keys() – get all keys
print("Keys:", student.keys())

# values() – get all values
print("Values:", student.values())

# items() – get key-value pairs
print("Items:", student.items())

# update() – update or add elements
student.update({"age": 20, "college": "Aims College"})
print("After update:", student)

# pop() – remove a key
student.pop("course")
print("After pop:", student)

# popitem() – remove last inserted item
student.popitem()
print("After popitem:", student)

# setdefault() – get value, add if not present
student.setdefault("gender", "Male")
print("After setdefault:", student)

# copy() – copy dictionary
new_student = student.copy()
print("Copied dictionary:", new_student)

# clear() – remove all items
student.clear()
print("After clear:", student)
