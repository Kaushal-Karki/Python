# Input marks for each subject
J = float(input("Enter your Java Marks: "))
C = float(input("Enter your C Marks: "))
Js = float(input("Enter your Js Marks: "))
Cpp = float(input("Enter your C++ Marks: "))
Cshap = float(input("Enter your C# Marks: "))

# Check pass/fail and valid marks range (35 to 100)
if (
    35 <= J <= 100 and   # Java marks check
    35 <= C <= 100 and   # C marks check
    35 <= Js <= 100 and  # JavaScript marks check
    35 <= Cpp <= 100 and # C++ marks check
    35 <= Cshap <= 100   # C# marks check
):
    print("Pass")
else:
    # If any subject is failed or marks are invalid
    print("NQ")
    print("Invalid marks entered")
    exit()  # Stop program execution

# Calculate average marks
marks = (J + C + Js + Cpp + Cshap) / 5

# Display separator
print("--------------------------------------")

# Display average marks
print("Average Marks:", marks)

# Grade calculation based on average marks
if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B+")
elif marks >= 60:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C+")
elif marks >= 40:
    print("Grade: C")
else:
    print("Grade: D")

# End of program
print("--------------------------------------")
#conditional statements