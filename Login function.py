# Login function
def login(username, password):
    correct_username = "admin"
    correct_password = "1234"

    if username == correct_username and password == correct_password:
        return "Login Successful"
    else:
        return "Invalid Username or Password"


# User input
u = input("Enter username: ")
p = input("Enter password: ")

# Function call
result = login(u, p)
print(result)
