#Write a program that outputs whether or not today is a weekday. An example of running this program on a Thursday is given below.git add.#

#importing required packed 
import datetime

#geting variable from datetime
dayOfWeek = datetime.datetime.today().weekday()

#starting if statement to get to know is it weekend, yet
if dayOfWeek<5:
    print ("Yes, unfortunately today is a weekday.")
else:
    print ("It is the weekend, yay!")