we = float(input("Enter your weight: "))
he = float(input("Enter your height: "))

bmi = float(we / (he ** 2))
print(f'our BMI is  {bmi}')

if bmi <= 18.5:
    print("You are under weight")
elif bmi == 18.6 or bmi <= 24.9:
    print("You are having a healthy weight")
elif bmi == 25 or bmi <= 29.9:
    print("You are Overweight")
else:
    print("You are Obese, Kindly see your Doctor")
