import re

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

email = input("Enter your email: ")
if validate_email(email):
    print("Valid Email ✅")
else:
    print("Invalid Email ❌")
