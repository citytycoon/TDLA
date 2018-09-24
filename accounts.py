# name = input("Username: ")
# name = input("Email: ")
# name = input("Password: ")
# name = input("Confirm Password: ")

# # Here the user account is created
# def register(name, email, password, confirm_password):
#     register[password] = name
#     return register

# print("Your account has been added !!! Thank you")

# def login(username):
#     if username == ' ':
#         return 'City Tycoon'
#     return None

username_password = {}
print("Sign up for To do List\n")
name = str(input("Please enter your preferred username.\n"))
passcode = str(input("Thank you, now enter a password as well.\n"))
username_password[name] = passcode
print(username_password)

login_username = str(input("Please enter your username.\n"))
login_password = str(input("Please enter your password.\n"))
if login_username in username_password and login_password == username_password[login_username]:
    print("Logged in")
else:
    print("Either the password and username is incorrect")
# def unauthorized():
#     return make_response(jsonify({'message': 'Unauthorized access'}), 403)


app = ('__name__')    