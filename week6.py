#Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.
# You should create a function called sqrt that does this.

#creating function called sqrt
def sqrt (p):
    sroot=p**2
    return sroot

#getting input
p=float(input("Enter value to be squared: "))

#printing result
print(sqrt(p))
