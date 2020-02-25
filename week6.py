#Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.
# You should create a function called sqrt that does this.

#importing math functions
import math

#creating function called sqrt
def sqrt (s):
    sq=math.sqrt(s)
    return sq

#getting input
s=float(input("Enter value to be squared: "))

#printing result
print(sqrt(s))