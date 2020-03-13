# Radoslaw Wojtczak - G00352937
# program that asks the user to input any positive integer and outputs the successive values of the following calculation.
# At each step calculate the next value by taking the current value and, if it is even, divide it by two,
#  but if it is odd, multiply it by three and add one. Have the program end if the current value is one.

#asking for input
a = int(input("Enter posivive value:"))

#if input is negative value print message and stop
if a < 0:
    print (a,"is not a positive number")
   # break

#prints input when positive
elif a > 0:
    print (a)
  #  break

#perform calculations until equals 1
if a > 1:
    if a % 2 == 0:
        a =  int(a/2)
    else:
        a = int((a*3)+1)
    print (a)