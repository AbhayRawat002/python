weight = float(input("Enter your weight in kg: "))
height_cm = float(input("Enter your height in cm: "))

height_m = height_cm / 100

if weight <= 0 or height_m <= 0:
    print("Invalid data")
else:
    bmi = weight / (height_m ** 2)
    print("BMI:", round(bmi, 2))
