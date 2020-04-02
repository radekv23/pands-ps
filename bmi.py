# Radoslaw Wojtczak - G00352937
# This is a program to calculate
# BMI (body maas index)

#getting weight and height input from the user
weight = float(input("Enter yout weight in kg: "))
height = float(input("Enter yout height in cm: "))

#calculating m2
meters = (height * height) *100

#calculating BMI
bmi = (weight / meters) 

#showing results to the user
print("BMI is: ", bmi)