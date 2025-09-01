weight = float(input())
height = float(input())

bmi = weight / ( height ** 2)

print(f"Your bmi is {bmi}")

if (bmi < 18.5):
    print("Underweight")
elif (bmi >= 18.5 and bmi <= 24.9) :
    print("Normal weight")
elif (bmi >= 25 and bmi <= 29.9):
    print("Overweight")
else : 
    print("Obese")