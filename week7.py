# Radoslaw Wojtczak - G00352937
# Write a program that reads in a text file and outputs the number of e's it contains. 
# The program should take the filename from an argument on the command line.


# variables : file for getting txt from user and counter to start counting "e"
file=input("Enter your file name:") # my file is houn.txt
counter = 0
 

 # method yo count numer of e's
with open(file, 'r') as f:
    for line in f:
        words = line.split()
        for i in words:
            for letter in i:
                if(letter=="e"):
                    counter=counter+1
# printing our results
print("Count of the letter 'e': ", counter)
