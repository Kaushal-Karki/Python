# ---------- WRITE MODE (w) ----------
f = open("data.txt", "w")
f.write("This is write mode\n")
f.close()


# ---------- READ MODE (r) ----------
f = open("data.txt", "r")
print("Read mode:")
print(f.read())
f.close()


# ---------- APPEND MODE (a) ----------
f = open("data.txt", "a")
f.write("This line is added using append mode\n")
f.close()


# ---------- READ + WRITE MODE (r+) ----------
f = open("data.txt", "r+")
print("\nRead + Write mode:")
print(f.read())
f.write("Added using r+ mode\n")
f.close()


# ---------- WRITE + READ MODE (w+) ----------
f = open("data2.txt", "w+")
f.write("This file is created using w+ mode\n")
f.seek(0)
print("\nWrite + Read mode:")
print(f.read())
f.close()


# ---------- APPEND + READ MODE (a+) ----------
f = open("data2.txt", "a+")
f.write("Added using a+ mode\n")
f.seek(0)
print("\nAppend + Read mode:")
print(f.read())
f.close()


# ---------- EXCLUSIVE CREATION MODE (x) ----------
try:
    f = open("newfile.txt", "x")
    f.write("File created using x mode\n")
    f.close()
except FileExistsError:
    print("\nFile already exists (x mode)")


# ---------- BINARY MODE (wb / rb) ----------
f = open("binary.bin", "wb")
f.write(b"Binary data example")
f.close()

f = open("binary.bin", "rb")
print("\nBinary mode:")
print(f.read())
f.close()


# ---------- TEXT MODE (default 't') ----------
f = open("textfile.txt", "wt")
f.write("Text mode file\n")
f.close()

f = open("textfile.txt", "rt")
print("\nText mode:")
print(f.read())
f.close()
