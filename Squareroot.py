#Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.
# Radoslaw Wojtczak - G00352936
#  creating a function called sqrt that does this.

# Enter positive floating point number as input.
s = float(input('Please, enter a positive number: '))

# You store the number in s and find the square root using the **
if s < 0:
    print("Please, enter a positive number.")
else:
   sqrt = s ** 0.5

# printing the square root
print('The square root is ', sqrt)



#Second version delet '#'

#import math
#def sqrt (s):
  #  sq=math.sqrt(s)
  #  return sq

  #s=float(input("Enter your value to be squared: "))

#print(sqrt(s))