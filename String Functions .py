# Sample string
s = "  Hello, Python World!  "
s2 = "python programming"
s3 = "123abc"

print("Original string:", s)

# 1. capitalize() – Capitalize first character
print("capitalize():", s2.capitalize())

# 2. casefold() – Lowercase string (stronger than lower())
print("casefold():", s2.casefold())

# 3. center(width) – Center string with spaces
print("center(30):", s2.center(30, "*"))

# 4. count(substring) – Count occurrences
print("count('o'):", s.count('o'))

# 5. encode() – Encode string
print("encode():", s.encode())

# 6. endswith() – Check if string ends with substring
print("endswith('World!'):", s.endswith("World!"))

# 7. expandtabs() – Replace tab (\t) with spaces
s_tab = "Hello\tPython"
print("expandtabs():", s_tab.expandtabs(4))

# 8. find() – Find first index of substring
print("find('Python'):", s.find("Python"))

# 9. format() – Format string
print("format():", "My name is {}".format("Yogendra"))

# 10. format_map() – Similar to format() but with dict
d = {"name": "Yogendra"}
print("format_map():", "My name is {name}".format_map(d))

# 11. index() – Find index (error if not found)
print("index('Python'):", s.index("Python"))

# 12. isalnum() – Check alphanumeric
print("isalnum():", s3.isalnum())

# 13. isalpha() – Check alphabet only
print("isalpha():", s2.isalpha())

# 14. isascii() – Check ASCII characters
print("isascii():", s.isascii())

# 15. isdecimal() – Check decimal numbers
print("isdecimal():", "123".isdecimal())

# 16. isdigit() – Check digits
print("isdigit():", "123".isdigit())

# 17. isidentifier() – Check valid Python identifier
print("isidentifier():", "my_var".isidentifier())

# 18. islower() – Check lowercase
print("islower():", s2.islower())

# 19. isnumeric() – Check numeric
print("isnumeric():", "123".isnumeric())

# 20. isprintable() – Check printable characters
print("isprintable():", s.isprintable())

# 21. isspace() – Check whitespace
print("isspace():", "   ".isspace())

# 22. istitle() – Check title case
print("istitle():", "Hello Python".istitle())

# 23. isupper() – Check uppercase
print("isupper():", "HELLO".isupper())

# 24. join() – Join iterable with string as separator
print("join():", "-".join(["Python", "Java", "C"]))

# 25. ljust() – Left justify
print("ljust(30, '*'):", s2.ljust(30, "*"))

# 26. lower() – Convert to lowercase
print("lower():", s.upper().lower())

# 27. lstrip() – Remove leading spaces
print("lstrip():", s.lstrip())

# 28. partition() – Split into 3 parts at separator
print("partition('Python'):", s.partition("Python"))

# 29. replace() – Replace substring
print("replace('Python','Java'):", s.replace("Python","Java"))

# 30. rfind() – Find last occurrence
print("rfind('o'):", s.rfind("o"))

# 31. rindex() – Last index (error if not found)
print("rindex('o'):", s.rindex("o"))

# 32. rjust() – Right justify
print("rjust(30,'*'):", s2.rjust(30,"*"))

# 33. rsplit() – Split from right
print("rsplit():", s.split())

# 34. rstrip() – Remove trailing spaces
print("rstrip():", s.rstrip())

# 35. split() – Split into list
print("split():", s.split())

# 36. splitlines() – Split into lines
multi = "Line1\nLine2\nLine3"
print("splitlines():", multi.splitlines())

# 37. startswith() – Check starting substring
print("startswith('  Hello'):", s.startswith("  Hello"))

# 38. strip() – Remove leading & trailing spaces
print("strip():", s.strip())

# 39. swapcase() – Swap upper/lower case
print("swapcase():", s2.swapcase())

# 40. title() – Title case each word
print("title():", s2.title())

# 41. translate() – Translate using mapping
table = str.maketrans("H","J")
print("translate():", s.translate(table))

# 42. upper() – Convert to uppercase
print("upper():", s2.upper())

# 43. zfill() – Pad string with zeros
num = "42"
print("zfill(5):", num.zfill(5))

# 44. partition() – Split into 3 parts
print("partition('Python'):", s.partition("Python"))

# 45. rpartition() – Split into 3 parts from right
print("rpartition('Python'):", s.rpartition("Python"))

# 46. isprintable() – Check printable characters
print("isprintable():", s.isprintable())

# 47. expandtabs() – Convert tabs to spaces
tab_str = "1\t2\t3"
print("expandtabs():", tab_str.expandtabs(4))
