# Radoslaw Wojtczak - G00352937
# program that asks the user to input any positive integer and outputs the successive values of the following calculation.
# At each step calculate the next value by taking the current value and, if it is even, divide it by two,
#  but if it is odd, multiply it by three and add one. Have the program end if the current value is one.

#asking for input
positive = int(input("Enter posivive value:"))

#if input is negative value print message and stop
while positive < 0:
    print (positive,"is not a positive number")
    break

#prints input when positive
while positive > 0:
    print (positive)
    break

#perform calculations until equals 1
while positive > 1:
    if positive % 2 == 0:
        positive =  int(positive/2)
    else:
        positive = int((positive*3)+1)
    print (positive)