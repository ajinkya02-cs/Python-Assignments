def check_voting_eligibility(age):
    if age >= 18:
        return "You are eligible to vote ✅"
    else:
        return f"You are not eligible to vote ❌\nPlease wait {18 - age} more year(s)."

try:
    age = int(input("Enter your age: "))
    result = check_voting_eligibility(age)
    print(result)
except ValueError:
    print("Invalid input. Please enter a valid number.")
