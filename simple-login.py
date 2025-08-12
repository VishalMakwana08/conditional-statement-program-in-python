
# Create a simple login system with username and password validation.

# Step 1: Hardcoded username and password
correct_username = "admin"
correct_password = "12345"

# Step 2: Get username and password from the user
username = input("Enter username: ")
password = input("Enter password: ")

# Step 3: Validate username and password
if username == correct_username and password == correct_password:
    print("Login Successful ✅ Welcome,", username)
else:
    print("Login Failed ❌ Incorrect username or password")
