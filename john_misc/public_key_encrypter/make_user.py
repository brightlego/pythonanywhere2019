import re
import os

def cs():
    print("\n"*50)
a = os.path.dirname(os.path.realpath(__file__))
print a
username = raw_input("What is your new username? ")
usernames = file("./usernames.txt","r").read().strip().split("\n")

while username in usernames or re.search("\b[a-zA-Z]",username) or re.search("\s",username):
    cs()
    if username in usernames:
        print("That name is already taken.")
    elif re.search("\b[a-zA-Z]",username):
        print("Username must start with a letter")
    else:
        print("No whitespace allowed in username.")
    username = raw_input("What is your new username? ")
cs()
password = raw_input("What is your password? ")
while re.match("\s",password):
    cs()
    print("No whitespace allowed in password.")
    password = raw_input("What is your password? ")
cs()
password_2 = raw_input("Type your password again for verification: ")
while password_2 != password:
    cs()
    password_2 = raw_input("Passwords do not match. Try again: ")
cs()
print "Thank you",username,"your account has been set up."