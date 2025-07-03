def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    return bmi, category

w = float(input("Enter weight (kg): "))
h = float(input("Enter height (m): "))
bmi, cat = calculate_bmi(w, h)
print(f"BMI: {bmi:.2f} - {cat}")
