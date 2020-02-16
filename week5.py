#Write a program that outputs whether or not today is a weekday. An example of running this program on a Thursday is given below.

import datetime

dayOfWeek = datetime.datetime.today().weekday()

if dayOfWeek<5:
    print ("Yes, unfortunately today is a weekday.")
else:
    print ("It is the weekend, yay!")