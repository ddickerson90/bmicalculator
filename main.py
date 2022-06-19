height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = round(weight / height ** 2)
if bmi <= 18.5:
  print(f"Your BMI is {bmi}, You are underweight")
elif bmi <= 25:
  print(f"Your BMI is {bmi}, You are normal weight")
elif bmi <= 30:
  print(f"Your BMI is {bmi}, You are overweight")
elif bmi <= 35:
  print(f"Your BMI is {bmi}, You are obese")
elif bmi > 35:
  print(f"Your BMI is {bmi}, You are clinically obese")1
