#Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.
# Radoslaw Wojtczak - G00352936
#  creating a function called sqrt that does this.

#creating function called sqrt
def sqrt (s)
    sq=s ** 0.5
#getting input
s=float(input("Enter your value to be squared: "))

#printing result
print(sqrt(s))


#Second version delet '#'

#import math
#def sqrt (s):
  #  sq=math.sqrt(s)
  #  return sq

  #s=float(input("Enter your value to be squared: "))

#print(sqrt(s))